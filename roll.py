#!/usr/bin/env python


from __future__ import (
    print_function, division, absolute_import, unicode_literals,
)


"""Produce a histogram of dice rolls."""


import pandas as pd
import random


def do_rolls(faces, number, drop_low=False, drop_high=False):
    """Roll FdN where ``faces`` is F, ``number`` is N."""
    rolls = [random.choice(faces) for _ in range(number)]
    if drop_low:
        rolls.remove(min(rolls))
    if drop_high:
        rolls.remove(max(rolls))
    return rolls


def main():
    """Entry point."""
    import argparse
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-f', '--face', type=int, action='append',
        help='Specify each face value.  Repeat to add more faces.',
    )
    group.add_argument(
        '-d', '--faces-thru', type=int,
        help='Specify the max space value, and use faces 1 through FACES_THRU',
    )
    parser.add_argument(
        '-n', '--number', required=True, type=int,
        help='How many dice to roll each time.  The "N" in Nd6, e.g.',
    )
    parser.add_argument(
        '--drop-low', action='store_true',
        help='Whether to drop the lowest value from each roll',
    )
    parser.add_argument(
        '--drop-high', action='store_true',
        help='Whether to drop the highest value from each roll',
    )
    parser.add_argument(
        '--trials', default=100000, type=int,
        help='Number trials for producing the histogram (default: 100000)',
    )
    parser.add_argument(
        'outfile',
        help='Path to output image for the histogram (e.g. /tmp/foo.png)',
    )
    parsed = parser.parse_args()

    faces = parsed.face or range(parsed.faces_thru)
    number = parsed.number
    drop_low = parsed.drop_low
    drop_high = parsed.drop_high
    trials = parsed.trials

    rolls = [
        sum(do_rolls(faces, number, drop_low, drop_high))
        for _ in range(trials)
    ]

    series = pd.Series(rolls)
    ax = series.hist()
    ax.get_figure().savefig(parsed.outfile)


if __name__ == '__main__':
    main()
