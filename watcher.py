import time
import imp
import urllib2
import sys
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


if __name__ == '__main__':
    handler, destination_path = sys.argv[1:]
    with open(handler) as f:
        print ''.join([line for line in f])


    # print args
    # code = ''.join([line for line in urllib2.urlopen(e)])
    # hook = imp.new_module('hook')
    # exec code in hook.__dict__
    # hook.main()

    # observer = Observer()
    # observer.schedule(MyHandler(), path=args[0] if args else '.')
    # observer.start()
    #
    # try:
    #     while True:
    #         time.sleep(1)
    # except KeyboardInterrupt:
    #     observer.stop()
    #
    # observer.join()