""" Code for LAMOST data munging """

from __future__ import (absolute_import, division, print_function,)
import numpy as np
import scipy.optimize as opt
from scipy import interpolate 
import os
import sys
from cannon.helpers import Table
from cannon.dataset import Dataset
import matplotlib.pyplot as plt

# python 3 special
PY3 = sys.version_info[0] > 2
if not PY3:
    range = xrange

try:
    from astropy.io import fits as pyfits
except ImportError:
    import pyfits

def get_pixmask(file_in, wl, middle, flux, ivar):
    """ Return a mask array of bad pixels for one object's spectrum

    Bad pixels are defined as follows: fluxes or ivars are not finite, or 
    ivars are negative

    Major sky lines. 4046, 4358, 5460, 5577, 6300, 6363, 6863

    Where the red and blue wings join together: 5800-6000

    Read bad pix mask: file_in[0].data[4] is the ormask 

    Parameters
    ----------
    fluxes: ndarray
        flux array

    flux_errs: ndarray
        measurement uncertainties on fluxes

    Returns
    -------
    mask: ndarray, dtype=bool
        array giving bad pixels as True values
    """
    npix = len(wl)
    
    bad_flux = (~np.isfinite(flux)) # count: 0
    bad_err = (~np.isfinite(ivar)) | (ivar <= 0)
    # ivar == 0 for approximately 3-5% of pixels
    bad_pix_a = bad_err | bad_flux
    
    # LAMOST people: wings join together, 5800-6000 Angstroms
    wings = np.logical_and(wl > 5800, wl < 6000)
    # this is another 3-4% of the spectrum
    ormask = (file_in[0].data[4] >0)
    # ormask = (file_in[0].data[4] > 0)[middle]
    # ^ problematic...this is over a third of the spectrum!
    bad_pix_b = wings | ormask
    # bad_pix_b = wings

    spread = 3 # due to redshift
    skylines = np.array([4046, 4358, 5460, 5577, 6300, 6363, 6863])
    bad_pix_c = np.zeros(npix, dtype=bool)
    for skyline in skylines:
        badmin = skyline-spread
        badmax = skyline+spread
        bad_pix_temp = np.logical_and(wl > badmin, wl < badmax)
        bad_pix_c[bad_pix_temp] = True
    # 34 pixels

    bad_pix_ab = bad_pix_a | bad_pix_b
    bad_pix = bad_pix_ab | bad_pix_c

    return bad_pix


def load_spectra(data_dir, filenames):
    """
    Extracts spectra (wavelengths, fluxes, fluxerrs) from apogee fits files

    Returns
    -------
    IDs: list of length nstars
        stellar IDs
    
    wl: numpy ndarray of length npixels
        rest-frame wavelength vector

    fluxes: numpy ndarray of shape (nstars, npixels)
        training set or test set pixel intensities

    ivars: numpy ndarray of shape (nstars, npixels)
        inverse variances, parallel to fluxes
        
    SNRs: numpy ndarray of length nstars
    """
    print("Loading spectra from directory %s" %data_dir)
    files = list(sorted(filenames))
    files = np.array(files)
    nstars = len(files)

    npix = np.zeros(nstars)
    for jj, fits_file in enumerate(files):
        file_in = pyfits.open("%s/%s" %(data_dir, fits_file))
        grid_all = np.array(file_in[0].data[2])
        if jj == 0:
            # all stars do NOT start out on the same wavelength grid
            # grid_all = np.array(file_in[0].data[2])
            # some spectra will end up with different pixels
            # because of the wavelength correction. so do this to ensure
            # that the interpolation never extrapolates...
            # values determined by experimentation, may change later
            # middle = np.logical_and(grid_all > 3705, grid_all < 9091)
            # only lost 10 pixels here
            # now, add on 200 pixels at the beginning to save the Ca H&K
            middle = np.logical_and(grid_all > 3905, grid_all < 9000)
            grid = grid_all[middle]
            npixels = len(grid) 
            SNRs = np.zeros(nstars, dtype=float)   
            fluxes = np.zeros((nstars, npixels), dtype=float)
            ivars = np.zeros(fluxes.shape, dtype=float)
            #badpixs = np.zeros((nstars, len(grid_all)), dtype=bool)
        flux = np.array(file_in[0].data[0])
        npix[jj] = len(flux)
        ivar = np.array((file_in[0].data[1]))
        # identify bad pixels PRIOR to shifting, so that the sky lines
        # don't move around
        badpix = get_pixmask(file_in, grid_all, middle, flux, ivar)
        flux = np.ma.array(flux, mask=badpix)
        ivar = np.ma.array(ivar, mask=badpix)
        SNRs[jj] = np.ma.median(flux*ivar**0.5)
        ivar = np.ma.filled(ivar, fill_value=0.)
        # correct for radial velocity of star
        redshift = file_in[0].header['Z']
        wlshift = redshift*grid_all
        wl = grid_all - wlshift
        # resample onto a common grid
        flux_rs = (interpolate.interp1d(wl, flux))(grid)
        ivar_rs = (interpolate.interp1d(wl, ivar))(grid)
        fluxes[jj,:] = flux_rs
        ivars[jj,:] = ivar_rs

    print("Spectra loaded")
    return grid, fluxes, ivars


def load_labels(label_file):
    """ Extracts training labels from file.

    Assumes that first row is # then label names, first col is # then 
    filenames, remaining values are floats and user wants all the labels.
    """
    print("Loading reference labels from file %s" %label_file)
    data = Table(label_file)
    data.sort('id')
    label_names = data.keys()[1:] # ignore id
    nlabels = len(label_names)
    print('%s labels:' %nlabels)
    print(label_names)
    labels = np.array([data[k] for k in label_names], dtype=float).T
    return data['id'], labels 
