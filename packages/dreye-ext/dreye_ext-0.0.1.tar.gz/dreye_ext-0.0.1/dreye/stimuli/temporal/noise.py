"""
Random noise stimuli

Noise with autocorrelations/convolution
Truncated distributions
White noise
Pink noise
Brown noise
"""

import pandas as pd
import numpy as np
import scipy.signal

from dreye.stimuli.base import BaseStimulus, DUR_KEY, DELAY_KEY, PAUSE_KEY
from dreye.utilities import Filter1D
from dreye.utilities.abstract import inherit_docstrings
from dreye.stimuli.mixin import SetTruncGaussianValues


@inherit_docstrings
class AbstractNoiseStimulus(BaseStimulus):
    """Abstract class for noise stimulus that implements convolution/filtering
    of noise signals.

    Parameters
    ----------
    filter_style : {'filtfilt', 'window', 'complete'}
        Filter styles. 'filtfilt' will use filter function to get a and
        b for the filtfilt function (x is the signal). 'window' will
        use dreye.utilities.Filter1D. 'complete' will pass the signal as the
        first argument to filter function, and return the complete filtered
        signal.
    filter_function : str
        Filtering function to use. Either creates filter design for
        filtfilt or window, or it is a finished filtering method.
        If filter_function is a string, must be a method in scipy.signal.
        For filter_style window, filter_function must be in
        scipy.signal.windows (also see dreye.utilities.Filter1D).
    filter_along_axis : int
        apply filtering process along axis. Default is None.
    filter_kwargs : dict
        Arguments passed to the filter function.
    extra_kwargs : dict
        Arguments passed to call of scipy.signal.filtfilt or
        dreye.utilities.Filter1D.
    """

    _add_mean_to_events = False

    def __init__(
        self,
        *,
        filter_style=None,
        filter_function=None,
        filter_kwargs=None,
        filter_along_axis=0,
        extra_kwargs=None,
        **kwargs
    ):

        super().__init__(
            filter_style=filter_style,
            filter_function=filter_function,
            filter_kwargs=filter_kwargs,
            filter_along_axis=filter_along_axis,
            extra_kwargs=extra_kwargs,
            **kwargs
        )

        if self.filter_kwargs is None:
            self.filter_kwargs = {}

        if self.extra_kwargs is None:
            self.extra_kwargs = {}

    @staticmethod
    def apply_filter(
        signal, filter_function, filter_style,
        filter_kwargs, extra_kwargs
    ):
        """
        Apply filter to signal according to filter function and style.
        """

        if filter_style is None or filter_function is None:
            return signal

        if filter_style == 'complete':
            # if filter_function is string get function from scipy.signal
            if isinstance(filter_function, str):
                filter_function = getattr(scipy.signal, filter_function)
            return filter_function(signal, **filter_kwargs, **extra_kwargs)

        elif filter_style == 'filtfilt':
            # if filter_function is string get function from scipy.signal
            if isinstance(filter_function, str):
                filter_function = getattr(scipy.signal, filter_function)
            b, a = filter_function(**filter_kwargs)
            return scipy.signal.filtfilt(b, a, signal, **extra_kwargs)

        elif filter_style == 'window':
            return Filter1D(filter_function, **filter_kwargs)(
                signal, **extra_kwargs
            )

        else:
            raise NameError(f'filter style {filter_style} is unknown')

    def filter_signal(self, signal):
        """
        Filter signal.
        """

        if self.filter_along_axis is None:
            return self.apply_filter(
                signal, self.filter_function,
                self.filter_style,
                self.filter_kwargs,
                self.extra_kwargs
            )
        else:
            return np.apply_along_axis(
                self.apply_filter,
                self.filter_along_axis,
                signal,
                self.filter_function,
                self.filter_style,
                self.filter_kwargs,
                self.extra_kwargs
            )


