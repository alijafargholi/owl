.. Owl documentation master file, created by
   sphinx-quickstart on Sat Jan 26 11:51:23 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _handler:

Handler
=======
Handler, as the name suggest, handles the events that triggers by ``watcher``.
Basically in **Handler** you can decide what to do when an event happens, like
a file is added to a directory.

There are 2 basic part in the Handler:
   - **catch** the event
      - there are 4 event type: *modified*, *created*, *deleted*, *moved*
   - **do something** with the event

Create a Handler
________________

You need inherit from one the *Watchdog* `Event Handler Classes <https://pythonhosted.org/watchdog/api.html#event-handler-classes>`_

.. code-block:: python

   from watchdog.events import FileSystemEventHandler

Now you need to create the handler `class`.

.. important:: ``owl`` expects the class to be called **Handler**

.. code-block:: python

   class Handler(FileSystemEventHandler):

Then decide which *event* to catch:
   - **on_any_event**: Catch-all event handler
   - **on_created**: Called when a file or directory is created
   - **on_modified**: Called when a file or directory is created
   - **on_moved**: Called when a file or directory is modified.
   - **on_deleted**: Called when a file or a directory is moved or renamed.

In this example, we're going to catch if the ``create`` and ``delete`` events

.. code-block:: python
   :emphasize-lines: 1, 4

       def on_created(self, event):
           self.process_created_event(event)

       def on_deleted(self, event):
           self.process_delete_event(event)

Now this the fun part where you decide what to do with that event. Each event
has 3 attributes which you can use to determine whether or not the you need to
take action on this event:

   - **event_type**: The type of the event as a string.
   - **is_directory**: True if event was emitted for a directory; False otherwise.
   - **src_path**: Source path of the file system object that triggered this event.

.. code-block:: python

       def process_created_event(self, event):
           created_path = event.src_path
           print "New file is created: {}".format(created_path)

       def process_delete_event(self, event):
           deleted_path = event.src_path
           print "file is deleted: {}".format(deleted_path)

That's the basic of how you can create a ``handler``. There is a lot you can
do once you start digging into the `Watchdog <https://pythonhosted.org/watchdog/>`_.
It's fairly simple and powerful.

Here is the entire code:

.. code-block:: python

   from watchdog.events import FileSystemEventHandler

   class Handler(FileSystemEventHandler):
       def on_created(self, event):
           self.process_created_event(event)

       def on_deleted(self, event):
           self.process_delete_event(event)

       def process_created_event(self, event):
           created_path = event.src_path
           print "New file is created: {}".format(created_path)

       def process_delete_event(self, event):
           deleted_path = event.src_path
           print "file is deleted: {}".format(deleted_path)


.. toctree::
   :maxdepth: 2
   :caption: Contents:
