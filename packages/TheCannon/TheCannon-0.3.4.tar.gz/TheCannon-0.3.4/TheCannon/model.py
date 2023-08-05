""" Make a single model class to rule them all """
from .dataset import Dataset
from .train_model import train_model as _train_model
from .infer_labels import infer_labels
from .spectral_model import diagnostics as _diagnostics
from .helpers.triangle import corner
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from copy import deepcopy

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

LARGE = 200.
SMALL = 1. / LARGE

class CannonModel(object):
    def __init__(self, dataset, order):
        if not isinstance(dataset, Dataset):
            txt = 'Expecting a Dataset instance, got {0}'
            raise TypeError(txt.format(type(dataset)))
        self.dataset = dataset
        self._model = None
        self.order = order


    @property
    def model(self):
        """ return the model definition or raise an error if not trained """
        if self._model is None:
            raise RuntimeError('Model not trained')
        else:
            return self._model


    def train(self, *args, **kwargs):
        """ Train the model """
        self._model = _train_model(self.dataset)


    def diagnostics(self):
        """Run a set of diagnostics on the model.

        Plot the 0th order coefficients as the baseline spectrum.
        Overplot the continuum pixels.

        Plot each label's leading coefficient as a function of wavelength.
        Color-code by label.

        Histogram of the chi squareds of the fits.
        Dotted line corresponding to DOF = npixels - nlabels
        """
        _model_diagnostics(self.dataset, self.model)


    def infer_labels(self, dataset):
        """
        Uses the model to solve for labels of the test set.

        Parameters
        ----------
        dataset: Dataset
            dataset that needs label inference

        Returns
        -------
        output of infer_labels
        """
        return infer_labels(self.model, dataset)


    def draw_spectra(self, dataset):
        """
        Parameters
        ----------
        dataset: Dataset
            dataset that needs label inference

        Returns
        -------
        cannon_set: Dataset
            same dataset as the input value with updated fluxes and variances
        """
        coeffs_all, covs, scatters, red_chisqs, pivots, label_vector = self.model
        nstars = len(dataset.test_SNR)
        cannon_fluxes = np.zeros(dataset.test_flux.shape)
        cannon_ivars = np.zeros(dataset.test_ivar.shape)
        for i in range(nstars):
            x = label_vector[:,i,:]
            spec_fit = np.einsum('ij, ij->i', x, coeffs_all)
            cannon_fluxes[i,:] = spec_fit
            bad = dataset.test_ivar[i,:] == SMALL
            cannon_ivars[i,:][~bad] = 1. / scatters[~bad] ** 2
        cannon_set = deepcopy(dataset)
        cannon_set.test_flux = cannon_fluxes
        cannon_set.test_ivar = cannon_ivars
        return cannon_set


    def split_array(self, array, num):
        """ split an array into a certain number of segments

        Parameters
        ----------
        array: numpy ndarray
            array to be split

        num: int
            number of elements to split array into

        Returns
        ------
        out: list 
            split array
        """
        avg = len(array) / float(num)
        out = []
        last = 0.0
        while last < len(array):
            out.append(array[int(last):int(last+avg)])
            last += avg
        return out


    def diagnostics(
            self, baseline_spec_plot_name = "baseline_spec_with_cont_pix",
            leading_coeffs_plot_name = "leading_coeffs.png",
            chisq_dist_plot_name = "modelfit_chisqs.png"):
        """Run a set of diagnostics on the model.

        Plot the 0th order coefficients as the baseline spectrum.
        Overplot the continuum pixels.

        Plot each label's leading coefficient as a function of wavelength.
        Color-code by label.

        Histogram of the chi squareds of the fits.
        Dotted line corresponding to DOF = npixels - nlabels

        Parameters
        ----------
        (optional) baseline_spec_plot_name: str
            plot name
        (optional) leading_coeffs_plot_name: str
            plot name
        (optional) chisq_dist_plot_name: str
            plot name
        """
        dataset = self.dataset
        model = self.model
        contmask = dataset.contmask
        lams = dataset.wl
        label_names = dataset.get_plotting_labels()
        coeffs_all, covs, scatters, chisqs, pivots, label_vector = model
        npixels = len(lams)
        nlabels = len(pivots)

        if contmask != None:
            # Baseline spectrum with continuum
            baseline_spec = coeffs_all[:,0]
            bad = np.round(baseline_spec,5) == 0
            baseline_spec = np.ma.array(baseline_spec, mask=bad)
            lams = np.ma.array(lams, mask=bad)

            # Continuum pixels
            contpix_lambda = lams[contmask]
            y = baseline_spec[contmask]

            # Split into ten segments
            nseg = 10
            lams_seg = self.split_array(lams.compressed(), nseg)
            xmins = [] 
            xmaxs = [] 
            for seg in lams_seg:
                xmins.append(seg[0])
                xmaxs.append(seg[-1])

            for i in range(nseg):
                fig, axarr = plt.subplots(2, sharex=True)
                plt.xlabel(r"Wavelength $\lambda (\AA)$")
                plt.xlim(xmins[i], xmaxs[i])
                ax = axarr[0]
                ax.step(lams, baseline_spec, where='mid', c='k', linewidth=0.3,
                        label=r'$\theta_0$' + "= the leading fit coefficient")
                ax.scatter(contpix_lambda, y, s=1, color='r',
                        label="continuum pixels")
                ax.legend(loc='lower right', 
                        prop={'family':'serif', 'size':'small'})
                ax.set_title("Baseline Spectrum with Continuum Pixels")
                ax.set_ylabel(r'$\theta_0$')
                ax = axarr[1]
                ax.step(lams, baseline_spec, where='mid', c='k', linewidth=0.3,
                     label=r'$\theta_0$' + "= the leading fit coefficient")
                ax.scatter(contpix_lambda, y, s=1, color='r',
                        label="continuum pixels")
                ax.set_title("Baseline Spectrum with Continuum Pixels, Zoomed")
                ax.legend(loc='upper right', prop={'family':'serif', 
                    'size':'small'})
                ax.set_ylabel(r'$\theta_0$')
                ax.set_ylim(0.95, 1.05)
                print("Diagnostic plot: fitted 0th order spec w/ cont pix")
                print("Saved as %s_%s.png" % (baseline_spec_plot_name, i))
                plt.savefig(baseline_spec_plot_name + "_%s" %i)
                plt.close()

        # Leading coefficients for each label & scatter
        bad = scatters < 0.0002
        scatters = np.ma.array(scatters, mask=bad)
        lams = np.ma.array(lams, mask=bad)
        fig, axarr = plt.subplots(nlabels+1, figsize=(8,8), sharex=True)
        ax1 = axarr[0]
        plt.subplots_adjust(hspace=0.001)
        nbins = len(ax1.get_xticklabels())
        for i in range(1,nlabels+1):
            axarr[i].yaxis.set_major_locator(
                    MaxNLocator(nbins=nbins, prune='upper'))
        plt.xlabel(r"Wavelength $\lambda (\AA)$", fontsize=14)
        plt.xlim(np.ma.min(lams), np.ma.max(lams))
        plt.tick_params(axis='x', labelsize=14)
        axarr[0].set_title(
                "First-Order Fit Coeffs and Scatter from the Spectral Model",
                fontsize=14)
        ax.locator_params(axis='x', nbins=10)
        first_order = np.zeros((len(coeffs_all[:,0]), nlabels))
        for i in range(0, nlabels):
            ax = axarr[i]
            lbl = r'$%s$'%label_names[i]
            ax.set_ylabel(lbl, fontsize=14)
            ax.tick_params(axis='y', labelsize=14)
            ax.xaxis.grid(True)
            y = np.ma.array(coeffs_all[:,i+1], mask=bad)
            first_order[:, i] = y
            ax.step(lams, y, where='mid', linewidth=0.5, c='k')
            ax.locator_params(axis='y', nbins=4)
        ax = axarr[nlabels]
        ax.tick_params(axis='y', labelsize=14)
        ax.set_ylabel("scatter", fontsize=14)
        top = np.max(scatters[scatters < 0.8])
        stretch = np.std(scatters[scatters < 0.8])
        ax.set_ylim(0, top + stretch)
        ax.step(lams, scatters, where='mid', c='k', linewidth=0.7)
        ax.xaxis.grid(True)
        ax.locator_params(axis='y', nbins=4)
        print("Diagnostic plot: leading coeffs and scatters across wavelength.")
        print("Saved as %s" %leading_coeffs_plot_name)
        fig.savefig(leading_coeffs_plot_name)
        plt.close(fig)

        # triangle plot of the higher-order coefficients
        labels = [r"$%s$" % l for l in label_names]
        fig = corner(first_order, labels=labels, show_titles=True,
                     title_args = {"fontsize":12})
        filename = "leading_coeffs_triangle.png"
        fig.savefig(filename)
        plt.close(fig)

        # Histogram of the chi squareds of ind. stars
        plt.hist(np.sum(chisqs, axis=0), color='lightblue', alpha=0.7)
        dof = len(lams) - coeffs_all.shape[1]   # for one star
        plt.axvline(x=dof, c='k', linewidth=2, label="DOF")
        plt.legend()
        plt.title("Distribution of " + r"$\chi^2$" + " of the Model Fit")
        plt.ylabel("Count")
        plt.xlabel(r"$\chi^2$" + " of Individual Star")
        print("Diagnostic plot: histogram of the red chi squareds of the fit")
        print("Saved as %s" %chisq_dist_plot_name)
        plt.savefig(chisq_dist_plot_name)
        plt.close()

    # convenient namings to match existing packages
    predict = infer_labels
    fit = train
