import os
from pathlib import Path

class PathCreator: 
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

def get_output_prefix(file_path, output_path):
    file_name = file_path.split('/')[-1].split('.')[0]
    return os.path.join(output_path, file_name)
