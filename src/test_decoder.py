import decoder
import numpy as np
import pytest


def decodesCorrectly():
    data = decoder.decodeAFM('/home/private/repos/afm-reader/sample/sample.nid')
    assert len(data) == 32

def testOptimistic():
    decoded = {
        "Spec": {
            "Backward": {
                "Sample_Bias": [[1,2,3]],
                "2nd Lock-In Amplitude": [[6,5,4]]
            },
            "Forward": {
                "Sample_Bias": [[4,5,6]],
                "2nd Lock-In Amplitude": [[3,2,1]]
            }
        }
    }
    dataConfig = {
      "x": [('Spec', 'Backward', 'Sample_Bias'), ('Spec', 'Forward', 'Sample_Bias')],
      "amplitude": [('Spec', 'Backward', '2nd Lock-In Amplitude'), ('Spec', 'Forward', '2nd Lock-In Amplitude')],
    }
    result = decoder.getDataFromDecoded(decoded, dataConfig)
    assert np.array_equal(result["x"], np.array([[1,2,3,4,5,6]]))
    assert np.array_equal(result["amplitude"], np.array([[6,5,4,3,2,1]]))

def testPessimistic():
    decoded = {}
    dataConfig = {
      "x": [('Spec', 'Backward', 'Sample_Bias'), ('Spec', 'Forward', 'Sample_Bias')],
    }

    with pytest.raises(Exception) as exception:
        decoder.getDataFromDecoded(decoded, dataConfig)
    assert str(exception.value) == '!!! Config error !!!' 





