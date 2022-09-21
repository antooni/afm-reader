from NSFopen.read import read as afmreader
import numpy as np

def decodeAFM(path):
    return afmreader(path, verbose=False).data

def getDataFromDecoded(decoded, dataConfig):
  data = {}

  for key, value in dataConfig.items():
    arr = None
    i = 0
    for keys in value:
      try: 
        d = decoded[keys[0]][keys[1]][keys[2]]
        if i == 0:
          arr = d
        else:
          arr = np.concatenate((arr, d), axis=1)
      except: 
        raise NameError('!!! Config error !!!')
      i += 1
    data[key] = arr  
  return data

def decode(path, config):
  decoded = decodeAFM(path)
  return getDataFromDecoded(decoded, config.data)
