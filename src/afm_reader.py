from config import Config
import decoder
from file_generator import FileGenerator
from path_creator import PathCreator
from plot_generator import PlotGenerator

#pass only decoded
def start_single_file(config: Config, file_path):
    data = decoder.decode(file_path, config)

    # initialize
    path_creator = PathCreator(file_path, config.output_path)
    file_generator = FileGenerator(path_creator, config.files, data)
    plot_generator = PlotGenerator(path_creator, config.plots, data)
    
    # run
    file_generator.generate_all()
    plot_generator.generate_all()



