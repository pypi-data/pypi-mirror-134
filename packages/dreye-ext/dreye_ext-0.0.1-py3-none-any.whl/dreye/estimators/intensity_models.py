"""
"""

import numpy as np
from sklearn.utils.validation import check_array, check_is_fitted

from dreye.utilities import (
    optional_to, asarray
)
from dreye.constants import ureg
from dreye.estimators.base import _SpectraModel, _RelativeMixin
from dreye.utilities.abstract import inherit_docstrings
from dreye.estimators.utils import check_measured_spectra, get_bg_ints, get_ignore_bounds


@inherit_docstrings
class RelativeIntensityFit(_SpectraModel, _RelativeMixin):
    """
    Fit relative intensity values to a given LED system.

    Parameters
    ----------
    measured_spectra : dreye.MeasuredSpectraContainer
        Container with all available LEDs and their measured spectra. If
        None, a fake LED measurement will be created with intensities
        ranging from 0 to 100 microphotonflux.
    background : dreye.Signal, optional
        The spectral distribution of the background illuminant.
    measured_spectra : dreye.MeasuredSpectraContainer, optional
        Container with all available LEDs and their measured spectra. If
        None, a fake LED measurement will be created with intensities
        ranging from 0 to 100 microphotonflux.
    max_iter : int, optional
        The number of maximum iterations. This is passed directly to
        `scipy.optimize.lsq_linear` and `scipy.optimize.least_squares`.
    bg_ints : array-like, optional
        The intensity values for each LED, when the relative capture of each
        photoreceptor equals one (i.e. background intensity).
        This will prevent fitting of the
        LED intensities if the background LED intensities
        are preset and the relative capture is 1.
    fit_only_uniques : bool, optional
        If True, use `numpy.unique` to select only the unique samples
        for fitting before transforming X back to the full array.
    ignore_bounds : bool, optional
        If True, ignore the bounds of the LED intensities. Howerver, a zero
        LED intensity bound will always exist.
    lsq_kwargs : dict, optional
        Keyword arguments passed directly to `scipy.optimize.least_squares`.
    rtype : str {'fechner', 'log', 'weber', None}, optional
        Relative intensity measure to use:

        * `log` or `fechner` -  :math:`log(I/I_{bg})`
        * `weber` - :math:`(I-I_{bg})/I_{bg}`
        * `total_weber` - :math:`(I-I_{bg})/Sum(I_{bg})`
        * `diff` - :math:`(I-I_{bg})`
        * `absolute` - :math:`I`
        * `ratio` or `linear` - :math:`I/I_{bg}`


    Attributes
    ----------
    fitted_intensities_ : numpy.ndarray
        Intensities fit in units of `measured_spectra.intensities`.
    fitted_relative_intensities_ : numpy.ndarray
        Relative intensity values that were fit.
    """

    # other attributes that are the length of X but not X
    @property
    def _X_length(self):
        if self.rtype == 'absolute':
            return []
        return ['fitted_intensities_']

    def __init__(
        self,
        *,
        measured_spectra=None,  # dict, or MeasuredSpectraContainer
        bg_ints=None,  # array-like
        rtype='weber',  # {'fechner/log', 'weber', None}
        intensity_bounds=None, 
        wavelengths=None, 
        ignore_bounds=None
    ):
        self.measured_spectra = measured_spectra
        self.rtype = rtype
        self.bg_ints = bg_ints
        self.intensity_bounds = intensity_bounds
        self.wavelengths = wavelengths
        self.ignore_bounds = ignore_bounds

    def fit(self, X, y=None):
        #
        self.measured_spectra_ = check_measured_spectra(
            self.measured_spectra,
            asarray(X).shape[1],
            change_dimensionality=False, 
            wavelengths=self.wavelengths, 
            intensity_bounds=self.intensity_bounds
        )
        self.bg_ints_ = get_bg_ints(
            self.bg_ints, self.measured_spectra_,
            rtype=self.rtype
        )
        # check X
        X = self._check_X(X)
        self.relative_intensities_ = X

        # check that input shape is correct
        if X.shape[1] != len(self.measured_spectra_):
            raise ValueError("Shape of input is different from number"
                             "of measured spectra in container.")

        ignore_bounds = get_ignore_bounds(
            self.ignore_bounds, self.measured_spectra, self.intensity_bounds
        )
        if ignore_bounds:
            self.fitted_intensities_ = self._to_absolute_intensity(X)
        else:
            self.fitted_intensities_ = np.clip(
                self._to_absolute_intensity(X),
                *self.measured_spectra_.intensity_bounds
            )
        self.fitted_relative_intensities_ = self._to_relative_intensity(
            self.fitted_intensities_
        )

        return self

    def inverse_transform(self, X):
        # check is fitted
        check_is_fitted(self, ['n_features_', 'measured_spectra_'])

        # check X
        X = optional_to(X, self.output_units)
        X = check_array(X)

        # map output values to intensities
        return self._to_relative_intensity(
            self.measured_spectra_.inverse_map(X, return_units=False)
        )

    @property
    def input_units(self):
        if self.rtype in ['absolute', 'diff']:
            return self.measured_spectra_.intensities.units
        return ureg(None).units

    @property
    def fitted_X_(self):
        return self.fitted_relative_intensities_

    @property
    def X_(self):
        return self.relative_intensities_