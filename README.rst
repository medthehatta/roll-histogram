Dice Rolls
==========

Roll dice and produce a histogram.


Usage::

    usage: roll.py [-h] [-f FACE | -d FACES_THRU] -n NUMBER [--drop-low]
                   [--drop-high] [--trials TRIALS]
                   outfile

    positional arguments:
      outfile               Path to output image for the histogram (e.g.
                            /tmp/foo.png)

    optional arguments:
      -h, --help            show this help message and exit
      -f FACE, --face FACE  Specify each face value. Repeat to add more faces.
      -d FACES_THRU, --faces-thru FACES_THRU
                            Specify the max space value, and use faces 1 through
                            FACES_THRU
      -n NUMBER, --number NUMBER
                            How many dice to roll each time. The "N" in Nd6, e.g.
      --drop-low            Whether to drop the lowest value from each roll
      --drop-high           Whether to drop the highest value from each roll
      --trials TRIALS       Number trials for producing the histogram (default:
                            100000)
