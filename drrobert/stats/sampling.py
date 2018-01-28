import numpy as np

def log_uniform(low, high):

    power = np.random.uniform(low=low, high=high)
    factor = np.random.uniform(high=10)

    return factor * 10**power
