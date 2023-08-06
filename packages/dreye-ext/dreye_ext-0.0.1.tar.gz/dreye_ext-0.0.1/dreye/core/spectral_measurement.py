"""Class to define spectral measurement
"""

import numpy as np
from scipy.interpolate import interp1d
from sklearn.isotonic import IsotonicRegression

from dreye.utilities import (
    is_numeric,
    optional_to, is_listlike, has_units,
    get_units, get_value
)
from dreye.utilities.abstract import inherit_docstrings
from dreye.constants import ureg, CONTEXTS
from dreye.core.signal import Signals, Signal, DomainSignal
from dreye.core.spectrum_mixin import (
    _SpectrumMixin, 
    _IntensityDomainSpectrumMixin
)
from dreye.core.signal_container import DomainSignalContainer
from dreye.err import DreyeError


@inherit_docstrings
class CalibrationSpectrum(_SpectrumMixin, Signal):
    """
    Defines a calibration measurement.

    Parameters
    ----------
    values : array-like, str, signal-type
        One-dimensional array that contains the values of the
        calibration measurement across wavelengths.
    domain/wavelengths : `dreye.Domain` or array-like, optional
        The wavelength domain of the signal.
        This needs to be the same length as `values`.
    units : str or `pint.Unit`, optional
        Units of the `values` array. Defaults to microjoule.
    area : numeric or `pint.Quantity`, optional
        The area of the spectrophotometer used for collecting photons. If
        the units cannot be obtained, then it is assumed to be in units of
        :math:`cm^2`.
    domain_units : str or `pint.Unit`, optional
        Units of the `domain` array.
    domain_min : numeric, optional
        Defines the minimum value in your domain for the intpolation range.
    domain_max : numeric, optional
        Defines the minimum value in your domain for the intpolation range.
    attrs : dict, optoinal
        User-defined dictionary of objects that are associated with the
        signal, but that are not used for any particular computations.
    name : str, optional
        Name of the signal instance.

    See Also
    --------
    Signal
    Spectrum
    IntensitySpectrum
    """

    def __init__(
        self,
        values,
        domain=None,
        *,
        area=None,
        units=None,
        **kwargs
    ):

        if area is None and not isinstance(values, CalibrationSpectrum):
            # assume area of 1 cm ** 2
            area = 1
        if units is None and not has_units(values):
            units = ureg('microjoule').units

        super().__init__(
            values=values, domain=domain, units=units,
            **kwargs
        )

        if area is None:
            area = self.attrs.get('area_', None)
        if not is_numeric(area):
            raise DreyeError("'area' argument must be a numeric value, "
                             f"but is of type '{type(area)}'.")

        if has_units(area):
            self.attrs['area_'] = area
        else:
            self.attrs['area_'] = area * ureg('cm ** 2')

    @property
    def area(self):
        return self.attrs['area_']


