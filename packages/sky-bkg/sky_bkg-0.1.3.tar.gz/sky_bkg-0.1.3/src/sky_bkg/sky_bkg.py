from scipy.integrate import simps
import pandas as pd
import numpy as np
from datetime import datetime
import julian
from astropy.coordinates import get_sun
from astropy.time import Time
from astropy import units as u
from astropy.coordinates import SkyCoord
from scipy import interpolate
import os

path = os.path.abspath(os.path.dirname(__file__))


def earthshine(theta):
    """
        For given theta angle, return the earth-shine spectrum.

    :param theta: angle (in degree) from the target to earth limb.
    :return: the scaled solar spectrum
        template_wave: unit in A
        template_flux: unit in erg/s/cm^2/A/arcsec^2

    """

    # read solar template
    solar_template = pd.read_csv(path+'/refs/solar_spec.dat', sep='\s+',
                               header=None, comment='#')
    template_wave = solar_template[0].values
    template_flux = solar_template[1].values

    # read earth shine surface brightness
    earthshine_curve = pd.read_csv(path+'/refs/earthshine.dat',
                               header=None, comment='#')
    angle = earthshine_curve[0].values
    surface_brightness = earthshine_curve[1].values

    # read V-band throughtput
    cat_filter_V = pd.read_csv(path+'/refs/filter_Bessell_V.dat', sep='\s+',
                               header=None, comment='#')
    filter_wave = cat_filter_V[0].values
    filter_response = cat_filter_V[1].values

    # interplate to the target wavelength in V-band
    ind_filter = (template_wave >= np.min(filter_wave)) & (template_wave <= np.max(filter_wave))
    filter_wave_interp = template_wave[ind_filter]
    filter_response_interp = np.interp(filter_wave_interp, filter_wave, filter_response)

    filter_constant = simps(filter_response_interp * filter_wave_interp, filter_wave_interp)
    template_constant = simps(filter_response_interp * template_wave[ind_filter] * template_flux[ind_filter],
                              template_wave[ind_filter])
    dwave = filter_wave_interp[1:] - filter_wave_interp[:-1]
    wave_eff = np.nansum(dwave * filter_wave_interp[1:] * filter_response_interp[1:]) / \
               np.nansum(dwave * filter_response_interp[1:])

    # get the normalized value at theta.
    u0 = np.interp(theta, angle, surface_brightness)    # mag/arcsec^2
    u0 = 10**((u0 + 48.6)/(-2.5))         # target flux in erg/s/cm^2/Hz unit
    u0 = u0 * 3e18 / wave_eff**2          # erg/s/cm^2/A/arcsec^2

    factor = u0 * filter_constant / template_constant
    norm_flux = template_flux * factor          # erg/s/cm^2/A/arcsec^2

    return template_wave, norm_flux



def zodiacal(ra, dec, time):
    """
        For given RA, DEC and TIME, return the interpolated zodical spectrum in Leinert-1998.

    :param ra: RA in unit of degree, ICRS frame
    :param dec: DEC in unit of degree, ICRS frame
    :param time: the specified string that in ISO format i.e., yyyy-mm-dd.
    :return:
        wave_A: wavelength of the zodical spectrum
        spec_mjy: flux of the zodical spectrum, in unit of MJy/sr
        spec_erg: flux of the zodical spectrum, in unit of erg/s/cm^2/A/sr

    """

    # get solar position
    dt = datetime.fromisoformat(time)
    jd = julian.to_jd(dt, fmt='jd')
    t = Time(jd, format='jd', scale='utc')

    astro_sun = get_sun(t)
    ra_sun, dec_sun = astro_sun.gcrs.ra.deg, astro_sun.gcrs.dec.deg

    radec_sun = SkyCoord(ra=ra_sun*u.degree, dec=dec_sun*u.degree, frame='gcrs')
    lb_sun = radec_sun.transform_to('geocentrictrueecliptic')

    # get offsets between the target and sun.
    radec_obj = SkyCoord(ra=ra*u.degree, dec=dec*u.degree, frame='icrs')
    lb_obj = radec_obj.transform_to('geocentrictrueecliptic')

    beta = abs(lb_obj.lat.degree)
    lamda = abs(lb_obj.lon.degree - lb_sun.lon.degree)

    # interpolated zodical surface brightness at 0.5 um
    zodi = pd.read_csv(path+'/refs/zodi_map.dat', sep='\s+', header=None, comment='#')
    beta_angle = np.array([0, 5, 10, 15, 20, 25, 30, 45, 60, 75])
    lamda_angle = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45,
                          60, 75, 90, 105, 120, 135, 150, 165, 180])
    xx, yy = np.meshgrid(beta_angle, lamda_angle)
    f = interpolate.interp2d(xx, yy, zodi, kind='linear')
    zodi_obj = f(beta, lamda)       # 10^−8 W m−2 sr−1 um−1

    # read the zodical spectrum in the ecliptic
    cat_spec = pd.read_csv(path+'/refs/solar_spec.dat', sep='\s+', header=None, comment='#')
    wave = cat_spec[0].values       # A
    spec0 = cat_spec[1].values      # 10^-8 W m^−2 sr^−1 μm^−1
    zodi_norm = 252                 # 10^-8 W m^−2 sr^−1 μm^−1

    spec = spec0 * (zodi_obj / zodi_norm) * 1e-8  # W m^−2 sr^−1 μm^−1

    # convert to the commonly used unit of MJy/sr, erg/s/cm^2/A/sr
    wave_A = wave
    spec_mjy = spec * 0.1 * wave_A**2 / 3e18 * 1e23 * 1e-6      # MJy/sr
    spec_erg = spec * 0.1                                       # erg/s/cm^2/A/sr
    spec_erg2 = spec_erg / 4.25452e10                           # erg/s/cm^2/A/arcsec^2

    return wave_A, spec_erg2



    # Notes for unit convertion
    # ---------------------------------------
    # 1 W/m2/sr/μm = 0.10 erg/s/cm2/sr/A   (1 W = 1e7 erg/s, 1 um = 1e4 A)
    # 1 Jy = 10^-26 W/m^2/Hz = 10^-23 erg/s/cm^2/Hz
    # 1 MJy = 10^-17 erg/s/cm^2/Hz
    # 1 rad = 206265 arcsec
    # 1 sr = 1 rad^2 = 4.25452e10 arcsec^2
    # ----------------------------------------
