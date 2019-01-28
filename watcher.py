"""
Main watcher module

Example
>>> python -m watcher handlers/hello_world.py .
"""
import time
import imp

import fire

from watchdog.observers import Observer


def main(handler, source_path):
    """Main watcher that that takes handler and path to watch.

    :type handler: str
    :param handler: path to handler module to run
    :type source_path: str
    :param source_path: path to the directory to watch
    """
    with open(handler) as f:
        handler_source_code = ''.join([line for line in f])
        handler_module = imp.new_module('hook')
        exec handler_source_code in handler_module.__dict__

    # start the watcher. if the path is not given it'll observes the
    # current directory
    observer = Observer()
    observer.schedule(handler_module.Handler(),
                      path=source_path or '.',
                      recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


if __name__ == '__main__':
    fire.Fire(main)
