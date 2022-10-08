import os
from common import get_average, get_data, plot, save_csv
from path_creator import PathCreator
from config import PlotConfig
import numpy as np


class PlotGenerator:
    def __init__(self, path_creator: PathCreator, config: dict[str, PlotConfig], data):
        self.path_creator = path_creator
        self.config = config 
        self.data = data
    
    def generate_all(self):
        for _, plot_config in self.config.items():
            try:
                self.plot(plot_config, self.data)
            except:
                raise NameError('!!! Config error !!!')


    def plot(self, plot_config: PlotConfig, data: dict[str, np.ndarray]):

        path = self.path_creator.get_plot_path(plot_config.x_name + '-' + plot_config.y_name)

        x_data = get_data(plot_config.x_data, data)
        y_data = get_data(plot_config.y_data, data)

        x_average = get_average(x_data)
        y_average = get_average(y_data)

        plot(x_data, y_data, plot_config.x_name, plot_config.x_unit, plot_config.y_name, plot_config.y_unit, path)
        plot(x_average, y_average, plot_config.x_name+"-average", plot_config.x_unit, plot_config.y_name+"-average", plot_config.y_unit, path)
        
        save_csv(os.path.join(path,plot_config.x_name),x_data)
        save_csv(os.path.join(path,plot_config.x_name + "-average") ,x_average )
        save_csv(os.path.join(path ,plot_config.y_name),y_data)
        save_csv(os.path.join(path , plot_config.y_name + "-average"),y_average)