@inherit_docstrings
class WhiteNoiseStimulus(AbstractNoiseStimulus, SetTruncGaussianValues):
    """
    White noise stimulus with truncated Gaussian.

    Parameters
    ----------
    estimator : scikit-learn type estimator
        Estimator that implements the `fit_transform` method.
    stim_dur : float
        duration of stimulus
    mean : float or array-like
        mean values for each channel.
    var : float or array-like
        variance for each channel.
    minimum : float
        minimum value
    maximum : float
        maximum value
    iterations : int
        How often to iterate over the whole stimulus. Does not rerandomize
        order for each iteration.
    start_delay : float
        Duration before step stimulus starts (inverse units of rate)
    end_dur : float
        Duration after step stimulus ended (inverse units of rate)
    seed : int
        seed for randomization.
    rate : float
        frame rate / rate of change.
    n_channels : int
        Number of channels.
    channel_names : list-like
        Name of each channel.
    filter_style : {'filtfilt', 'window', 'complete'}
        Filter styles. 'filtfilt' will use filter function to get a and
        b for the filtfilt function (x is the signal). 'window' will
        use dreye.utilities.Filter1D. 'complete' will pass the signal as the
        first argument to filter function, and return the complete filtered
        signal.
    filter_function : str
        Filtering function to use. Either creates filter design for
        filtfilt or window, or it is a finished filtering method.
        If filter_function is a string, must be a method in scipy.signal.
        For filter_style window, filter_function must be in
        scipy.signal.windows (also see dreye.utilities.Filter1D).
    filter_along_axis : int
        apply filtering process along axis. Default is None.
    filter_kwargs : dict
        Arguments passed to the filter function.
    extra_kwargs : dict
        Arguments passed to call of scipy.signal.filtfilt or
        dreye.utilities.Filter1D.
    """

    def __init__(
        self,
        *,
        estimator=None,
        subsample=None,
        rate=1,
        n_channels=None,
        stim_dur=10,
        mean=0,
        var=1,
        minimum=None,
        maximum=None,
        iterations=1,
        start_delay=0,
        end_dur=0,
        pause_dur=0,
        seed=None,
        channel_names=None,
        filter_style=None,
        filter_function=None,
        filter_kwargs=None,
        filter_along_axis=0,
        extra_kwargs=None,
    ):

        super().__init__(
            estimator=estimator,
            rate=rate,
            subsample=subsample,
            stim_dur=stim_dur,
            mean=mean,
            var=var,
            minimum=minimum,
            maximum=maximum,
            iterations=iterations,
            start_delay=start_delay,
            end_dur=end_dur,
            pause_dur=pause_dur,
            seed=seed,
            n_channels=n_channels,
            filter_style=filter_style,
            filter_function=filter_function,
            filter_kwargs=filter_kwargs,
            filter_along_axis=filter_along_axis,
            channel_names=channel_names,
            extra_kwargs=extra_kwargs,
        )

        self._set_trunc_gaussian_values()

    @property
    def ch_names(self):
        return self.channel_names

    def create_random_signal(self):
        """
        Create a truncated white noise signal.
        """

        distribution = self._get_distribution()

        total_frames = int(self.rate * self.stim_dur)

        return distribution.rvs(
            size=(total_frames, self.n_channels),
            random_state=self.seed
        )

    def create_baseline(self, dur):
        """
        Create `numpy.ndarray` of length dur*rate
        with only the mean values.
        """

        frames = int(np.ceil(self.rate * dur))
        signal = np.ones((frames, self.n_channels))
        signal = signal * np.atleast_2d(self.mean)
        return signal

    def create(self):
        # pause signal
        pause_signal = self.create_baseline(self.pause_dur)
        stim_dur_signal = self.create_baseline(self.stim_dur)
        # create random signal and filter it
        random_signal = self.create_random_signal()
        # this will smooth over the transition
        random_signal = np.vstack(
            [stim_dur_signal, random_signal, stim_dur_signal]
        )
        random_signal = self.filter_signal(random_signal)
        random_signal = random_signal[
            len(stim_dur_signal):len(random_signal) - len(stim_dur_signal)
        ]

        # initialize metadata
        metadata = dict(
            random_signal=random_signal,
        )
        random_dur = len(random_signal) / self.rate

        # package random signal with pause
        start_signal = self.create_baseline(self.start_delay)
        signal = np.vstack([
            start_signal,
            random_signal,
        ])

        # initialize event dataframe
        events = [{
            DELAY_KEY: len(start_signal) / self.rate,
            DUR_KEY: random_dur,
            PAUSE_KEY: len(pause_signal) / self.rate,
            'iter': 0,
            'name': self.name
        }]

        for n in range(self.iterations - 1):
            events.append({
                DELAY_KEY: (len(signal) + len(pause_signal)) / self.rate,
                DUR_KEY: random_dur,
                PAUSE_KEY: len(pause_signal) / self.rate,
                'iter': n + 1,
                'name': self.name
            })

            signal = np.vstack([
                signal,
                pause_signal,
                random_signal
            ])

        events = pd.DataFrame(events)
        # add random signal for each channel
        for idx, channel in enumerate(self.channel_names):
            assert channel not in events.columns
            events[channel] = [random_signal[:, idx]] * len(events)

        signal = np.vstack([signal, self.create_baseline(self.end_dur)])

        self._signal = signal
        self._events = events
        self._metadata = metadata

        return self


