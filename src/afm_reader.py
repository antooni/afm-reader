from config import Config
import decoder
import plotter
from pathlib import Path

#pass only decoded
def start_single_file(config: Config, file_path):
    data = decoder.decode(file_path, config)

    create_output_path(file_path, config.output_path)
    output_prefix = get_output_prefix(file_path, config.output_path) 
    print(output_prefix)

    for key, file in config.files.items():
      try:
        plotter.save_file(output_prefix, data[file.data_name], file.data_name)
      except:
        raise NameError('!!! Config error !!!')

    for key, plot_config in config.plots.items():
      try:
        plotter.plot(plot_config, data, output_prefix)
      except:
        raise NameError('!!! Config error !!!')

def get_output_prefix(file_path, output_path):
    file_name = file_path.split('/')[-1].split('.')[0]
    #maybe some lib like encode path to avoid this error with /
    return output_path + '/' + file_name + '/'

def create_output_path(file_path, output_path):
    file_name = file_path.split('/')[-1].split('.')[0]
    Path(output_path + '/' + file_name).mkdir(parents=True, exist_ok=True)
    

