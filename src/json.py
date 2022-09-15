import json
import sys

class Config:
  def __init__(self, json_string):
    config = json.loads(json_string)
    self.sourcePath = config["sourcePath"]
    self.outputPath = config["outputPath"]
    self.data = config["data"]
    self.files = config["files"]
    self.plots = config["plots"]

def start(string):
  config = Config(string)
  print(config.data["bias"])

if __name__ == "__main__":
  start(sys.argv[1])