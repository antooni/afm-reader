from pathlib import Path
from typing import Dict
import matplotlib.pyplot as plt
import numpy as np

from config import FileConfig, PlotConfig

def save_atomic(output_prefix, data, name):
  np.savetxt(output_prefix + name +'.csv', data, fmt='%s', delimiter=",")

def save_file(output_prefix, data: np.ndarray, file_config: FileConfig):
  save_path = output_prefix+ '/file-'+file_config.data_name + '/' 
  Path(save_path).mkdir(parents=True, exist_ok=True)

  if file_config.multiplier != 1:
    multiplied = np.multiply(data, file_config.multiplier)
    save_atomic(save_path, multiplied, file_config.data_name + '-multiplied')
    # np.savetxt(save_path + file_config.data_name +'-multiplied.csv', multiplied, fmt='%s', delimiter=",")

  if file_config.transpose == True:
    transposed = np.transpose(data)
    save_atomic(save_path, transposed, file_config.data_name + '-transposed')
    # np.savetxt(save_path + file_config.data_name +'-transposed.csv', transposed, fmt='%s', delimiter=",")

  np.savetxt(save_path + file_config.data_name +'.csv', data, fmt='%s', delimiter=",")

def get_data(labels: list[str],  data: Dict[str, np.ndarray]) -> np.ndarray:
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

def plot_atomic(x: np.ndarray,y: np.ndarray,name_x, unit_x, name_y, unit_y, output_prefix):
  plt.xlabel(name_x + ' ['+ unit_x +']')
  plt.ylabel(name_y + ' ['+ unit_y +']')

  save_path = output_prefix+'plot-'+name_x+'-'+ name_y+'.png'

  if len(x.shape) == 1:
    plt.plot(x, y)
  else:
    for i in range(len(y)):
      plt.plot(x[i], y[i])

  fig = plt.gcf()
  fig.savefig(save_path, dpi=300)
  plt.show()


def plot(plot_config: PlotConfig, data: Dict[str, np.ndarray], output_prefix: str):

  output_prefix2 = output_prefix + '/plot-' + plot_config.x_name + '-' + plot_config.y_name + '/'
  Path(output_prefix2).mkdir(parents=True, exist_ok=True)

  x_data = get_data(plot_config.x_data, data)
  y_data = get_data(plot_config.y_data, data)

  x_average = get_average(x_data)
  y_average = get_average(y_data)

  plot_atomic(x_data, y_data, plot_config.x_name, plot_config.x_unit, plot_config.y_name, plot_config.y_unit, output_prefix2)
  plot_atomic(x_average, y_average, plot_config.x_name+"-average", plot_config.x_unit, plot_config.y_name+"-average", plot_config.y_unit, output_prefix2)
  save_atomic(output_prefix2,x_data, plot_config.x_name)
  save_atomic(output_prefix2,x_average, plot_config.x_name + "-average")
  save_atomic(output_prefix2,y_data, plot_config.y_name)
  save_atomic(output_prefix2,y_average, plot_config.y_name + "-average")

