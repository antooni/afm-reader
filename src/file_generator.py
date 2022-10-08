
import os
from common import save_csv
from config import FileConfig
from path_creator import PathCreator
import numpy as np

class FileGenerator:
    def __init__(self, path_creator: PathCreator, config: dict[str, FileConfig], data):
        self.path_creator = path_creator        
        self.config: dict[str, FileConfig] = config
        self.data = data

    def generate_all(self):
        for _, file in self.config.items():
            try:
                self.save_file(self.data[file.data_key], file)
            except:
                raise NameError('!!! Config error !!!')

    def save_file(self, data: np.ndarray, file_config: FileConfig):
        path = os.path.join(self.path_creator.get_file_path(file_config.data_key), file_config.data_key)

        if file_config.multiplier != 1:
            multiplied = np.multiply(data, file_config.multiplier)
            save_csv(path  + '-multiplied', multiplied)

        if file_config.transpose == True:
            transposed = np.transpose(data)
            save_csv(path + '-transposed', transposed)

        save_csv(path, data)




