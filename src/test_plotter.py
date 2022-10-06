from unittest import result
import numpy as np

from plotter import get_average, get_data


def test_get_data():
    data = {
        "bias_forward": np.array([[1,2],[3,4]]),
        "bias backward": np.array([[1,2],[3,4]])
    }

    labels = ["bias_forward","bias backward"]

    result = get_data(labels, data)

    assert np.array_equal(result, np.array([[1,2,2,1],[3,4,4,3]]))


def test_get_average():
    data = np.array([[1,2],[3,4]])
    result = get_average(data)

    assert np.array_equal(result, np.array([2, 3]))
