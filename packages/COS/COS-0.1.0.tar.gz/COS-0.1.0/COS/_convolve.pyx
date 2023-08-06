""" Routine to convolve a model flux array with the wavelength-dependent,
non-gaussian COS LSF. Currently only supports the G130M, G160M and G230L
gratings. Defaults to a Gaussian LSF corresponding to the resolution of
HST/FOS for NUV wavelengths, unless otherwise specified.

"""

from __future__ import division, print_function

from .utils import read_lsf

import numpy as np
cimport numpy as nc

cdef extern from "math.h":
    double exp(double)

cdef double gaussian(double x, double sigma):
    return exp(-0.5 * (x / sigma) ** 2)

cimport cython

@cython.boundscheck(False)
def convolve_with_COS_FOS(
        nc.ndarray[nc.float64_t] a,
        nc.ndarray[nc.float64_t] wavelength,
        use_cos_nuv=False,
        cos_nuv_only=False):
    """ Convolves array `a` at wavelengths `wavelength` with either the COS LSF
    or a gaussian LSF for FOS, depending on the wavelength.

    Parameters
    ----------
    a : array of floats, shape (N,)
        Array to be convolved.

    wavelength : array of floats, shape (N,)
        Wavelength at each point.

    use_cos_nuv : bool
        If True, use the COS NUV line spread function instead of
        convolving with FOS resolution (default = False).

    cos_nuv_only : bool
        If True, use only the COS NUV line spread function. For
        use when there is no COS FUV data (default = False).

    Returns
    -------
    results : array of floats with shape (N,)
        Convolved array.

    """

    cdef int i, m, n, imax, N, n_g130m, n_g160m, n_nuv
    cdef double result, wtot, wval, sigma, wup, dw
    cdef nc.ndarray[nc.float64_t] lsf, results = np.empty_like(a)

    ind = wavelength.searchsorted(1795)
    dw = np.median(np.diff(wavelength[:ind]))
    N = len(a)
    n = 0

    if not cos_nuv_only:
        print('COS FUV pixel width {0:.4f} Angstrom'.format(dw))

        profile = read_lsf('G130M', dw)
        keys = 'w1150 w1200 w1250 w1300 w1350 w1400 w1450'.split()
        g130m = [np.array(profile.lsf[k]) for k in keys]

        profile = read_lsf('G160M', dw)
        keys = 'w1450 w1500 w1550 w1600 w1650 w1700 w1750'.split()
        g160m = [np.array(profile.lsf[k]) for k in keys]

        g130uplim = [1175, 1225, 1275, 1325, 1375, 1425, 1450]
        g160uplim = [1475, 1525, 1575, 1625, 1675, 1725, 1795]

        n_g130m = len(g130m[0])
        n_g160m = len(g160m[0])

        # G130M:
        for k in range(len(g130m)):
            lsf = g130m[k]
            wup = g130uplim[k]

            while n < N and wavelength[n] < wup:
                result = 0
                wtot = 0

                for m in range(-(n_g130m // 2), n_g130m // 2 + 1):
                    i = n + m
                    if i < 0 or i >= N:
                        continue
                    wval = lsf[m + n_g130m // 2]
                    result += wval * a[i]
                    wtot += wval

                results[n] = result / wtot
                n += 1

        # G160M:
        for k in range(len(g160m)):
            lsf = g160m[k]
            wup = g160uplim[k]

            while n < N and wavelength[n] < wup:
                result = 0
                wtot = 0

                for m in range(-(n_g160m // 2), n_g160m // 2 + 1):
                    i = n + m
                    if i < 0 or i >= N:
                        continue
                    wval = lsf[m + n_g160m // 2]
                    result += wval * a[i]
                    wtot += wval

                results[n] = result / wtot
                n += 1

    # COS NUV:
    if use_cos_nuv and N - n > 5:

        dw = np.median(np.diff(wavelength[n:]))

        print('COS NUV pixel width {0:.4f} Angstrom\n'
              '(from {1:.6f} Angstrom)'.format(dw, wavelength[n]))

        profile = read_lsf('NUV', dw)

        keys = 'w1700 w1800 w1900 w2000 w2100 w2200 w2300 w2400 w2500 w2600 \
        w2700 w2800 w2900 w3000 w3100 w3200'.split()

        nuv = [np.array(profile.lsf[k]) for k in keys]
        nuv_uplim = [1750.5, 1850.5, 1950.5, 2050.5, 2150.5, 2250.5, 2350.5,
                     2450.5, 2550.5, 2650.5, 2750.5, 2850.5, 2950.5, 3050.5,
                     3150.5, 3200.5]

        n_nuv = len(nuv[0])

        for k in range(len(nuv)):
            lsf = nuv[k]
            wup = nuv_uplim[k]

            while n < N and wavelength[n] < wup:
                result = 0
                wtot = 0

                for m in range(-(n_nuv // 2), n_nuv // 2 + 1):
                    i = n + m
                    if i < 0 or i >= N:
                        continue
                    wval = lsf[m + n_nuv // 2]
                    result += wval * a[i]
                    wtot += wval

                results[n] = result / wtot
                n += 1
    else:

        # Use FOS resolution:
        while n < N and wavelength[n] < 2300:

            dw = wavelength[n] - wavelength[n-1]
            sigma = 1.39 / 2.35

            # Determine how far away we need to go from the Gaussian centre:
            imax = int(5 * sigma / dw)

            result = 0
            wtot = 0

            for m in range(-imax, imax + 1):
                i = n + m
                if i < 0 or i >= N:
                    continue
                wval = gaussian(-m * dw, sigma)
                result += wval * a[i]
                wtot += wval

            results[n] = result / wtot
            n += 1

        while n < N and wavelength[n] < 3300:

            sigma = 1.97 / 2.35

            # Determine how far away we need to go from the Gaussian centre:
            imax = int(5 * sigma / dw)

            result = 0
            wtot = 0

            for m in range(-imax, imax + 1):
                i = n + m
                if i < 0 or i >= N:
                    continue
                wval = gaussian(-m * dw, sigma)
                result += wval * a[i]
                wtot += wval

            results[n] = result / wtot
            n += 1

    return results
