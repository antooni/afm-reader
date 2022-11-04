from config import Config
import pytest
import copy

CONFIG = {
  "sourcePath": "path/to/source",
  "outputPath": "path/to/output",
  "data": {
    "bias": ["Spec", "Forward", "Sample_Bias"],
    "amplitude": ["Spec", "Forward", "2nd Lock-In Amplitude"],
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

    assert len(config.data_config.keys()) == 2
    assert config.data_config["bias"] == ["Spec", "Forward", "Sample_Bias"]
    assert config.data_config["amplitude"] == ["Spec", "Forward", "2nd Lock-In Amplitude"]
    

    assert len(config.files_config.keys()) == 1
    assert config.files_config["bias"].data_key == "bias"
    assert config.files_config["bias"].multiplier == 1
    assert config.files_config["bias"].transpose == True
    assert len(config.files_config["bias"].__dict__) == 3

    assert len(config.plots_config.keys()) == 1
    assert config.plots_config["bias_amplitude"].x_data == "bias"
    assert config.plots_config["bias_amplitude"].x_unit == "-"
    assert config.plots_config["bias_amplitude"].y_data == "amplitude"
    assert config.plots_config["bias_amplitude"].y_unit == "pN"
    assert len(config.plots_config["bias_amplitude"].__dict__) == 4

    

def test_error_handling():
    with pytest.raises(NameError, match='!!! Config error !!! / files'):
        wrong_file_data_name = copy.deepcopy(CONFIG)
        wrong_file_data_name["files"]["bias"]["data_name"] = "non-existing-data"
        Config(wrong_file_data_name)

    with pytest.raises(NameError, match='!!! Config error !!! / plot x_data'):
        wrong_plot_x_data = copy.deepcopy(CONFIG)
        wrong_plot_x_data["plots"]["bias_amplitude"]["x_data"] = "non-existing-data"
        Config(wrong_plot_x_data)

    with pytest.raises(NameError, match='!!! Config error !!! / plot y_data'):
        wrong_plot_y_data = copy.deepcopy(CONFIG)
        wrong_plot_y_data["plots"]["bias_amplitude"]["y_data"] = "non-existing-data"
        Config(wrong_plot_y_data)

#rethink error naming convention

