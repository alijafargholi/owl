.. Owl documentation master file, created by
   sphinx-quickstart on Sat Jan 26 11:51:23 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _instalation:

Installation
============
``Owl`` relies on Google's `Fire <https://github.com/google/python-fire>`_
library for automatically generating command line interfaces *(CLIs)* and
`Watchdog <https://pythonhosted.org/watchdog/>`_ library for monitor file
system.

Installing Requirements
-----------------------
Install ``fire`` using ``pip`` like so:

.. code-block:: shell

   pip install fire

Then install ``watchdog``:

.. code-block:: shell

   pip install watchdog


Installing Owl
--------------
There are 2 ways of getting the latest version.

1- Download the `latest version <Owl <https://github.com/alijafargholi/owl/releases/latest>`_ of Owl by clicking `here <https://github.com/alijafargholi/owl/archive/master.zip>`_
   - then unzip anywhere you think it's more convenient to you. I ideally place
     it some in your ``PYTHONPATH``

2- Simply clone it in a desire location

.. code-block:: shell

   git clone https://github.com/alijafargholi/owl.git

.. image:: ./_static/gif/clone_owl.gif

.. toctree::
   :maxdepth: 2
   :caption: Contents:
