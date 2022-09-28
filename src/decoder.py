from NSFopen.read import read as afmreader
import numpy as np
from config import Config


def decode_afm(path):
    return afmreader(path, verbose=False).data

def get_data_from_decoded(decoded, data_config):
  data = {}

  for key, value in data_config.items():
    arr = None
    i = 0
    for keys in value:
      try: 
        d = decoded[keys[0]][keys[1]][keys[2]]
        if i == 0:
          arr = d
        else:
          flipped = np.fliplr(d)
          arr = np.concatenate((arr, flipped), axis=1)
      except: 
        raise NameError('!!! Config error !!!')
      i += 1
    data[key] = arr  
  return data

def decode(path, config: Config):
  #validate data with config
  decoded = decode_afm(path)
  return get_data_from_decoded(decoded, config.data)
