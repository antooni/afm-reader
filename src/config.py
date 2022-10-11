import json
from typing import Dict, List

class Config:
  def __init__(self, config: dict):
    self.source_path: str = config["source_path"]
    self.output_path: str = config["output_path"]

    self.data: Dict[str, List[str]] = config["data"]
    
    self.files: Dict[str, FileConfig] = {}
    for key, value in config["files"].items():
      self.files[key] = FileConfig(value)

    self.plots: Dict[str, PlotConfig] = {}
    for key, value in config["plots"].items():
      self.plots[key] = PlotConfig(value)

class FileConfig:
  def __init__(self, file_config):
    self.data_key: str = file_config["data_key"]
    self.multiplier: float = float(file_config.get("multiplier", 1))
    self.transpose: bool = bool(file_config.get("transpose", False))

class PlotConfig: 
  def __init__(self, plot_config):
    self.x_data: List[str] = plot_config["x_data"]
    self.x_name: str = plot_config["x_name"]
    self.x_unit: str = plot_config["x_unit"]
    self.x_multiplier: float = float(plot_config.get("x_multiplier", 1))
    self.x_lim: List[float] | None = plot_config.get("x_lim", None)
    self.y_data: List[str] = plot_config["y_data"]
    self.y_name: str = plot_config["y_name"]
    self.y_unit: str = plot_config["y_unit"]
    self.y_multiplier: float = float(plot_config.get("y_multiplier", 1))
    self.y_lim: List[float] | None = plot_config.get("y_lim", None)




def get_config(config_path: str) -> Config:
  file = open(config_path)
  config_json = json.load(file)
  return Config(config_json)