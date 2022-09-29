from config import Config

CONFIG = {
  "sourcePath": "path/to/source",
  "outputPath": "path/to/output",
  "data": {
    "bias": [
      ["Spec", "Backward", "Sample_Bias"],
      ["Spec", "Forward", "Sample_Bias"]
    ],
    "amplitude": [
      ["Spec", "Backward", "2nd Lock-In Amplitude"],
      ["Spec", "Forward", "2nd Lock-In Amplitude"]
    ]
  },
  "files": {
    "bias": {
      "data_name": "bias",
      "multiplier": "1",
      "transpose": "True"
    }
  },
  "plots": {
    "bias_amplitude": {
      "x_data": "bias",
      "x_unit": "-",
      "y_data": "amplitude",
      "y_unit": "pN"
    }
  }
}


def test_config():
    config = Config(CONFIG)

    assert config.source_path == "path/to/source"
    assert config.output_path == "path/to/output"

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
