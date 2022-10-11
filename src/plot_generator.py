import os
from common import get_average, get_data, plot
from iowrapper import IOWrapper
from config import PlotConfig
import numpy as np
from typing import Dict

    
def plot_all(config: Dict[str, PlotConfig], data, iowrapper: IOWrapper):
    for _, plot_config in config.items():
        try:
            plot_and_save(plot_config, data, iowrapper)
        except:
            raise NameError('!!! Config error !!!')


def plot_and_save( plot_config: PlotConfig, data: Dict[str, np.ndarray], iowrapper: IOWrapper):
    path = iowrapper.get_plot_path(plot_config.x_name + '-' + plot_config.y_name)

    x_data = get_data(plot_config.x_data, data)
    y_data = get_data(plot_config.y_data, data)

    x_average = get_average(x_data)
    y_average = get_average(y_data)

    p = plot(x_data, y_data, plot_config.x_name, plot_config.x_unit, plot_config.y_name, plot_config.y_unit, path)
    pp = plot(x_average, y_average, plot_config.x_name+"-average", plot_config.x_unit, plot_config.y_name+"-average", plot_config.y_unit, path)
    
    save_path = os.path.join(path,'plot-'+plot_config.x_name+'-'+ plot_config.y_name+'.png')

    iowrapper.save_plot(save_path,p)
    iowrapper.save_plot(save_path,pp)

    iowrapper.save_csv(os.path.join(path,plot_config.x_name),x_data)
    iowrapper.save_csv(os.path.join(path,plot_config.x_name + "-average") ,x_average )
    iowrapper.save_csv(os.path.join(path ,plot_config.y_name),y_data)
    iowrapper.save_csv(os.path.join(path , plot_config.y_name + "-average"),y_average)