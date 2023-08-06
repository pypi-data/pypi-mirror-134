"""
Model for LED substitution
"""

import warnings

import numpy as np
import pandas as pd
from scipy.optimize import least_squares

from dreye.estimators.base import _RelativeMixin
from dreye.estimators.excitation_models import IndependentExcitationFit
from dreye.utilities.abstract import inherit_docstrings
from dreye.utilities import asarray

EPS = 1e-5
EPS1 = 1e-3
EPS2 = 1e-2
# TODO docstrings


@inherit_docstrings
class LedSubstitutionFit(IndependentExcitationFit, _RelativeMixin):
    """
    Led Substitution estimator.
    """

    def __init__(
        self,
        *,
        photoreceptor_model=None,  # dict or Photoreceptor class
        fit_weights=None,
        background=None,  # dict or Spectrum instance or array-like
        measured_spectra=None,  # dict, or MeasuredSpectraContainer
        max_iter=None,
        bg_ints=None,
        ignore_bounds=None,
        lsq_kwargs=None,
        background_external=None,
        rtype='weber',  # {'fechner/log', 'weber', None}
        unidirectional=False,  # allow only increase or decreases of LEDs in simulation
        keep_proportions=False,
        keep_intensity=True, 
        intensity_bounds=None,
        wavelengths=None, 
        capture_noise_level=None
    ):
        super().__init__(
            photoreceptor_model=photoreceptor_model,
            measured_spectra=measured_spectra,
            background=background,
            max_iter=max_iter,
            fit_weights=fit_weights,
            unidirectional=unidirectional,
            lsq_kwargs=lsq_kwargs,
            ignore_bounds=ignore_bounds,
            bg_ints=bg_ints,
            background_external=background_external, 
            wavelengths=wavelengths, 
            intensity_bounds=intensity_bounds, 
            capture_noise_level=capture_noise_level
        )
        self.rtype = rtype
        self.keep_proportions = keep_proportions
        self.keep_intensity = keep_intensity

    def fit(self, X, y=None):
        """
        LED substitution experiment.

        Parameters
        ----------
        X : numpy.ndarray
            Two-dimensional array with two columns. The first column contains
            the indices of the LED to simulate and the second column contains
            the intensity for the LED to reach and simulate.
            TODO: if NaN, skip those entries and substitute with the background
            intensity.
        """

        # set required objects
        self._set_required_objects(None)

        X = asarray(X)
        assert (X.shape[1] % 2) == 0

        if X.shape[1] == 2:
            led_idcs = X[:, 0].astype(int)  # every second one
            led_bounds = X[:, 1]  # every second one starting at 1
        else:
            # TODO simulate combinations of LEDs
            raise NotImplementedError("Combinations of LED steps")
            # led_idcs = X[:, 0::2].astype(int)  # every second one
            # led_bounds = X[:, 1::2]  # every second one starting at 1

        led_bgs = self.bg_ints_[led_idcs]
        if self.rtype in {'fechner', 'weber', 'log', 'total_weber', 'diff'}:
            led_simulate_maxs = led_bounds > 0
        elif self.rtype in {'ratio', 'linear'}:
            led_simulate_maxs = led_bounds > 1
        elif self.rtype == 'absolute':
            led_simulate_maxs = led_bounds > led_bgs
        else:
            raise ValueError(f"rtype `{self.rtype}` not recognized.")

        led_abs_bounds = self._to_absolute_intensity(
            led_bounds, led_bgs
        )

        fitted_intensities = []
        fitted_info = []

        already_fitted = {}

        for led_idx, led_bound, led_simulate_max in zip(
            led_idcs, led_abs_bounds, led_simulate_maxs
        ):
            w_solo = self._get_w_solo(led_idx, led_bound)
            if np.any(w_solo > self.intensity_bounds_[1]):
                warnings.warn(
                    "Absolute intensity goes beyond measurment bounds! - "
                    "Change target intensity values."
                )
            # keep proportions or not
            if (
                self.keep_proportions
                and (led_idx in already_fitted)
            ):
                old_w, old_w_solo = already_fitted[led_idx]

                old_rel_w = self._to_relative_intensity(
                    old_w,
                    self.bg_ints_,
                )
                old_rel_solo = self._to_relative_intensity(
                    old_w_solo[led_idx],
                    self.bg_ints_[led_idx],
                )
                new_rel_solo = self._to_relative_intensity(
                    w_solo[led_idx],
                    self.bg_ints_[led_idx],
                )

                factor = np.sum(new_rel_solo / old_rel_solo)
                new_rel_w = factor * old_rel_w

                w = self._to_absolute_intensity(
                    new_rel_w,
                    self.bg_ints_,
                )

                if np.any(w > self.intensity_bounds_[1]):
                    warnings.warn(
                        "Proportions go beyond measurement bounds! - "
                        "Turn off `keep_proportions` to avoid this error or "
                        "switch the order of the first sample fitted to be "
                        "the maximum intensity."
                    )
            else:
                w, w_solo = self._fit_sample(
                    w_solo,
                    led_idx,
                    led_bound,
                    led_simulate_max,
                )

                already_fitted[led_idx] = (w, w_solo)

            new_relative_int = self._to_relative_intensity(
                w_solo[led_idx],
                self.bg_ints_[led_idx],
            )

            fitted_intensities.append(w)
            fitted_intensities.append(w_solo)

            fitted_info.append({
                'led': self.measured_spectra_.names[led_idx],
                'simulate': True,
                'rel_led_int': new_relative_int,
                'rtype': self.rtype
            })
            fitted_info.append({
                'led': self.measured_spectra_.names[led_idx],
                'simulate': False,
                'rel_led_int': new_relative_int,
                'rtype': self.rtype
            })

        fitted_intensities = np.array(fitted_intensities)
        fitted_excitations = np.array([
            self.get_excitation(w)
            for w in fitted_intensities
        ])

        # pass
        self.fitted_intensities_ = fitted_intensities[::2]
        self.fitted_solo_intensities_ = fitted_intensities[1::2]
        self.fitted_relative_intensities_ = self._to_relative_intensity(
            self.fitted_intensities_
        )
        self.fitted_solo_relative_intensities_ = self._to_relative_intensity(
            self.fitted_solo_intensities_
        )
        self.fitted_excite_X_ = fitted_excitations[::2]
        self.fitted_solo_excite_X_ = fitted_excitations[1::2]

        self.fitted_capture_X_ = self.photoreceptor_model_.inv_excitefunc(
            self.fitted_excite_X_
        )
        self.fitted_solo_capture_X_ = self.photoreceptor_model_.inv_excitefunc(
            self.fitted_solo_excite_X_
        )

        index = pd.MultiIndex.from_frame(pd.DataFrame(fitted_info))
        fitted_excitations = pd.DataFrame(
            fitted_excitations,
            index=index,
            columns=[f"fitted_{rh}" for rh in self.photoreceptor_model_.labels]
        ).reset_index()
        self.fitted_excitations_df_ = fitted_excitations

        fitted_intensities = pd.DataFrame(
            fitted_intensities,
            index=pd.MultiIndex.from_frame(fitted_excitations),
            columns=self.measured_spectra_.names
        )
        self.fitted_intensities_df_ = fitted_intensities
        return self

    def _fit_sample(
        self,
        w_solo,
        led_idx,
        led_bound,
        led_simulate_max,
    ):
        # adjust A matrix
        target_capture_x = self.get_capture(w_solo)

        # check if simulating max and adjust bounds
        if led_simulate_max:
            # TODO add noise from capture noise level
            assert np.all(target_capture_x >= self.capture_border_ - EPS), (
                str(target_capture_x)
            )
            # adjust lower bound to be the led intensity of interest
            if self._unidirectional_:
                min_bound = self.bg_ints_.copy()
            else:
                min_bound = self.intensity_bounds_[0].copy()
            min_bound[led_idx] = led_bound
            max_bound = self.intensity_bounds_[1].copy()
            if self.keep_intensity:
                max_bound[led_idx] = led_bound + EPS2
            bounds_ = (
                min_bound, max_bound
            )
        else:
            assert np.all(target_capture_x <= self.capture_border_ + EPS), (
                str(target_capture_x)
            )
            # adjust upper bound to be the led intensity of interest
            if self._unidirectional_:
                max_bound = self.bg_ints_.copy()
            else:
                max_bound = self.intensity_bounds_[1].copy()
            max_bound[led_idx] = led_bound
            min_bound = self.intensity_bounds_[0].copy()
            if self.keep_intensity:
                min_bound[led_idx] = led_bound - EPS2
            bounds_ = (
                min_bound, max_bound
            )

        # bounds for the LED not simulated and the other LEDs during simulation
        if self._unidirectional_ and led_simulate_max:
            min_bound = self.bg_ints_.copy()
            max_bound = self.intensity_bounds_[1].copy()
        elif self._unidirectional_:
            min_bound = self.intensity_bounds_[0].copy()
            max_bound = self.bg_ints_.copy()
        else:
            min_bound = self.intensity_bounds_[0].copy()
            max_bound = self.intensity_bounds_[1].copy()
        min_bound[led_idx] = self.bg_ints_[led_idx]
        max_bound[led_idx] = self.bg_ints_[led_idx] + EPS
        bounds_without = (
            min_bound, max_bound
        )

        # try to simulate the lower bound of the LED simulation
        w0 = self._init_sample(
            target_capture_x,
            bounds_without,
        ).copy()
        if led_simulate_max:
            w0[led_idx] = led_bound + EPS1
        else:
            w0[led_idx] = led_bound - EPS1

        # simulatenously fit the upper and lower bound
        result = least_squares(
            self._objective,
            x0=w0,
            args=(led_idx,),
            bounds=bounds_,
            max_nfev=self.max_iter,
            **({} if self.lsq_kwargs is None else self.lsq_kwargs)
        )
        w = result.x.copy()
        w[led_idx] = self.bg_ints_[led_idx]
        w_solo = self.bg_ints_.copy()
        w_solo[led_idx] = result.x[led_idx]

        return w, w_solo

    def _get_w_solo(self, led_idx, led_bound):
        w_solo = self.bg_ints_.copy()
        w_solo[led_idx] = led_bound
        return w_solo

    def _objective(
        self,
        w, led_idx
    ):
        w_solo = self.bg_ints_.copy()
        w_solo[led_idx] = w[led_idx]
        w = w.copy()
        w[led_idx] = self.bg_ints_[led_idx]
        x_pred = self.get_excitation(w)
        excite_x = self.get_excitation(w_solo)
        return self.fit_weights_ * (excite_x - x_pred)

    @property
    def X_(self):
        return self.fitted_solo_excite_X_
