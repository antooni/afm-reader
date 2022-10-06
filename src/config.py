import json
from typing import Dict

class Config:
  def __init__(self, config: dict):
    self.source_path: str = config["sourcePath"]
    self.output_path: str = config["outputPath"]

    self.data: Dict[str, list[str]] = config["data"]
    
    self.files: Dict[str, FileConfig] = {}
    for key, value in config["files"].items():
      self.files[key] = FileConfig(value)

    self.plots: Dict[str, PlotConfig] = {}
    for key, value in config["plots"].items():
      self.plots[key] = PlotConfig(value)

class FileConfig:
  def __init__(self, file_config):
    self.data_name = file_config["data_name"]
    self.multiplier = int(file_config.get("multiplier", 1))
    self.transpose = bool(file_config.get("transpose", False))

class PlotConfig: 
  def __init__(self, plot_config):
    self.x_data = plot_config["x_data"]
    self.x_unit = plot_config["x_unit"]
    self.y_data = plot_config["y_data"]
    self.y_unit = plot_config["y_unit"]


def get_config(config_path: str) -> Config:
  file = open(config_path)
  config_json = json.load(file)
  return Config(config_json)