This package contains code useful for analysis of far-UV spectra taken with
the Cosmic Origins Spectrograph (COS) on the Hubble Space Telescope. It
allows fast convolution of synthetic spectra with the non-gaussian COS line
spread function for the G130M, G160M and all near UV gratings. There are
utilities for generating a wavelength-dependent line spread function for use
with `VPFIT <http://www.ast.cam.ac.uk/~rfc/vpfit.html>`_, for reading and
writing CalCOS pipeline output, and for estimating the significance of
absorption features in reduced COS spectra. There is also a co-addition
routine for combining COS spectra from multiple settings, and a script for
running the CalCOS pipeline.

To install, download the tarball from the pypi website and then do::

    python setup.py install

This package can also be easily installed using pip::

    pip install COS