@inherit_docstrings
class MeasuredSpectrum(_IntensityDomainSpectrumMixin, DomainSignal):
    """
    Two-dimensional intensity signal of LED measurements
    with wavelength domain and output labels.

    Parameters
    ----------
    values : array-like, str, signal-type
        Two-dimensional array that contains the value of your signal.
    domain/wavelengths : `dreye.Domain` or array-like, optional
        The wavelength domain of the signal.
        This needs to be the same length as `values`.
    labels : `dreye.Domain` or array-like, optional
        The domain of the signal along the other axis.
        This needs to be the same length of
        the `values` array along the axis of the labels. The labels
        domain is assumed to be the output of the LED system.
        This can be volts or seconds in the case of pulse-width
        modulation.
    zero_intensity_bound : numeric, optional
        The output in labels units that correspond to zero intensity
        of the LED.
    max_intensity_bound : numeric, optional
        The output in labels units that correspond to maximum
        intensity that can be achieved.
    resolution : array-like, optional
        Array of individual steps that can be resolved by the hardware.
    units : str or `pint.Unit`, optional
        Units of the `values` array. Units must be convertible to
        photonflux or irradiance.
    domain_units : str or `pint.Unit`, optional
        Units of the `domain` array. Units are assumed to be nanometers.
    labels_units : str or `pint.Unit`, optional
        Units of the `labels` array.
    domain_axis : int, optional
        The axis that corresponds to the `domain` argument. Defaults to 0.
    domain_min : numeric, optional
        Defines the minimum value in your domain for the intpolation range.
    domain_max : numeric, optional
        Defines the minimum value in your domain for the intpolation range.
    attrs : dict, optoinal
        User-defined dictionary of objects that are associated with the
        signal, but that are not used for any particular computations.
    name : str, optional
        Name of the signal instance.

    See Also
    --------
    DomainSignal
    """

    inverse_map_method = 'isotonic'

    def __init__(
        self, values, domain=None, labels=None, *,
        zero_intensity_bound=None,
        max_intensity_bound=None,
        resolution=None,
        **kwargs
    ):

        super().__init__(values=values, domain=domain, labels=labels, **kwargs)

        # getting correct values and converting units
        if zero_intensity_bound is None:
            zero_intensity_bound = self.attrs.get(
                'zero_intensity_bound_', None)
        if max_intensity_bound is None:
            max_intensity_bound = self.attrs.get(
                'max_intensity_bound_', None)
        if resolution is None:
            resolution = self.attrs.get('resolution_', None)

        self.attrs['zero_intensity_bound_'] = self._get_domain_bound(
            zero_intensity_bound, self.labels
        )
        self.attrs['max_intensity_bound_'] = self._get_domain_bound(
            max_intensity_bound, self.labels
        )
        # should be the minimum step that can be taken - or an array?
        if is_listlike(resolution):
            self.attrs['resolution_'] = optional_to(
                resolution, self.labels.units
            ) * self.labels.units
        elif resolution is None:
            self.attrs['resolution_'] = None
        else:
            raise DreyeError("resolution must be list-like or None")

        self._intensity = None
        self._normalized_spectrum = None
        self._mapper = None
        self._inverse_mapper = None

        if self.name is None:
            idx = np.argmax(self.normalized_spectrum.magnitude)
            peak = self.domain.magnitude[idx]
            self.name = f"peak_at_{int(peak)}"

    @property
    def zero_is_lower(self):
        """
        Ascending or descending intensity values.

        This is inferred automatically.
        """
        if (
            np.isnan(self.zero_intensity_bound.magnitude)
            or np.isnan(self.max_intensity_bound.magnitude)
        ):
            # integral across wavelengths
            intensity = self.intensity.magnitude
            argsort = np.argsort(self.output.magnitude)
            return intensity[argsort][0] < intensity[argsort][-1]
        else:
            return (
                self.zero_intensity_bound.magnitude
                < self.max_intensity_bound.magnitude
            )

    @property
    def resolution(self):
        """
        Smallest possible label/output value differences.

        Includes units
        """
        if self.attrs['resolution_'] is None:
            return
        return self.attrs['resolution_'].to(self.labels.units, *CONTEXTS)

    @property
    def zero_intensity_bound(self):
        """
        Label value corresponding to zero intensity across wavelengths.

        Includes units.
        """
        return self.attrs['zero_intensity_bound_'].to(self.labels.units, *CONTEXTS)

    @property
    def max_intensity_bound(self):
        """
        Label/output value corresponding to max intensity across wavelengths.

        Includes units.
        """
        return self.attrs['max_intensity_bound_'].to(self.labels.units, *CONTEXTS)

    @property
    def output_bounds(self):
        """
        Bounds of output, e.g. 0 and 5 volts.

        Does not include units.
        """

        output_bounds = list(self.output.boundaries)

        idx_zero = 1 - int(self.zero_is_lower)
        if not np.isnan(self.zero_intensity_bound.magnitude):
            output_bounds[idx_zero] = self.zero_intensity_bound.magnitude
        if not np.isnan(self.max_intensity_bound.magnitude):
            output_bounds[idx_zero - 1] = self.max_intensity_bound.magnitude

        return tuple(output_bounds)

    @property
    def output(self):
        """
        Alias for labels unless resolution is not None.

        If resolution is not None, label values will be mapped to closest
        resolution value.
        """
        if self.resolution is None:
            return self.labels
        return self.labels._class_new_instance(
            self._resolution_mapping(self.labels.magnitude),
            units=self.labels.units,
            **self.labels._init_kwargs
        )

    @property
    def intensity_bounds(self):
        """
        Bounds of intensity signal after wavelength integration.

        Does not include units.
        """

        integral = self.intensity.magnitude

        if not np.isnan(self.zero_intensity_bound.magnitude):
            lower = 0.0
            upper = np.max(integral)
        else:
            lower = np.max([np.min(integral), 0.0])
            upper = np.max(integral)

        return (lower, upper)

    @property
    def normalized_spectrum(self):
        """
        Spectrum normalized to integrate to one.

        Will take mean across intensities to remove noise.
        Returns a spectra instance.
        """

        if self._normalized_spectrum is None:
            values = self.mean(axis=self.labels_axis)
            units, values = get_units(values), get_value(values)
            # threshold to zero
            values[values < 0] = 0
            # create spectrum
            spectrum = Signal(
                values=values,
                domain=self.domain,
                name=self.name,
                units=units,
                attrs=self.attrs,
            )
            self._normalized_spectrum = spectrum.normalized_signal

        return self._normalized_spectrum

    @property
    def intensity(self):
        """
        The intensity of each measurement.

        This takes the integral across the wavelength domain and
        returns a `Signal` instance with the output domain.
        """

        if self._intensity is None:
            # calculate integral and make sure it's above zero
            integral = self.integral
            mag, units = integral.magnitude, integral.units
            mag[mag < 0] = 0.0
            self._intensity = Signal(
                mag,
                units=units,
                domain=self.output,
                name=self.name,
                attrs=self.attrs,
            )
        return self._intensity

    def to_measured_spectra(self, units='uE'):
        """
        Convert to MeasuredSpectraContainer
        """
        return MeasuredSpectraContainer([self], units=units)

    def _resolution_mapping(self, values):
        """
        Map output values to given resolution.

        Parameters
        ----------
        values : np.ndarray or float
            Array that should already be in units of `labels.units`.
        """

        if self.resolution is None:
            return values

        numeric_type = is_numeric(values)
        new_values = np.atleast_1d(values)

        res_idx = np.argmin(
            np.abs(
                new_values[:, None]
                - self.resolution.magnitude[None, :]
            ),
            axis=1
        )

        new_values = self.resolution.magnitude[res_idx]
        if numeric_type:
            return np.squeeze(new_values)
        return new_values

    def ints_to_spectra(
        self, values,
        return_signal=True,
        return_units=True,
        **kwargs
    ):
        """
        Map Intensity values to a completely interpolated spectrum

        Parameters
        ----------
        values : array-like
            samples in intensity-convertible units or no units.
        return_signal : bool
            Whether to return a `Signal` instance.

        Returns
        -------
        output : signal-type, `numpy.ndarray`, or `pint.Quantity`
            Mapped output values.
        """
        labels = values
        values = optional_to(values, self.intensity.units)
        values = self.interpolator(
            self.intensity.magnitude,  # x
            self.magnitude,  # y
            **{**self.labels_interpolator_kwargs, **kwargs},
        )(values)
        if return_signal and return_units:
            if is_numeric(labels):
                values = Signal(
                    values,
                    units=self.units,
                    domain=self.domain,
                    name=labels,
                )
            else:
                values = Signals(
                    values,
                    units=self.units,
                    domain=self.domain,
                    labels=labels,
                )
            return values
        elif return_units:
            return values * self.units
        else:
            return values

    def map(self, values, return_units=True, check_bounds=True):
        """
        Map Intensity values to output values.

        Parameters
        ----------
        values : array-like
            samples in intensity-convertible units or no units.
        return_units : bool
            Whether to return mapped values with units.

        Returns
        -------
        output : `numpy.ndarray` or `pint.Quantity`
            Mapped output values.
        """

        values = optional_to(values, self.intensity.units)

        if is_numeric(values):
            shape = None
        elif values.ndim > 1:
            shape = values.shape
            values = values.flatten()
        else:
            shape = None

        # check intensity bound of values
        if check_bounds:
            imin, imax = self.intensity_bounds
            truth = np.all(values >= imin) and np.all(values <= imax)
            assert truth, 'Some values to be mapped are out of bounds.'

        mapped_values = self.mapper(values)
        mapped_values = self._resolution_mapping(mapped_values)

        if shape is not None:
            mapped_values = mapped_values.reshape(shape)

        if return_units:
            return mapped_values * self.labels.units

        return mapped_values

    def inverse_map(self, values, return_units=True):
        """
        Go from output values to intensity values

        Parameters
        ----------
        values : array-like
            samples in output-convertible units or no units.
        return_units : bool
            Whether to return mapped values with units.

        Returns
        -------
        output : `numpy.ndarray` or `pint.Quantity`
            Mapped intensity values.
        """
        # this is going to be two dimensional, since it is a Signals instance
        values = optional_to(values, self.labels.units)

        if is_numeric(values):
            shape = values.shape
            values = [values]
        elif values.ndim > 1:
            shape = values.shape
            values = values.flatten()
        else:
            shape = None

        values = self._resolution_mapping(values)
        intensity = self.inverse_mapper(values)

        if shape is not None:
            intensity = intensity.reshape(shape)

        if return_units:
            return intensity * self.intensity.units
        else:
            return intensity

    def get_residuals(self, values, return_units=True, check_bounds=True):
        """
        Get residuals between values and mapped values

        Parameters
        ----------
        values : array-like
            samples in intensity-convertible units or no units.
        return_units : bool
            Whether to return mapped values with units.

        Returns
        -------
        output : `numpy.ndarray` or `pint.Quantity`
            Mapped residual intensity values.
        """

        values = optional_to(values, units=self.intensity.units)
        mapped_values = self.map(
            values, return_units=False, check_bounds=check_bounds
        )

        # interpolate to new values given resolution
        res = self.inverse_map(mapped_values, return_units=False) - values

        if return_units:
            return res * self.intensity.units
        else:
            return res

    def score(self, values, check_bounds=True):
        """
        R^2 score for particular mapping.

        Parameters
        ----------
        values : array-like
            samples in intensity-convertible units or no units.
        return_units : bool
            Whether to return mapped values with units.

        Returns
        -------
        r2 : float
            R^2-score.
        """
        values = optional_to(values, self.intensity.units)
        mapped_values = self.map(
            values, return_units=False, check_bounds=check_bounds
        )
        fit_values = self.inverse_map(mapped_values, return_units=False)
        res = (values - fit_values) ** 2
        tot = (values - values.mean()) ** 2
        return 1 - res.sum() / tot.sum()

    @property
    def mapper(self):
        """
        Mapper for intensity values to output values.
        """
        if self._mapper is None:
            self._assign_mapper()
        return self._mapper

    @property
    def inverse_mapper(self):
        """
        Mapper for output values to intensity values.
        """
        if self._inverse_mapper is None:
            self._assign_mapper()
        return self._inverse_mapper

    def _assign_mapper(self):
        # 1D signal
        y = self.intensity.magnitude  # integral across intensities
        x = self.output.magnitude
        # sort x, y (not necessary)
        argsort = np.argsort(x)
        x = x[argsort]
        y = y[argsort]
        zero_intensity_bound = self.zero_intensity_bound.magnitude

        # a little redundant but should ensure safety of method
        if self.zero_is_lower and zero_intensity_bound < np.min(x):
            x = np.concatenate([[zero_intensity_bound], x])
            y = np.concatenate([[0], y])
        # a little redundant but should ensure safety of method
        elif not self.zero_is_lower and zero_intensity_bound > np.max(x):
            x = np.concatenate([x, [zero_intensity_bound]])
            y = np.concatenate([y, [0]])

        # get new_y and set inverse_mapper
        self._inverse_mapper = self._get_inverse_mapper(x, y)
        new_y = self._inverse_mapper(x)
        # set mapper
        self._mapper = self._get_mapper(new_y, x)

    def _get_inverse_mapper(self, x, y):
        """
        get mapping from outputs to intensity
        """
        # x are volts and y are intensities
        # perform isotonic regression
        if self.inverse_map_method == 'isotonic':
            isoreg = IsotonicRegression(
                # lower and upper intensity values
                y_min=self.intensity_bounds[0],
                y_max=self.intensity_bounds[1],
                increasing=self.zero_is_lower
            )
            isoreg.fit(x, y)
            new_y = isoreg.transform(x)
        elif self.inverse_map_method == 'spline':
            from pygam import s, LinearGAM
            constraints = (
                'monotonic_inc' if self.zero_is_lower else 'monotonic_dec'
            )
            model = LinearGAM(
                s(
                    0,
                    n_splines=min(len(x), 10),
                    spline_order=1,
                    lam=0.1,
                    constraints=constraints
                ),
                max_iter=1000
            )
            model.fit(x, y)
            new_y = model.predict(x)
        elif self.inverse_map_method == 'gamma':
            from scipy.optimize import curve_fit
            xdata = (x - x.min()) / (x.max() - x.min())
            if not self.zero_is_lower:
                xdata = 1 - xdata
            ydata = (y - y.min()) / (y.max() - y.min())

            def func(xdata, gamma):
                return xdata ** gamma

            popt, _ = curve_fit(func, xdata, ydata, p0=[1], bounds=[0.2, 5])

            new_y = func(xdata, *popt) * (y.max() - y.min()) + y.min()
        else:
            raise NameError(
                f"inverse_map_method `{self.inverse_map_method}` "
                "not recognized."
            )

        if self.zero_is_lower:
            interp = interp1d(
                x, new_y,
                bounds_error=False,
                fill_value=self.intensity_bounds
            )
        else:
            interp = interp1d(
                x, new_y,
                bounds_error=False,
                fill_value=self.intensity_bounds[::-1]
            )

        return interp

    def _get_mapper(self, new_y, x):
        """
        get mapping from intensity to outputs
        """
        if self.zero_is_lower:
            interp = interp1d(
                new_y, x,
                bounds_error=False,
                fill_value=self.output_bounds
            )

        else:
            interp = interp1d(
                new_y, x,
                bounds_error=False,
                fill_value=self.output_bounds[::-1]
            )

        def mapper(*args, **kwargs):
            return np.clip(
                interp(*args, **kwargs),
                a_min=self.output_bounds[0],
                a_max=self.output_bounds[1]
            )
        return mapper


