from config import Config
import decoder
from file_generator import file_all
from path_creator import PathCreator
from plot_generator import plot_all

#pass only decoded
def start_single_file(config: Config, file_path):
    # get data
    # we leave it as dict for easier mock
    data = decoder.decode(file_path, config)

    # initialize
    # I have PathCreator because it can be easily mocked
    path_creator = PathCreator(file_path, config.output_path)
    
    # run
    file_all(config.files, data, path_creator) 
    plot_all(config.plots, data, path_creator)



