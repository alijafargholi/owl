from watchdog.events import PatternMatchingEventHandler


class Handler(PatternMatchingEventHandler):
    """Example of how a handler would function
    Use the pattern variable to define what files to process, for example:
    patterns = ["*.pdf"]
    """

    def process(self, event):
        """ This is the actual method that dose the magic based on the event.

        to check event type `event.event_type`:
        ``modified`` | ``created`` | ``moved`` | ``deleted``

        to check to see if the event is from a directory:
            event.is_directory (returns True or False)

        event path where the action take place:
            `event.src_path`

        :type event: watchdog.events
        :param event:
        """
        # logging
        print event.src_path, event.event_type, type(event)

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)
