import sys
from config import Config
import decoder
import plotter
from pathlib import Path
import argparse

def getOutputPrefix(filePath, configOutputPath):
    fileName = filePath.split('/')[-1].split('.')[0]
    Path(configOutputPath + '/' + fileName).mkdir(parents=True, exist_ok=True)
    return configOutputPath + '/' + fileName + '/' + fileName

def run(configPath, filePath):
    config = Config(configPath)
    data = decoder.decode(filePath, config)
    outputPrefix = getOutputPrefix(filePath, config.outputPath) 

    for f in config.files:
      try:
        plotter.saveFile(outputPrefix, data[f], f)
      except:
        raise NameError('!!! Config error !!!')

    for p in config.plots:
      try:
        plotter.plot(outputPrefix,data[p[0]], data[p[2]], p[0], p[1], p[2], p[3], config.outputPath)
      except:
        raise NameError('!!! Config error !!!')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise NameError('Too little arguments provided')

    configPath = sys.argv[1]
    filePath = sys.argv[2]

    run(configPath, filePath) 


    

