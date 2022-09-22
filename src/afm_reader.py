from config import Config
import decoder
import plotter
from pathlib import Path

def get_output_prefix(file_path, output_path):
    file_name = file_path.split('/')[-1].split('.')[0]
    return output_path + '/' + file_name + '/' + file_name

def create_output_path(file_path, output_path):
    file_name = file_path.split('/')[-1].split('.')[0]
    Path(output_path + '/' + file_name).mkdir(parents=True, exist_ok=True)

def start_single_file(config: Config, file_path):
    data = decoder.decode(file_path, config)

    create_output_path(file_path, config.output_path)
    output_prefix = get_output_prefix(file_path, config.output_path) 

    for f in config.files:
      try:
        plotter.saveFile(output_prefix, data[f], f)
      except:
        raise NameError('!!! Config error !!!')

    for p in config.plots:
      try:
        plotter.plot(output_prefix,data[p[0]], data[p[2]], p[0], p[1], p[2], p[3])
      except:
        raise NameError('!!! Config error !!!')



    

