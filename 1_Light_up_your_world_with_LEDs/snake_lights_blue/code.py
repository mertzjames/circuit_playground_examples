"""For a detailed guide on all the features of the Circuit Playground Express (cpx) library:
https://adafru.it/cp-made-easy-on-cpx"""
import time
import microcontroller
from adafruit_circuitplayground.express import cpx

FULL = 255

BLUE_FULL = (0, 0, FULL)
BLUE_THREE_QUARTER = (0, 0, int(FULL * 0.75))
BLUE_TWO_THIRD = (0, 0, int(FULL * 0.66))
BLUE_HALF = (0, 0, int(FULL * 0.5))
BLUE_THIRD = (0, 0, int(FULL * 0.33))
BLUE_QUART = (0, 0, int(FULL * 0.25))

NO_COLOR = (0, 0, 0)

cpx.pixels.brightness = 0.3
cpx.pixels.auto_write = False

pix_len = len (cpx.pixels)

pixels_locs = list(range(6))
pixels_locs.reverse()
pixel_colors = (
    BLUE_FULL,
    BLUE_THREE_QUARTER,
    BLUE_TWO_THIRD,
    BLUE_HALF,
    BLUE_THIRD,
    BLUE_QUART
)

start = time.monotonic()
color_i = 0
while True:
    now = time.monotonic()

    if now - start > 0.5:
        cpx.pixels.fill(NO_COLOR)
        for c, p in zip(pixel_colors, pixels_locs):
            cpx.pixels[p] = c
        cpx.pixels.show()
        start = now
        pixels_locs = [(p + 1) % pix_len for p in pixels_locs]
