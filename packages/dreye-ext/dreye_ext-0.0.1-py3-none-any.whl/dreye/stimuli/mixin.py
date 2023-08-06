"""various mixin classes
"""

from itertools import product
import numpy as np
import pandas as pd
from scipy import stats

from dreye.utilities import is_numeric, asarray, convert_truncnorm_clip

# TODO handling baseline_values and set actual properties here


class SetTruncGaussianValues:

    def _set_trunc_gaussian_values(self):

        self.mean = asarray(self.mean)
        self.var = asarray(self.var)

        if self.n_channels is None and self.channel_names is None:
            self.n_channels = max([self.mean.size, self.var.size])
        elif self.n_channels is None:
            self.n_channels = len(self.channel_names)

        if self.channel_names is None:
            self.channel_names = list(range(self.n_channels))
        else:
            self.channel_names = list(self.channel_names)
            assert len(self.channel_names) == self.n_channels

        if self.minimum is None:
            self.minimum = self.mean - 5 * self.var
        else:
            self.minimum = asarray(self.minimum)
        if self.maximum is None:
            self.maximum = self.mean + 5 * self.var
        else:
            self.maximum = asarray(self.maximum)

        if np.all(self.maximum == self.minimum):
            self.maximum += 10**-5
            self.minimum -= 10**-5

        assert np.all(self.minimum < self.maximum)

    def _get_distribution(self):
        a, b = convert_truncnorm_clip(
            self.minimum, self.maximum, self.mean, self.var)

        distribution = stats.truncnorm(
            a=a,
            b=b,
            loc=self.mean,
            scale=self.var
        )
        return distribution


class SetBaselineMixin:

    # --- misc helper function --- #
    @staticmethod
    def _set_baseline_values(baseline_values, channel_names):
        """function for setting baseline values attribute to
        numpy array. Method is used in _set_values method.
        """

        # check if baseline_values are correct size
        if is_numeric(baseline_values):
            baseline_values = asarray(
                [baseline_values] * len(channel_names)
            )
        # TODO dict
        else:
            baseline_values = asarray(baseline_values)
            assert len(channel_names) == len(baseline_values)

        return baseline_values.astype(float)


class SetStepMixin:

    def _set_values(self, values, baseline_values, separate_channels):
        """function to set values attribute to pandas DataFrame.
        """

        index_for_df = None

        # convert values into pandas dataframe object
        if is_numeric(values):
            channel_names = asarray([0])
            baseline_values = self._set_baseline_values(
                baseline_values, channel_names)
            values = asarray([values]).astype(float)

        elif isinstance(values, dict):
            channel_names = asarray(list(values.keys()))
            baseline_values = self._set_baseline_values(
                baseline_values, channel_names)
            if separate_channels:
                _values = []
                for index, ele in enumerate(values.values()):
                    # ignore none elements and zero length elements
                    if ele is None or len(ele) == 0:
                        continue
                    __values = asarray(
                        [baseline_values] * len(ele)
                    ).astype(float)
                    __values[:, index] = asarray(ele).astype(float)
                    _values.extend(__values.tolist())
                values = _values
            else:
                values = list(product(*values.values()))

        elif not isinstance(values, pd.DataFrame):
            values = asarray(values)
            if values.ndim > 1:
                channel_names = np.arange(values.shape[1])
            else:
                channel_names = asarray([0])
            baseline_values = self._set_baseline_values(
                baseline_values, channel_names)

        else:
            channel_names = values.columns
            index_for_df = values.index
            baseline_values = self._set_baseline_values(
                baseline_values, channel_names)

        df_values = pd.DataFrame(
            asarray(values).astype(float), columns=channel_names,
            index=index_for_df
        )

        if any([name is None for name in df_values.index.names]):
            names = []
            for idx, name in enumerate(df_values.index.names):
                if name is None:
                    name = f"values_index_{idx}"
                names.append(name)
            df_values.index.names = names

        return df_values, baseline_values


class SetRandomStepMixin:

    def _set_values(self, values, baseline_values, values_probs):
        """return values in dictionary format and baseline_values as
        numpy.array
        """

        if isinstance(values, dict):
            if values_probs is None:
                values_probs = {}
            else:
                assert isinstance(values_probs, dict), \
                    'values probs must be dict'

            channel_names = asarray(list(values.values()))
            # transform each element into numpy array
            for key, ele in values.items():
                # ignore none elements and zero length elements
                if ele is None or len(ele) == 0:
                    continue
                # convert element to numpy array
                ele = asarray(ele)
                values[key] = ele

                # check values probs array
                if values_probs.get(key, None) is None:
                    values_probs[key] = np.ones(len(ele)) / len(ele)
                else:
                    values_prob = asarray(values_probs[key])
                    values_prob = values_prob / np.sum(values_prob)
                    assert len(values_prob) == len(ele), \
                        'values prob not same length as values.'
                    values_probs[key] = values_prob

        else:
            channel_names = asarray([0])

            values = asarray(values)
            assert values.ndim == 1, \
                'if array-like values must be one-dimensional'

            if values_probs is None:
                values_probs = np.ones(len(values)) / len(values)
            else:
                values_probs = asarray(values_probs) / np.sum(values_probs)
                assert len(values_probs) == len(values), \
                    'values prob not same length as values.'

            values = {channel_names[0]: values}
            values_probs = {channel_names[0]: values_probs}

        baseline_values = self._set_baseline_values(
            baseline_values, channel_names)

        return values, baseline_values, values_probs
