import os
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


#maybe it should also handle saves and be kind of IOWrapper
class IOWrapper: 
  def __init__(self, file_path: str, output_path: str):
    self.output_prefix = get_output_prefix(file_path,output_path)

  def get_file_path(self, name: str) -> str:
    save_path = os.path.join(self.output_prefix, 'files', name)
    Path(save_path).mkdir(parents=True, exist_ok=True)
    return save_path

  def get_plot_path(self,name):
    save_path = os.path.join(self.output_prefix, 'plots', name)
    Path(save_path).mkdir(parents=True, exist_ok=True)
    return save_path 

  def save_csv(self, name, data):
    save_csv(name, data)

  def save_plot(self, name, data):
    save_plot(name, data)

def get_output_prefix(file_path, output_path):
    file_name = file_path.split('/')[-1].split('.')[0]
    return os.path.join(output_path, file_name)

def save_csv(name: str, data):
  np.savetxt(name +'.csv', data, fmt='%s', delimiter=",")

def save_plot(path: str, fig):
  plt.show()
  fig.savefig(path, dpi=300)