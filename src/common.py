import os
import numpy as np
import numpy as np
import matplotlib.pyplot as plt

from config import PlotConfig
from path_creator import PathCreator

def save_csv(name: str, data):
  np.savetxt(name +'.csv', data, fmt='%s', delimiter=",")


def get_data(labels: list[str],  data: dict[str, np.ndarray]) -> np.ndarray:
  d: np.ndarray = np.array([])
  i: int = 0
  
  for label in labels:
    if i == 0:
      d = data[label]
      print(type(data[label]))
    else:
      flipped = np.fliplr(data[label])
      d = np.concatenate((d, flipped), axis=1)
    i += 1
  
  return d

def get_average(data: np.ndarray) -> np.ndarray:
  return np.mean(data, axis=0)

def plot(x: np.ndarray,y: np.ndarray,name_x, unit_x, name_y, unit_y, output_prefix):
  plt.xlabel(name_x + ' ['+ unit_x +']')
  plt.ylabel(name_y + ' ['+ unit_y +']')

  save_path = os.path.join(output_prefix,'plot-'+name_x+'-'+ name_y+'.png')

  if len(x.shape) == 1:
    plt.plot(x, y)
  else:
    for i in range(len(y)):
      plt.plot(x[i], y[i])

  fig = plt.gcf()
  fig.savefig(save_path, dpi=300)
  plt.show()

