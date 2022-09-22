from afm_reader import start_single_file
from afm_watchdog import start_watchdog
from config import Config
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise NameError('Too little arguments provided')

    config_path = sys.argv[1]
    config = Config(config_path)

    if len(sys.argv) == 2:
        print('🔍 Watch mode | folder: ' + config.sourcePath)
        start_watchdog(config)


    if len(sys.argv) == 3:
        file_path = sys.argv[2]
        print('📩 Single run mode | file: ' + file_path)
        start_single_file(config, file_path)
