KeyServer
==================

Command line Pub key generator from keyserver.ubuntu.com

        usage: keyserver.py [-h] [-k KEY] [-c] [-f FILENAME]

        optional arguments:
          -h, --help            show this help message and exit
          -k KEY, --key KEY     Key number for search pub key
          -c, --copy            Copy pub key result to clipboard
          -f FILENAME, --file FILENAME
                                Store pub key result to file**

::

    pip install keyserver

Example
-------

Command line
~~~~~~~~~~~~

**Get key**

::

    $ keyserver -k 3B4FE6ACC0B21F32 -f key1
    $ apt-key add key1

**Get key and Copy it to clipboard**

::

    $ keyserver -k 3B4FE6ACC0B21F32 -f key1 -c
    $ apt-key add key1



License
-------

MIT
