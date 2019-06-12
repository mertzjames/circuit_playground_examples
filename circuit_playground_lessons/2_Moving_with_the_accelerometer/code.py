"""Creating a Level

## Overview

This exercise will show you how to create a simple leveling device and
light up the LED(s) to indicate the direction of the tilt of the board.

## Setup

In this exercise there's no need to configure the board with anything
besides copying `code.py` onto the CPX board.
"""

import time

from math import atan, sqrt, degrees

import adafruit_lis3dh
from adafruit_circuitplayground.express import cpx

# Setup the board:
cpx.pixels.brightness = 0.01
cpx.pixels.auto_write = False

# This one is new (and a little hacky).  Basically, we're setting the
# accelerometer to be less sensitive to not detect all the really small
# changes in acceleration.  Unfortunately there is no way to change this
# without mucking around with the private vars.
#
# See also: https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/issues/60
cpx._lis3dh.range = adafruit_lis3dh.RANGE_16_G

GREEN = (0, 255, 0)
NO_COLOR = (0, 0, 0)

# This is used to set the threshold of how 'off center' the board is
# before we start showing that off centeredness.
L_THRESH = 2

# These are the mappings that we use to convert the degrees to the LEDs.
ANGLE_TO_LED_MAPPING = {
#   Angle   :   LED(s)
    0       :   [2],
    30      :   [3],
    60      :   [4],
    90      :   [4,5],
    120     :   [5],
    150     :   [6],
    180     :   [7],
    210     :   [8],
    240     :   [9],
    270     :   [9,0],
    300     :   [0],
    330     :   [1],
    360     :   [2]
}

def base_round(num, base=30):
    """
    This rounds to the nearest base multiple.  Taken from:
        https://stackoverflow.com/a/2272174/447015
    """
    return base * round(num/base)

def get_angle(x, y):
    """
    Returns the angle (in degrees) based on the x, y cords.  This
    assumes that the x and y are the adjacent and opposite sides of a
    right triangle.
    """

    # Since we're working with a full 360 degrees plane, we need to
    # adjust the values to the correct coordinate plane.
    deg_shift = 0
    if x < 0 and y > 0:
        deg_shift = 90
    elif x < 0 and y < 0:
        deg_shift = 180
    elif x > 0 and y < 0:
        deg_shift = 270

    a = abs(x)
    b = abs(y)

    rad_angle = atan(b / a)
    deg_angle = degrees(rad_angle)
    return int(deg_angle) + deg_shift

def get_l(x, y):
    """
    Returns the distance (or length) of a point from the origin.  This
    assumes that the x and y are the adjacent and opposite sides of a
    right triangle.  This uses the Pythangorean therom where:

        a^2 + b^2 = c^2
    """
    a = abs(x)
    b = abs(y)
    return sqrt(a ** 2 + b ** 2)

def main():

    while True:

        # empty the pixels to start off clean
        cpx.pixels.fill(NO_COLOR)

        # cpx.acceleration returns a tuple with three values (x, y, z).
        # These represent the current value of acceleration detected.
        # When sitting flat, the z value will be near 9.8 m/s^2 (the
        # force of gravity).  When tilting the board in any direction, 
        # that gravitational force will distribute to the x and y
        # values.
        x, y, z = cpx.acceleration

        # By calculating `l`, we can determine just how much "tilt"
        # there is away from laying flat.
        l = get_l(x, y)
        
        # We only want to proceed when `l` is greater than our defined
        # threshold above.
        if l > L_THRESH:

            # Next we calculate the angle of the tilt, round it to the
            # the nearest 30 degrees, and use that to light up the
            # appropriate leds.
            angle = get_angle(x, y)
            nearest_angle = base_round(angle)
            leds_to_light = ANGLE_TO_LED_MAPPING[nearest_angle]
            for pix in leds_to_light:
                cpx.pixels[pix] = GREEN
        
        # If we're laying flat (or nearly flat), then light up all the
        # leds.
        else:
            cpx.pixels.fill(GREEN)

        # give the device a little bit of time between each calculation.
        time.sleep(0.2)


main()
