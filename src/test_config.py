from config import Config, FileConfig
from pathlib import Path


def test_config():
    config_path = Path(__file__).resolve().parents[1].joinpath('sample/config.json')
    config = Config(config_path)

    assert config.source_path == "/home/private/repos/afm-reader/sample"
    assert config.output_path == "/home/private/repos/afm-reader/results"

    assert len(config.data.keys()) == 2
    assert config.data["bias"] == [
      ["Spec", "Backward", "Sample_Bias"],
      ["Spec", "Forward", "Sample_Bias"]
    ]
    assert config.data["amplitude"] == [
      ["Spec", "Backward", "2nd Lock-In Amplitude"],
      ["Spec", "Forward", "2nd Lock-In Amplitude"]
    ]

    assert len(config.files.keys()) == 1
    assert config.files["bias"].data_name == "bias"
    assert config.files["bias"].multiplier == 1
    assert config.files["bias"].transpose == True
    assert len(config.files["bias"].__dict__) == 3

    assert len(config.plots.keys()) == 1
    assert config.plots["bias_amplitude"].x_data == "bias"
    assert config.plots["bias_amplitude"].x_unit == "-"
    assert config.plots["bias_amplitude"].y_data == "amplitude"
    assert config.plots["bias_amplitude"].y_unit == "pN"
    assert len(config.plots["bias_amplitude"].__dict__) == 4
