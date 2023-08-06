## Helper module in popmodel containing constants and functions for
## OH calculations.
## Adam Birdsall

## Literature cited:

# Bradshaw et al, Appl Opt, 23, 2134 (1984)
# Daily et al., Applied Optics 16 (3), 568-571 (1977)
# Fuchs et al., Atmos Meas Tech, 1611-1626(2012)
# Schlosser et al., J Atmos Chem, 56, 187-205 (2007)
# Tsuji et al, Bull Chem Soc Jpn, 73, 2695-2702 (2000)
# van de Meerakker et al, Phys Rev Lett, 95, 013003 (2005)

import atmcalcs as atm

import math as m
import numpy as np
from scipy.constants import k as kb
from scipy.constants import c, N_A, pi, h
import scipy.special

#######################

def kqavg(kn2,ko2,kh2o,xh2o=0.02):
    '''get average k in air (default 0.78 N2/0.20 O2/0.02 H2O)'''
    xn2=0.79-xh2o/2
    xo2=0.21-xh2o/2
    return xn2*kn2+xo2*ko2+xh2o*kh2o

#######################

### Literature values for OH
mass = 17.01/(N_A)*1000    # kg

nu12 = 3407.53 * atm.wavenum_to_Hz  # Hz, IR transition used in Tsuji et al,
# 2000. Illustrative example; popmodel extracts precise wavenumber for given IR
#       transition from HITRAN.

## Degeneracies
# Generally, degeneracies for rotational quantum number J are 2J+1. The ground
# electronic state is PI, so lambda doubling doubles the degeneracies. A-state
# is SIGMA, so there is no lambda doubling.

# Example values for 3-level system where IR transition is P branch and UV is
# Q branch:
ga = 20    # (J = 4.5)
gb = 16    # (J = 3.5)
gc = 8    # From (2*J + 1) and N = 3 (?) for Tsuji et al. feature. Assuming
            # Q branch.

## Einstein coefficients
# Aba is very slow and unimportant for popmodel calculations. Acb and Aca are
# used by popmodel as values independent of line selected.
Aba = 16.9      # Einstein coefficient for spontaneous emission, s^-1;
                # using van de Meerakker et al, 2005
                # alt value: 14.176 s^-1 from Tsuji et al, 2000

Acb = 5300 #for A2Sigma+(v'=0)-->X2Pi(v"=1) Copeland (1987). Really, we'd 
# want the A's for each rotational transition...

Aca = 1.45e6 #s-1, for A2Sigma+(v'=0)-->X2Pi(v"=0), German (1975)
# No c<--a laser, so B coefficients not applicable.

## Rotational relaxation
# Define in terms of depopulation rate of rotational level of interest. Model
# also needs to include repopulation rate such that thermal distribution is
# reached at equilibrium.
rrout = np.array([7.72e-10,7.72e-10, 4.65e-10])
# Smith and Crosley, 1990 model rates. Undifferentiated by quencher or v.

## Lambda doublet relaxation
lrout = 4.5e-10 # ballpark placeholder

## Thermal rotational distribution
# Use LIFBASE-calculated thermal distributions at 296 K for both halves of each
# lambda doublet -- can later divide in half to calculate population in each
# half of lambda doublet (equal e and f).
# X(v"=0) rotational levels
# F1 term (PI_3/2) where J = N + 0.5 (starts with N=1)
rotfrac_a1 = np.array([[0.1147102,
                      0.1373055,
                      0.1333955,
                      0.1108903,
                      0.0807381,
                      0.0521280,
                      0.0300671,
                      0.0155687]])
# F2 term (PI_1/2) where J = N - 0.5 (starts with N=1)
rotfrac_a2 = np.array([[0.0303408,
                       0.0520817,
                       0.0605903,
                       0.0566615,
                       0.0449620,
                       0.0310304,
                       0.0188811,
                       0.0102155]])
# X(v"=1) rotational levels
# F1 term
rotfrac_b1 = np.array([[0.1118301,
                       0.1346591,
                       0.1319314,
                       0.1108789,
                       0.0818258,
                       0.0536861,
                       0.0315495,
                       0.0166880]])
# F2 term
rotfrac_b2 = np.array([[0.0295226,
                       0.0509050,
                       0.0596629,
                       0.0563731,
                       0.0453257,
                       0.0317841,
                       0.0197044,
                       0.0108914]])
# to avoid digging into mess of calculating populations for A_SIGMA just assume
# distribution is more or less like X(v"=0). Tenuous connection to reality.
rotfrac_c = rotfrac_a1+rotfrac_a2
# build rotfrac dict for extraction in main.py
rotfrac = {}
rotfrac['a'] = np.concatenate((rotfrac_a1,rotfrac_a2))
rotfrac['b'] = np.concatenate((rotfrac_b1,rotfrac_b2))
rotfrac['c'] = rotfrac_c[0]

