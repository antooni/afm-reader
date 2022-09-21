import time
import os
import sys
from afm_reader import run
from config import Config


from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

try:
    file = open("ignore.txt", "r")
    extensions = file.read().splitlines()
    file.close()
except:
    extensions = []
 

def created(event):
    print('hello') 
    print(event) 
    filename = event.src_path.split('/')[-1]
    print(filename)

def deleted(event):
    print('deleted')
   
def modified(event):
    historicalSize = -1
    filePath = event.src_path
    while (historicalSize != os.path.getsize(filePath)):
        historicalSize = os.path.getsize(filePath)
        time.sleep(10)
    print("file copy has now finished")
    # how to get configPath there
    run(configPath, filePath)


def start(configPath):
    config = Config(configPath)

    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = True
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    go_recursively = False
    my_event_handler.on_created = modified
    my_event_handler.on_deleted = deleted
    my_event_handler.on_moved = created
    my_observer = Observer()
    my_observer.schedule(my_event_handler, config.sourcePath, recursive=go_recursively)
    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()

if __name__ == "__main__":

    configPath = sys.argv[1]

    start(configPath) 

