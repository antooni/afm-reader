import decoder
import numpy as np
import pytest
from pathlib import Path


def test_decoding():
    file_path = Path(__file__).resolve().parents[1].joinpath('sample/sample.nid')
    data = decoder.decode_afm(file_path)
    assert len(data) == 32  # type: ignore

def test_optimistic():
    decoded = {
        "Spec": {
            "Backward": {
                "Sample_Bias": [[1,2,3]],
            },
            "Forward": {
                "2nd Lock-In Amplitude": [[3,2,1]]
            }
        }
    }
    data_config = {
      "bias_backward": ['Spec', 'Backward', 'Sample_Bias'],
      "amplitude_forward": ['Spec', 'Forward', '2nd Lock-In Amplitude'],
    }
    result = decoder.get_data_from_decoded(decoded, data_config)
    assert np.array_equal(result["bias_backward"], np.array([[1,2,3]]))
    assert np.array_equal(result["amplitude_forward"], np.array([[3,2,1]]))

def test_pessimistic():
    decoded = {}
    data_config = {
      "x_forward": ['Spec', 'Forward', 'Sample_Bias'],
    }

    with pytest.raises(Exception) as exception:
        decoder.get_data_from_decoded(decoded, data_config)
    assert str(exception.value) == '!!! Config error !!!' 





