import matplotlib.pyplot as plt
import numpy as np


def save_file(output_prefix, data, data_name):
  save_path = output_prefix+'-'+data_name+'.csv'
  np.savetxt(save_path, data, fmt='%s', delimiter=",")

def plot(output_prefix, x, y, name_x, unit_x, name_y, unit_y, xlim = None, ylim = None):
  for i in range(len(y)):
      plt.plot(x[i], y[i])

  if xlim != None:
      plt.xlim(xlim)
  if ylim != None:
      plt.ylim(ylim)

  plt.xlabel(name_x + ' ['+ unit_x +']')
  plt.ylabel(name_y + ' ['+ unit_y +']')

  save_path = output_prefix+'-plot-'+name_x+'-'+ name_y+'.png'

  fig = plt.gcf()
  fig.savefig(save_path, dpi=300)
  plt.show()

