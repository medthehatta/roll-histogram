Dice Rolls
==========

Roll dice and produce a histogram.


Usage
-----

::

    usage: roll.py [-h] [-f FACE | -d FACES_THRU] [-n NUMBER] [--drop-low] [--drop-high] [--non-normalized]
                   [--trials TRIALS]
                   outfile

    positional arguments:
      outfile               Path to output image for the histogram (e.g. /tmp/foo.png)

    optional arguments:
      -h, --help            show this help message and exit
      -f FACE, --face FACE  Specify each face value. Repeat to add more faces.
      -d FACES_THRU, --faces-thru FACES_THRU
                            Specify the max space value, and use faces 1 through FACES_THRU
      -n NUMBER, --number NUMBER
                            How many dice to roll each time. The "N" in Nd6, e.g.
      --drop-low            Whether to drop the lowest value from each roll
      --drop-high           Whether to drop the highest value from each roll
      --non-normalized      Whether the y axis should be a ratio (the default) or an absolute number of counts
      --trials TRIALS       Number trials for producing the histogram (default: 100000)



Examples
--------

4d6 drop low::

    $ roll.py -n 4 -d 6 --drop-low /tmp/4d6dL.png

4dF::

    $ roll.py -n 4 -f -1 -f 0 -f 1 /tmp/fudge.png


Deployment
----------

Requires ``virtualenv``::

    $ cd /path/to/roll-histogram
    $ virtualenv my-venv
    $ . ./my-venv/bin/activate
    $ pip install -r ./requirements.txt

To use::

    $ cd /path/to/roll-histogram
    $ . ./my-venv/bin/activate
    $ ./roll.py ...
