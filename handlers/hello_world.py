from watchdog.events import PatternMatchingEventHandler


class Handler(PatternMatchingEventHandler):
    """Example of how a handler would function

    possible event type `event.event_type`:
        'modified' | 'created' | 'moved' | 'deleted'

    check to see if the event is from a directory:
        event.is_directory (returns True or False)

    event path:
        `event.src_path`

    Use the pattern variable to define what files to process, for example:
    patterns = ["*.pdf"]
    """

    def process(self, event):
        """ This is the actual method that dose the magic.

        :type event:
        :param event:
        """
        # logging
        print event.src_path, event.event_type, type(event)

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)
