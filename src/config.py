import json

class Config:
  def __init__(self, config_file):
    file = open(config_file)
    config = json.load(file)
    #check config
    #cehck if folder path ends with /

    self.source_path = config["sourcePath"]
    self.output_path = config["outputPath"]
    self.data = config["data"]
    self.files = config["files"]
    self.plots = config["plots"]