## HITRAN data for 3407 cm^-1 IR transition
# v = 0 --> v = 1, J = 4.5 --> J = 3.5
# loadHITRAN automates extracting these values from arbitrary IR OH line

g_air = .053    # air-broadened HWHM, cm^-1 atm^-1 at 296K

g_self = .03    # self-broadened HWHM, cm^-1 atm^-1 at 296K

n_air = .66    # coeff of temp dependence of air-broadened half-width

# uncertainties in HITRAN data for this transition:
# in wavenumber: 3 ('0.001 - 0.01')
# in intensity: 4 ('10-20%')
# in g-air: 2 ('avg or estimate')
# in g-self: 0 ('unreported')
# in n_air: 1 ('default')
# in air-pressure shift: 0 ('unreported') -- value given as 0

### Laser operating parameters
# No longer call these particular values in popmodel KineticsRun calcs. Do use
# spec_intensity function, though.
temp = 296.    # temperature, K. All HITRAN data assumes 296K!

beam_diam_IR = 5e-3    # beam diameter, m

beam_diam_UV = 5e-3    # beam diameter, m

bandwidth_IR = 1e6    # Hz, Aculight spec
bandwidth_UV = 7e9    # Hz, Schlosser et al 2007.

power_IR = 3    # W, Aculight spec
power_UV = 50e-3    # W, Schlosser et al 2007, average power

reprate_UV = 8.5e3    # Hz, Fuchs et al. 2012
period_UV = 1/reprate_UV    # s
pulsewidth_UV = 30e-9    #s, somewhat arbitrary, Fuchs et al. report 25 ns pulse
peak_power_UV = power_UV * period_UV/pulsewidth_UV # W, peak power

# Beam parameters
A_IR = pi*(.5*beam_diam_IR)**2 # beam area, m^2
A_UV = pi*(.5*beam_diam_UV)**2

# Spectral radiances (intensities) for master equations, W/m^2*sr*Hz
# Note IR is CW laser, while UV is pulsed.
def spec_intensity(power,area,bandwidth):
    return power/(area*bandwidth)

Lab = spec_intensity(power_IR,A_IR,bandwidth_IR)
Lbc = spec_intensity(peak_power_UV,A_UV,bandwidth_UV)

op_press = 2.    # operating pressure of detection cell, torr
                # Julich LIF instrument operates at 
                # 3.5 hPa = 2.6 torr (Fuchs et al.)
                # 8.5 hPa = 6.4 torr (Schlosser et al.)
xoh = 0.5e-12 # 0.5 pptv, ballpark (1.2E7 cm^-3 at 760 torr, 296 K)

# Quenching:
xh2o = 0.02    # mole fraction of water
Q = atm.press_to_numdens(op_press, temp) # total 'quencher' conc, molec/cm^3

# Quenching speciated by N2/O2/H2O: (s^-1/(molec cm^-3))
# Full result of lit search in 'vib excited lifetime calcs OH TP LIF.xlsx'.
# Define estimated rate constants based on these values.
kqbh2o=1.36e-11    # Reported value for multiple groups, +/-0.4e-11; however, Silvente et al. give value 50% larger
kqbo2=1e-13    # Choose intermediate value between reported measurements of 7.5e-14 and 1.3e13
kqbn2=1.5e-15    # Only one reported measurement (D'Ottone et al.), but this term is a minor contribution
kqb = kqavg(kqbn2,kqbo2,kqbh2o,xh2o)

quenchb = kqb * Q # s^-1

# Electronic quenching of A state (s^-1/(molec cm^-3))
kqch2o = 68.0e-11 # Wysong et al. 1990, v'=0
kqco2 = 13.5e-11 # Wysong et al. 1990, v'=0
kqcn2 = 1.9e-11 # Copeland et al. 1985, v'=0, N'=3 (other N available -- gets smaller with bigger N)
kqc = kqavg(kqcn2,kqco2,kqch2o,xh2o)

quenchc = kqc * Q # s^-1

###############################

## Functions for calculations

# N.B. Two conventions for Einstein B coefficient:
# (1) Spectral radiance (intensity) 
# Spectral intensity L is laser power per (area, solid angle and frequency)
# L: J m^-2 s^-1 Hz^-1 sr^-1 = W m^-2 Hz^-1 sr^-1
#     units of B: m^2 J^-1 s^-1 = s kg^-1
# (2) Energy density rho: J m^-3 Hz^-1 sr^-1 = W s m^-3 Hz^-1 sr^-1
#     units of B: m^3 J^-1 s^-2 = m kg^-1
# We're using (1), intensity convention, e.g., Daily et al., 1977.
# L and rho are related by L = c*rho (see McQuarrie Ch. 15).
# L and rho are also per solid angle, or sr^-1 -- see Wikipedia.

