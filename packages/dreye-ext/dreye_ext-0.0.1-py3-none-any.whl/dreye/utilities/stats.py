"""various utility functions for handinglin distributions
"""


def convert_truncnorm_clip(a, b, loc, scale):
    """
    Convert `scipy.stats.truncnorm` clip values to standard form.
    """

    return (a - loc) / scale, (b - loc) / scale
