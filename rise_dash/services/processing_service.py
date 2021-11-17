import numpy as np


def min_max_normalisation(array: np.ndarray) -> np.ndarray:
    array_min = array.min()
    array_max = array.max()
    return (array - array_min) / (array_max - array_min)
