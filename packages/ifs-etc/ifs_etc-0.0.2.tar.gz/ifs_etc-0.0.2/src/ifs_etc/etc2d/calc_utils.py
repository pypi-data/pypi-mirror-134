import os
import json
import pandas as pd
import pdb

snpp_refdata = os.getenv('SNPP_PATH') + 'refdata/'

def get_telescope_config():

    dict = {}
    dict['diameter'] = 200
    dict['obscure'] = 0.
    dict['coll_area'] = 31415.926535897932

    out_file = open(snpp_refdata + 'csst/telescope/config.json', "w")
    json.dump(dict, out_file, indent=2)
    out_file.close()

    return dict


def get_instrument_config():


    # throughput_file = os.path.join(os.getenv('SNPP_refdata'), 'csst', 'ifs', 'IFU_throughput.dat')
    # throughput = pd.read_csv(throughput_file,
    #                          sep='\s+', skiprows=1, header=None, names=['nm', 'q'])
    # lambdaq = throughput.nm.values * 10  # nm to A
    # qifs = throughput.q.values  # ; throughput of the whole system,
    # # ;assuming the total throughput cannot reach the theory value, 0.3 is the upper limit.
    # qifs[qifs >= 0.3] = 0.3
    # qinput = 1.0                    # the throughput of the telescope
    # qtot = qifs * qinput            # *qe ;qtot of CSST already includes the CCD efficiency


    dict = {}
    dict['fov_xsize'] = 6                   # arcsec
    dict['fov_ysize'] = 6                   # arcsec
    dict['spaxel_xsize'] = 0.2              # arcsec
    dict['spaxel_ysize'] = 0.2              # arcsec
    dict['ccd_xsize'] = 1.755555            # A, delta_lambda_per_pixel
    dict['ccd_ysize'] = 0.1                 # arcsec, spatial axis
    dict['readout_xbin'] = 1
    dict['readout_ybin'] = 1
    dict['gain'] = 1                            # e/ADU
    dict['dark'] = 0.017                        # e/s/pix
    dict['readout_noise'] = 4.0                 # e/pix
    dict['QE'] = 1.0                            # e/pix
    dict['efficiency_file'] = 'IFU_throughput.dat'

    out_file = open(snpp_refdata + "csst/ifs/config.json", "w")
    json.dump(dict, out_file, indent=2)
    out_file.close()

    return dict


def build_default_source():

    dict = {}
    dict['id'] = 1
    dict['geometry'] = {'type': 'flat', 'x_offset': 0.0, 'y_offset': 0.0, 'PA': 45.0,
                        'Re_major': 3., 'Re_minor': 1.5, 'sersic_n': 1,
                        'xwidth': 2., 'ywidth': 2.}
    dict['spectrum'] = {'name': 'SFgal_texp_FeH0_tau5_Ew10_AGN1.fits', 'redshift': 0.0, 'lines':[]}
    dict['normalization'] = {'value': 17.7, 'unit':'mag/arcsec^2', 'band': 'SDSS-g'}

    out_file = open(snpp_refdata + "source/config.json", "w")
    json.dump(dict, out_file, indent=2)
    out_file.close()

    return dict


def build_default_scene():

    scene = [build_default_source()]
    return scene


def build_default_calc():

    calc = {}
    calc['configuration'] = get_instrument_config()
    calc['scene'] = build_default_scene()
    calc['background'] = 'from_msc'
    calc['background_level'] = 'from_msc'
    calc['repn'] = 20.
    calc['obst'] = 300.

    calc['targetsnr'] = 10      # only be used in calculate_type = 'limitmag',
                                # in this case, normalization value is invalid


    return calc






