import json

class Config:
  def __init__(self, config_file):
    file = open(config_file)
    config = json.load(file)
    self.sourcePath = config["sourcePath"]
    self.outputPath = config["outputPath"]
    self.data = config["data"]
    self.files = config["files"]
    self.plots = config["plots"]

#create config with checks
#cehck if folder path ends with /