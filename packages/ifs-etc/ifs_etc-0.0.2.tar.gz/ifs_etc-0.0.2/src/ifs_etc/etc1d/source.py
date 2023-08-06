import numpy as np
import pandas as pd
import os
import astropy.io.fits as fits
from scipy.integrate import simps
import pdb

refdata = os.path.abspath(os.path.dirname(__file__)+'/../refdata') + '/'


class read_template(object):

    def __init__(self, source):

        self.source = source
        self.line_definitions = self.source['lines']

        # snpp_path = '/Users/linlin/Pro/snpp_v1_05/refdata/'
        template_filename = refdata + 'sed/' + self.source['name']
        # filtera = snpp_path + 'normalization/filters/sdss_g0.par'
        # result = input_mag_model(self.source['normalization']['value'],
        #                          galtpl, filtera)  # scale the template to given brightness
        hdu = fits.open(template_filename)
        self.wave = hdu[1].data['wavelength']   # A
        self.flux = hdu[1].data['flux'] * 1e-12         # 10^-12 erg/s/A/cm2


class read_filter(object):
    # load the filters
    # filterfile = filtera  # '../sdss_g0.par'
    # filterpath='./'
    # filterfile=filterpath+filtersel   # ;fluxfilter: max=1, min=0, no particular unit
    def __init__(self, band):

        filterfile = refdata + 'normalization/filters/sdss_g0.par'
        # print('Filter File:', filterfile)

        band = pd.read_csv(filterfile, sep='\s+', header=None, comment='#')
        self.wave = band[0].values  # A
        self.throughput = band[1].values  # vaccum_pass
        self.wavemin = self.wave[0]
        self.wavemax = self.wave[-1]

        # find the central wavelength, effective wavelength, and FWHM of the given filter
        filtermid = (self.wavemax - self.wavemin) * 0.5  # A, central wavelength
        dwave = self.wave[1:] - self.wave[:-1]
        self.waveeff = np.nansum(dwave * self.wave[1:] * self.throughput[1:]) / \
                       np.nansum(dwave * self.throughput[1:])
                                                                            # A, effective wavelength
        rmax = np.max(self.throughput)
        nnn = np.where(self.throughput > 0.5 * rmax)[0]
        self.FWHMmin = self.wave[nnn[0]]      # wave range at FWHM
        self.FWHMmax = self.wave[nnn[-1]]
        self.wavefwhm = self.FWHMmax - self.FWHMmin  # A, FWHM


def filter_mag(objwave, objflux, filterwave, filterthroughtput, output='mag'):
    '''
    :param objwave: unit as A
    :param objflux: unit as erg/s/cm^2/A
    :param filterwave: unit as A
    :param filterthroughtput: unit as detector signal per photon (use vaccum_pass for space telescope,
                              otherwise select a given airmass)
    :return: AB magnitude in this band
    '''

    # resample the throughtput to objwave
    ind = (objwave >= np.min(filterwave)) & (objwave <= np.max(filterwave))
    wavetmp = objwave[ind]
    phot_frac = np.interp(wavetmp, filterwave, filterthroughtput)  # phot fraction (/s/A/cm^2?)
    # convert to energy fraction
    # E_frac = E0/hv * N_frac / E0 ~ N_frac/nu ~ N_frac * lambda
    energy_frac = phot_frac * wavetmp  # convert to energy fraction

    # convert the objflux to erg/s/cm^2/Hz
    c = 3e18    # A/s
    objflux_hz = objflux[ind] * (objwave[ind]**2) / c    # erg/s/scm^2/Hz

    from scipy.integrate import simps
    integrate_flux = simps(objflux_hz * energy_frac, c/wavetmp) / simps(energy_frac, c/wavetmp)

    if output == 'mag':
        mag = -2.5 * np.log10(integrate_flux) - 48.6
        return mag
    elif output == 'flux':
        return integrate_flux
    else:
        print('Error: output need to be "mag" or "flux". ')
        return np.nan


def normalized(template_wave, template_flux, config):

    # grid = get_grid(config)

    source = config['source']

    normalize = source['normalization']

    filter = read_filter(normalize['band'])

    ind_filter = (template_wave >= filter.wavemin) & (template_wave <= filter.wavemax)
    filter_wave = template_wave[ind_filter]
    filter_flux = np.interp(filter_wave, filter.wave, filter.throughput)
    filter_constant = simps(filter_flux * filter_wave, filter_wave)

    template_constant = simps(filter_flux * template_wave[ind_filter] * template_flux[ind_filter],
                              template_wave[ind_filter])

    u0 = normalize['value']
    u0 = 10**((u0 + 48.6)/(-2.5))         # target flux in erg/s/cm^2/Hz unit
    u0 = u0 * 3e18 / filter.waveeff**2    # erg/s/cm^2/A

    # geometry = source['geometry']
    # if geometry['type'] == 'Sersic':
    #
    #     xcen = grid.nx / 2 + geometry['x_offset']
    #     ycen = grid.ny / 2 + geometry['y_offset']
    #     rmaj = geometry['Re_major'] / grid.xspxsize
    #     rmin = geometry['Re_minor'] / grid.xspxsize
    #
    #     scaled_img = sersic(grid.nx, grid.ny, xcen, ycen,
    #              u0, rmaj, rmin/rmaj, geometry['PA'], geometry['sersic_n'])
    #
    # elif geometry['type'] == 'flat':
    #
    #     xcen = grid.nx / 2 + geometry['x_offset']
    #     ycen = grid.ny / 2 + geometry['y_offset']
    #
    #     scaled_img = flatbox(grid.nx, grid.ny, xcen, ycen,
    #                     u0, geometry['xwidth'], geometry['ywidth'])
    #
    # else:
    #     print('geometry should be one of these: ("Sersic" | "flat").')
    #     pdb.set_trace()

    factor = u0 * filter_constant / template_constant

    # norm_wave = np.zeros(shape=(len(template_wave), grid.ny, grid.nx), dtype=float)
    # norm_flux = np.zeros(shape=(len(template_wave), grid.ny, grid.nx), dtype=float)
    # for j in range(grid.ny):
    #     for i in range(grid.nx):
    norm_wave = template_wave                  # A
    norm_flux = template_flux * factor         # erg/s/cm^2/A


    # check the normalized magnitude should be normalized.value - 2.5*log(0.04)
    # mag2d = np.zeros(shape=(grid.ny, grid.nx), dtype=float)
    # for j in range(grid.ny):
    #     for i in range(grid.nx):
    mag = filter_mag(norm_wave, norm_flux,
                     filter_wave, filter_flux, output='mag')


    return norm_wave, norm_flux, mag


class ModelCube(object):

    def __init__(self, config):

        self.ccdspec_wave = np.arange(3500, 10000, 1.75555)
        self.ccdspec_nw = len(self.ccdspec_wave)

        # grid = get_grid(config)

        object = config['source']['spectrum']

        template = read_template(object)
        template_wave_interp = self.ccdspec_wave
        template_flux_interp = np.interp(template_wave_interp, template.wave, template.flux)

        # self.ccdspec_flux = np.zeros(shape=(self.ccdspec_nw, grid.ny, grid.nx), dtype=np.float32)

        self.wavecube, self.fluxcube, self.mag2d = normalized(template_wave_interp, template_flux_interp, config)