def b21(a21, freq):
    '''
    Calculate Einstein coefficient for stimulated emission from A
    coefficient, using McQuarrie Eqn 15.13 and dividing by c to
    convert to intensity convention, m^2 J^-1 s^-1.

    Also consistent with Demtroder 3rd ed, assuming typo in eqn. 2.22.
    (i.e., missing nu^3 in numerator, h is to first power)
    Provides result consistent with Frank's value of 1e8 for OH
    excitation to v' = 1 from email 16 May 2014.

    Parameters
    ----------
    a21 : float (or 1D numpy array)
    Einstein A coefficient for spontaneous emission, s^-1.
    freq : float (or 1D numpy array)
    Frequency of transition, Hz.

    Returns
    -------
    b21 : float (or 1D numpy array)
    Einstein B coefficient for stimulated emission, m^2 J^-1 s^-1.
    '''
    b21 = a21 * c**2 / (8. * m.pi * h * freq**3)
    return b21

def b12(a21, g1, g2, freq):
    '''
    Calculate Einstein coefficient for absorption from A coefficient.

    Parameters
    ----------
    a21: float (or 1D numpy array)
    Einstein A coefficient for spontaneous emission, s^-1.
    g1, g2: float (or 1D numpy array)
    Degeneracies of lower and upper states. Function converts g's to float
    to avoid high likelihood of int division.
    freq : float (or 1D numpy array)
    Frequency of transition, Hz.

    Returns
    -------
    b12 : float (or 1D numpy array)
    Einstein B coefficient for absorption, m^2 J^-1 s^-1.
    '''
    b12 = np.array(g1).astype(float)/np.array(g2).astype(float) * b21(a21, freq)
    return b12

def fwhm_doppler(nu, temp, mass):
    '''
    Calculates FWHM, Hz, of peak from Doppler broadening.

    Source: Demtroder 3rd ed., p 70 (Eqn 3.43a)
    '''
    fwhm = (2*m.pi*nu/c) * (8*kb*temp*m.log(2)/mass)**0.5
    return fwhm

def press_broaden(press=op_press):
    '''
    Uses HITRAN parameters to calculate HWHM, in MHz, at 'press'
    in torr. Default pressure of op_press
    '''
    hwhm = press * atm.torr_to_atm * (g_air) * atm.wavenum_to_Hz / 1e6
    return hwhm

def sat(bandwidth, beam, q=quenchb):
    '''
    Calculates power when saturation parameter is equal to 1,
    following Daily et al., 1977, i.e., when population of excited
    state is half that of ground state, scaled by degeneracies. Full
    saturation is when this parameter is >>1.

    Parameters
    ----------
    bandwidth : float
    Bandwidth of laser, MHz
    beam : float
    Beam diameter, mm
    q : float
    combined quenching and spontaneous emission rate (Q + A), s^-1.
    Default value is literature OH v"=1 --> v"=0 quench rate.

    Returns
    -------
    sat_power : float
    Power when saturation parameter is 1, W.
    '''
    
    sat_intensity = q / b21(a21)
    beam_area = m.pi * (0.5 * beam / 1.e3)**2
    sat_power = sat_intensity * beam_area * (bandwidth * 1.e6)
        # power is I * A * bandwidth

    return sat_power

def voigt(xarr,amp,xcen,sigma,gamma,normalized=False):
    """
    Normalized Voigt profile from pyspeckit, on Github.

    z = (x+i*gam)/(sig*sqrt(2))
    V(x,sig,gam) = Re(w(z))/(sig*sqrt(2*pi))

    The area of V in this definition is 1.
    If normalized=False, then you can divide the integral of V by
    sigma*sqrt(2*pi) to get the area.

    Original implementation converted from
    http://mail.scipy.org/pipermail/scipy-user/2011-January/028327.html
    (had an incorrect normalization and strange treatment of the input
    parameters)

    Modified implementation taken from wikipedia, using the definition.
    http://en.wikipedia.org/wiki/Voigt_profile

    Parameters
    ----------
    xarr : np.ndarray
    The X values over which to compute the Voigt profile
    amp : float
    Amplitude of the voigt profile
    if normalized = True, amp is the AREA
    xcen : float
    The X-offset of the profile
    sigma : float
    The width / sigma parameter of the Gaussian distribution -- standard
    deviation
    gamma : float
    The width / shape parameter of the Lorentzian distribution -- HWHM
    normalized : bool
    Determines whether "amp" refers to the area or the peak of the voigt
    profile

    Outputs
    -------
    V : np.ndarray
    Voigt profile y values for xarr, either normalized or not.
    """
    z = ((xarr-xcen) + 1j*gamma) / (sigma * np.sqrt(2))
    V = amp * np.real(scipy.special.wofz(z))
    if normalized:
        return V / (sigma*np.sqrt(2*np.pi))
    else:
        return V

################################

## Executes when running from within module

if __name__ == "__main__":
    print('ohcalcs is accessory, use main')
