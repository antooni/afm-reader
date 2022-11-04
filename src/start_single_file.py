from config import Config
import decoder
from file_generator import file_all
from iowrapper import IOWrapper
from plot_generator import plot_all

#pass only decoded
def start_single_file(config: Config, file_path):
    # get data
    # we leave it as dict for easier mock
    data = decoder.decode(file_path, config)

    # initialize
    iowrapper = IOWrapper(file_path, config.output_path)
    
    # run
    file_all(config.files_config, data, iowrapper) 
    plot_all(config.plots_config, data, iowrapper)

    print('🎉 finished processing ' + file_path)



