
import os
from common import save_csv
from config import FileConfig
from path_creator import PathCreator
import numpy as np

def file_all(config: dict[str, FileConfig], data, path_creator: PathCreator):
    for _, file in config.items():
        try:
            save_file(data[file.data_key], file, path_creator)
        except:
            raise NameError('!!! Config error !!!')

def save_file(data: np.ndarray, file_config: FileConfig, path_creator: PathCreator):
    path = os.path.join(path_creator.get_file_path(file_config.data_key), file_config.data_key)

    if file_config.multiplier != 1:
        multiplied = np.multiply(data, file_config.multiplier)
        save_csv(path  + '-multiplied', multiplied)

    if file_config.transpose == True:
        transposed = np.transpose(data)
        save_csv(path + '-transposed', transposed)

    save_csv(path, data)




