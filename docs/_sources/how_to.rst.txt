.. Owl documentation master file, created by
   sphinx-quickstart on Sat Jan 26 11:51:23 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

How to
======
Now that you have the requirements :ref:`installed <instalation>`, you're ready
to start using the ``Owl``.

The syntax is quit simple. You need just need a :ref:`Handler <handler>` and
the path that you want to monitor:

.. code-block:: shell

   python <PATH>/<TO>/owl/watcher.py <PATH>/<TO>/handler.py ~/User/

Quick Example
-------------
Owl comes with a ``hello_world`` handler which can be used to test and make
sure we have everything setup correctly.

assuming I cloned Owl repository in the following path:

.. code-block:: shell

   /Users/ali.jafargholi/repos/owl

we can find the ``watcher.py`` module at the root level and the ``hello_world.py``
handler inside the **handlers** directory. Therefore we can run our watcher using
this handler like so:

.. code-block:: shell

   python /Users/ali.jafargholi/repos/owl/watcher.py /Users/ali.jafargholi/repos/owl/handlers/hello_world.pt .

The above code starts the watcher on the current directory and will print any
action in the terminal

.. image:: ./_static/gif/quick_start.gif

.. note:: If you have ``owl`` in your ``PYTHONPATH`` you can use ``-m`` argument
          instead of giving the full path to the ``watcher``

          .. code-block:: shell

             python -m watcher handler.py .

.. toctree::
   :maxdepth: 2
   :caption: Contents:
