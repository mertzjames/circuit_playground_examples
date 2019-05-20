"""RGB Flashing Lights

## Overview

This excercise will show you how to flash the LED's of the board
rotating through three different colors; Red, Green, and Blue.

## Setup

In this excercise there's no need to configure the board with anything
besides coping `code.py` onto the CPE board.
"""

import time
from adafruit_circuitplayground.express import cpx

# Here we define three different colors using a tuple structure.  There
# are three numbers in the tuple, each representing how much of a
# specific color should be displayed.  For the CPE board, the three
# colors are Red, Green, and Blue (RGB).  The values possible ranges
# from 0 (none of that color) to 256 (all of that color).  In this
# example we only do three colors; Red, Green, and Blue.
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# We know place these colors into another tuple for us to iterate
# (step through) later on.
COLORS = (RED, GREEN, BLUE)

# Adjust the brightness to 30% of the possibility.  Possible range is
# 0.0 to 1.0
cpx.pixels.brightness = 0.3

# This option ensures that the LED's are only updated when the `.show()`
# is called on the LED's.
cpx.pixels.auto_write = False

# Get the current time as "start" to see how much time has passed later
# on.
start = time.monotonic()

# color_i is used to keep track of which color to display next.
color_i = 0

# This is the main loop of the board.  This will run infinetly.
while True:

    # Get the current time
    now = time.monotonic()

    # Because of how fast this loop is going, if we switched colors each
    # loop, it would be too fast to see the changes correctly.  So, we
    # only update the LED's after at least 0.5 seconds have passed.
    if now - start > 0.5:

        # Get the color from the tuple we defined above, set that to be
        # the next color for the LED's `.fill()`, and then update the
        # board to actually display that color `.show()`
        color = COLORS[color_i]
        cpx.pixels.fill(color)
        cpx.pixels.show()

        # The `%` operator may be unfamiliar to you.  This is the
        # "modulo" operator and basically returns the "remainder" of
        # the division.  For example, in our case, there are three
        # colors in our tuple `COLORS` above, so that tuple has a length
        # of 3.  With that in mind:
        #   
        #   2 % 3 = 2
        #   3 % 3 = 0
        #   4 % 3 = 1 (Note: this will never happen in our code; see below)
        #
        # When we reach the last item in the `COLORS` list, we need to
        # restart back to the beginning, so we use this "modulo" aka mod
        # operator to do just that.  This means that we'll infintely
        # change `color_i` like so:
        # 
        #   0, 1, 2, 0, 1, 2, 0, ...
        color_i = (color_i + 1) % len(COLORS)

        # Since we've made an update to the LED's we want to reset when
        # we make the update to the LED's to another 0.5 seconds from
        # now, so we need to update `start` to the current time.
        start = now