@inherit_docstrings
class BrownNoiseStimulus(WhiteNoiseStimulus):
    """
    Brownian noise stimulus (cumulative white noise).

    Parameters
    ----------
    estimator : scikit-learn type estimator
        Estimator that implements the `fit_transform` method.
    stim_dur : float
        duration of stimulus
    mean : float or array-like
        mean values for each channel.
    var : float or array-like
        variance for each channel.
    minimum : float
        minimum value
    maximum : float
        maximum value
    iterations : int
        How often to iterate over the whole stimulus. Does not rerandomize
        order for each iteration.
    start_delay : float
        Duration before step stimulus starts (inverse units of rate)
    end_dur : float
        Duration after step stimulus ended (inverse units of rate)
    seed : int
        seed for randomization.
    rate : float
        frame rate / rate of change.
    n_channels : int
        Number of channels.
    channel_names : list-like
        Name of each channel.
    filter_style : {'filtfilt', 'window', 'complete'}
        Filter styles. 'filtfilt' will use filter function to get a and
        b for the filtfilt function (x is the signal). 'window' will
        use dreye.utilities.Filter1D. 'complete' will pass the signal as the
        first argument to filter function, and return the complete filtered
        signal.
    filter_function : str
        Filtering function to use. Either creates filter design for
        filtfilt or window, or it is a finished filtering method.
        If filter_function is a string, must be a method in scipy.signal.
        For filter_style window, filter_function must be in
        scipy.signal.windows (also see dreye.utilities.Filter1D).
    filter_along_axis : int
        apply filtering process along axis. Default is None.
    filter_kwargs : dict
        Arguments passed to the filter function.
    extra_kwargs : dict
        Arguments passed to call of scipy.signal.filtfilt or
        dreye.utilities.Filter1D.
    """

    def create_random_signal(self):
        """
        Create of truncated Brownian noise signal.
        """

        # using truncnorm from parent class
        signal = super().create_random_signal()

        # _broadcastable mean
        mean = np.atleast_2d(self.mean)

        # brownian part (removing mean drift)
        signal = np.cumsum(signal - mean, axis=0) + mean

        # fit max and min to shape of signal for _broadcasting
        max = np.atleast_2d(self.maximum)
        min = np.atleast_2d(self.minimum)

        # threshold to max and min
        signal = np.where(signal < max, signal, max)
        signal = np.where(signal > min, signal, min)

        return signal


# TODO Binary noise
