import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict

from config import PlotConfig


def get_data(labels: List[str],  data: Dict[str, np.ndarray]) -> np.ndarray:
  return data[labels[0]]
  # d: np.ndarray = np.array([])
  # i: int = 0
  
  # for label in labels:
  #   if i == 0:
  #     d = data[label]
  #   else:
  #     flipped = np.fliplr(data[label])
  #     d = np.concatenate((d, data[label]), axis=1)
  #   i += 1
  
  # return d

def get_average(data: np.ndarray) -> np.ndarray:
  return np.mean(data, axis=0)

def plot(x:np.ndarray, y: np.ndarray, plot_config: PlotConfig):
  plt.xlabel(plot_config.x_name + ' ['+ plot_config.x_unit +']')
  plt.ylabel(plot_config.y_name + ' ['+ plot_config.y_unit +']')

  if plot_config.x_lim != None:
    plt.xlim(plot_config.x_lim[0], plot_config.x_lim[1])

  if plot_config.y_lim != None:
    plt.ylim(plot_config.y_lim[0], plot_config.y_lim[1])


  # if len(x.shape) == 1:
    # plt.plot(x, y)
  else:
    for i in range(len(y)):
      plt.plot(x[i], y[i])

  fig = plt.gcf()
  return fig