@inherit_docstrings
class MeasuredSpectraContainer(DomainSignalContainer):
    """
    A container that can hold multiple `dreye.MeasuredSpectrum` instances.

    The `map` methods are also accessible in the container.

    Parameters
    ----------
    container : list-like
        A list of `dreye.DomainSignal` instances.
    units : str or `ureg.Unit`, optional
        The units to convert the values to. If None,
        it will choose the units of the first signal in the list.
    domain_units : str or `ureg.Unit`, optional
        The units to convert the domain to. If None,
        it will choose the units of domain of the first signal in the list.
    labels_units : str or `ureg.Unit`, optional
        The units to convert the labels to. If None,
        it will choose the units of labels of the first signal in the list.

    See Also
    --------
    DomainSignalContainer
    """

    _xlabel = r'$\lambda$ (nm)'
    _cmap = 'viridis'
    _init_keys = [
        '_intensities',
        '_normalized_spectra',
        '_mapper'
    ] + DomainSignalContainer._init_keys
    _allowed_instances = MeasuredSpectrum

    def ints_to_spectra(
        self, values, return_signal=True,
        return_units=True, **kwargs
    ):
        """
        Map Intensity values to a completely interpolated and summed spectra.

        Parameters
        ----------
        values : array-like
            samples in intensity-convertible units or no units.
        return_signal : bool
            Whether to return a `Signal` instance.

        Returns
        -------
        output : signal-type, `numpy.ndarray`, or `pint.Quantity`
            Mapped output values.
        """

        values = optional_to(values, units=self.intensities.units)
        # assert values.ndim < 3, 'values must be 1 or 2 dimensional'
        spectra = None
        for idx, measured_spectrum in enumerate(self):
            spectrum = measured_spectrum.ints_to_spectra(
                values[..., idx],
                return_signal=return_signal,
                return_units=return_units,
                **kwargs
            )
            if spectra is None:
                spectra = spectrum
            else:
                spectra += spectrum

        return spectra

    def map(self, values, return_units=True, check_bounds=True):
        """
        Map Intensity values to output values.

        Parameters
        ----------
        values : array-like (..., n_leds)
            2D samples in intensity-convertible units or no units.
        return_units : bool
            Whether to return mapped values with units.

        Returns
        -------
        output : `numpy.ndarray` or `pint.Quantity`
            Mapped output values.
        """

        values = optional_to(values, units=self.intensities.units)
        # assert values.ndim < 3, 'values must be 1 or 2 dimensional'
        x = np.atleast_2d(values)

        y = np.empty(x.shape)
        for idx, measured_spectrum in enumerate(self):
            y[..., idx] = measured_spectrum.map(
                x[..., idx], return_units=False, check_bounds=check_bounds
            )

        if values.ndim == 1:
            y = y[0]

        if return_units:
            return y * self.labels_units

        return y

    def inverse_map(self, values, return_units=True):
        """
        Go from output values to intensity values

        Parameters
        ----------
        values : array-like (..., n_leds)
            2D samples in output-convertible units or no units.
        return_units : bool
            Whether to return mapped values with units.

        Returns
        -------
        output : `numpy.ndarray` or `pint.Quantity`
            Mapped intensity values.
        """
        values = optional_to(values, units=self.labels_units)
        # assert values.ndim < 3, 'values must be 1 or 2 dimensional'
        x = np.atleast_2d(values)

        y = np.empty(x.shape)
        for idx, measured_spectrum in enumerate(self):
            y[..., idx] = measured_spectrum.inverse_map(
                x[..., idx], return_units=False
            )

        if values.ndim == 1:
            y = y[0]

        if return_units:
            return y * self.intensities.units

        return y

    def get_residuals(self, values, return_units=True, check_bounds=True):
        """
        Get residuals between values and mapped values

        Parameters
        ----------
        values : array-like (..., n_leds)
            2D samples in intensity-convertible units or no units.
        return_units : bool
            Whether to return mapped values with units.

        Returns
        -------
        output : `numpy.ndarray` or `pint.Quantity`
            Mapped residual intensity values.
        """

        values = optional_to(values, units=self.intensities.units)
        # assert values.ndim < 3, 'values must be 1 or 2 dimensional'
        x = np.atleast_2d(values)

        y = np.empty(x.shape)
        for idx, measured_spectrum in enumerate(self):
            y[..., idx] = measured_spectrum.get_residuals(
                x[..., idx], return_units=False, check_bounds=check_bounds
            )

        if values.ndim == 1:
            y = y[0]

        if return_units:
            return y * self.intensities.units

        return y

    def score(self, values, average=True, check_bounds=True):
        """
        R^2 score for particular mapping.

        Parameters
        ----------
        values : array-like
            2D samples in intensity-convertible units or no units.
        return_units : bool
            Whether to return mapped values with units.

        Returns
        -------
        r2 : float
            R^2-score.
        """
        values = optional_to(values, units=self.intensities.units)
        # assert values.ndim < 3, 'values must be 1 or 2 dimensional'
        x = np.atleast_2d(values)

        scores = np.array([
            measured_spectrum.score(x[..., idx], check_bounds=check_bounds)
            for idx, measured_spectrum in enumerate(self)
        ])

        if average:
            return np.mean(scores)

        return scores

    @property
    def resolution(self):
        """
        Resolution of devices
        """
        resolutions = self.__getattr__('resolution')
        nones = ([r is None for r in resolutions])
        if all(nones):
            return
        else:
            return resolutions

    @property
    def zero_is_lower(self):
        """
        Whether zero intensity output value is lower than the max intensity
        output value.
        """
        return np.array(self.__getattr__('zero_is_lower'))

    @property
    def zero_intensity_bound(self):
        """
        Boundary of output corresponding to zero intensity spectrum

        Contains output units.
        """
        return np.array([
            ele.magnitude
            for ele in self.__getattr__('zero_intensity_bound')
        ]) * self.labels_units

    @property
    def max_intensity_bound(self):
        """
        Boundary of output corresponding to maximum intensity spectrum.

        Contains output units.
        """
        return np.array([
            ele.magnitude
            for ele in self.__getattr__('max_intensity_bound')
        ]) * self.labels_units

    @property
    def intensity_bounds(self):
        """
        Intensity bounds for the Measured Spectra in two-tuple array form.

        Unit removed.
        """
        value = [ele.intensity_bounds for ele in self]
        return tuple(np.array(value).T)

    @property
    def output_bounds(self):
        """
        Output bounds for Measured Spectra in two-tuple array form.

        Unit removed
        """
        value = [ele.output_bounds for ele in self]
        return tuple(np.array(value).T)

    @property
    def normalized_spectra(self):
        """
        Normalized spectra for each LED measurement.

        Returns a `dreye.Spectra` instance in units of `1/nm`.

        See Also
        --------
        dreye.MeasuredSpectrum.normalized_spectrum
        """
        if self._normalized_spectra is None:
            for idx, ele in enumerate(self):
                if idx == 0:
                    spectra = Signals(ele.normalized_spectrum)
                else:
                    spectra = spectra.labels_concat(
                        Signals(ele.normalized_spectrum)
                    )

            self._normalized_spectra = spectra
        return self._normalized_spectra

    @property
    def intensities(self):
        """
        Intensities for each LED measurement across outputs.

        Returns a `dreye.Signals` instance in units of integrated
        intensity.

        See Also
        --------
        dreye.MeasuredSpectrum.intensity
        """
        if self._intensities is None:
            for idx, ele in enumerate(self):
                if idx == 0:
                    intensities = Signals(ele.intensity)
                else:
                    intensities = intensities.labels_concat(
                        Signals(ele.intensity)
                    )

            self._intensities = intensities
        return self._intensities

    @property
    def wavelengths(self):
        return self.normalized_spectra.domain

    @property
    def _ylabel(self):
        return self[0]._ylabel
