import matplotlib.pyplot as plt
import numpy as np

from config import PlotConfig

def save_file(output_prefix, data, data_name):
  save_path = output_prefix+'-'+data_name+'.csv'
  np.savetxt(save_path, data, fmt='%s', delimiter=",")

def get_data(labels: list[str],  data):
  d = None
  i = 0
  
  for label in labels:
    if i == 0:
      d = data[label]
    else:
      flipped = np.fliplr(data[label])
      d = np.concatenate((d, flipped), axis=1)
    i += 1
  
  return d

def get_average(data):
  return np.mean(data, axis=0)

def plot_atomic(x,y,name_x, unit_x, name_y, unit_y, output_prefix):
  plt.xlabel(name_x + ' ['+ unit_x +']')
  plt.ylabel(name_y + ' ['+ unit_y +']')

  save_path = output_prefix+'-plot-'+name_x+'-'+ name_y+'.png'

  if len(x.shape) == 1:
    plt.plot(x, y)
  else:
    for i in range(len(y)):
      plt.plot(x[i], y[i])

  fig = plt.gcf()
  fig.savefig(save_path, dpi=300)
  plt.show()


def plot(plot_config: PlotConfig, data, output_prefix: str):

  x_data = get_data(plot_config.x_data, data)
  y_data = get_data(plot_config.y_data, data)

  x_average = get_average(x_data)
  y_average = get_average(y_data)

  plot_atomic(x_data, y_data, "X", plot_config.x_unit, "Y", plot_config.y_unit, output_prefix)
  plot_atomic(x_average, y_average, "X-average", plot_config.x_unit, "Y-average", plot_config.y_unit, output_prefix)
  # save_file(np.concatenate(x_data, x_average))
  # save_file(np.concatenate(y_data, y_average))

