=========
textshare
=========

*A simple command line utility to share code and texts*

============
installation
============

.. code-block:: bash

    $ pip install textshare

=====
usage
=====

textshare [OPTIONS] [FILEPATHS]...

Options:
-i, --input  uses stdin as input
--help       Show this message and exit.

========
examples
========

.. code-block:: bash 

    $ textshare filename1 filename2

    $ cat file | textshare -i
