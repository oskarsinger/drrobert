import numpy as np

def log_uniform(low, high, factor=None):

    power = np.random.uniform(low=low, high=high)

    if factor is None:
        factor = np.random.uniform(low=1, high=10)

    return factor * 10**power
