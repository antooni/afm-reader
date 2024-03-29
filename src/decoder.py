from typing import Dict
from NSFopen.read import read as afmreader
import numpy as np
from config import Config


def decode_afm(path):
    return afmreader(path, verbose=False).data

def get_data_from_decoded(decoded, data_config) -> Dict[str, np.ndarray]:
  data: Dict[str, np.ndarray] = {}

  for key, value in data_config.items():
    try: 
      d: np.ndarray = decoded[value[0]][value[1]][value[2]]
    except: 
        raise NameError('!!! Config error !!!')
    data[key] = d  
  return data

def decode(path, config: Config) -> Dict[str, np.ndarray]:
  #validate data with config
  decoded = decode_afm(path)
  return get_data_from_decoded(decoded, config.data_config)
