"""For a detailed guide on all the features of the Circuit Playground Express (cpx) library:
https://adafru.it/cp-made-easy-on-cpx"""
import time
from adafruit_circuitplayground.express import cpx

# Colors for the 'trail'
BLUE_1 = (0, 51, 102)
BLUE_2 = (0, 76, 153)
BLUE_3 = (0, 102, 204)
BLUE_4 = (51, 153, 255)
BLUE_5 = (102, 178, 255)
BLUE_6 = (153, 204, 255)

# The rest of the LED's we want 'off'
NO_COLOR = (0, 0, 0)

cpx.pixels.brightness = 0.01
cpx.pixels.auto_write = False

# 
num_neo_pix = len(cpx.pixels)

neo_pix_locs = list(range(6))
neo_pix_locs.reverse()
neo_pix_colors = (
    BLUE_1,
    BLUE_2,
    BLUE_3,
    BLUE_4,
    BLUE_5,
    BLUE_6
)

start = time.monotonic()
last_button_press = start
go_left = False
color_i = 0

while True:
    now = time.monotonic()

    if cpx.button_a and (now - last_button_press) > 0.2:
        go_left = False
        last_button_press = now
    elif cpx.button_a and (now - last_button_press) > 0.2:
        go_left = True
        last_button_press = now

    if now - start > 0.05:
        cpx.pixels.fill(NO_COLOR)
        for c, p in zip(neo_pix_colors, neo_pix_locs):
            cpx.pixels[p] = c
        cpx.pixels.show()
        start = now
        if go_left:
            neo_pix_locs = [(p + 1) % num_neo_pix for p in neo_pix_locs]
        else:
            neo_pix_locs = [(p - 1) % num_neo_pix for p in neo_pix_locs]
