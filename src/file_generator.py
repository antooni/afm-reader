
import os
from config import FileConfig
from iowrapper import IOWrapper
import numpy as np

def file_all(config: dict[str, FileConfig], data, iowrapper: IOWrapper):
    for _, file in config.items():
        try:
            save_file(data[file.data_key], file, iowrapper)
        except:
            raise NameError('!!! Config error !!!')

def save_file(data: np.ndarray, file_config: FileConfig, iowrapper: IOWrapper):
    path = os.path.join(iowrapper.get_file_path(file_config.data_key), file_config.data_key)

    if file_config.multiplier != 1:
        multiplied = np.multiply(data, file_config.multiplier)
        iowrapper.save_csv(path  + '-multiplied', multiplied)

    if file_config.transpose == True:
        transposed = np.transpose(data)
        iowrapper.save_csv(path  + '-transposed', transposed)

    iowrapper.save_csv(path, data)




