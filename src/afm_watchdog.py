import time
import os
from afm_reader import start_single_file
from config import Config

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

import glob
 
   
def created(event, config: Config):
    recent_size = -1
    file_path = event.src_path
    while (recent_size != os.path.getsize(file_path)):
        recent_size = os.path.getsize(file_path)
        time.sleep(10)
    print("file copy has now finished")
    start_single_file(config, file_path)


def start_watchdog(config: Config):
    files = os.listdir(config.source_path)

    for file in files:
    # check only text files
        if file.endswith('.nid'):
            start_single_file(config,os.path.join(config.source_path, file))            

    #get only .nid
    patterns = ["*.nid"]
    ignore_patterns = None
    ignore_directories = True
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    go_recursively = False
    my_event_handler.on_created = lambda event : created(event, config)
    my_observer = Observer()
    my_observer.schedule(my_event_handler, config.source_path, recursive=go_recursively)
    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()


