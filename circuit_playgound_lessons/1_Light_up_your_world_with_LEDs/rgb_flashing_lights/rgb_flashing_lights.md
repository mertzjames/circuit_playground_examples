# RGB Flashing Lights

In this exercise, you'll learn how to get your CPE board to automatically change colors from Red, Green, and Blue every 0.5 seconds.  You will also learn about the following programming, Python, and other concepts:

* The NeoPixel LED
* Color scales using RGB
* Tuples
* The "modulo" or "mod" (`%`) operator

## Required Setup

In this exercise you'll need the following:

* The CPX board, connected to your computer
* VsCode (or your fav editor) open with the `code.py` file open

## Key Concepts

### Color Scales Using RGB

Since the NeoPixel uses the Red, Green, Blue LED's to create different colors, you should learn how to create different colors using the RGB color model.  The RGB color model consists of defining three number values ranging from 0 to 255 as an intensity for the three colors.  The first number is always Red, the second Green, and the third Blue.  

Lets say you have an RGB value of 0, 0, 255 that would mean that the intensity of Blue is full and the other two colors is 0.  This means that the color shown is Blue!  The same goes for Red (255, 0, 0) and Green (0, 255, 0).  You can combine the intensities of different colors to generate another color!  255, 255, 0 would produce Yellow for example.  With these combination there is 255 * 255 * 255 or 16,581,375 different colors!  If you want to play around with the different values and see what they produce, checkout [this online RGB Color Tool](https://www.rapidtables.com/web/color/RGB_Color.html).

### Tuples

When working with the NeoPixel LEDs, they require passing in a tuple that represents the RGB value to change their color.  In Python (and some other programming) languages, tuples are used as a way to store a sequence of objects.  What makes tuples unique from other sequences, is that once they are defined, they are immutable, or they cannot be changed.  To create a tuple in Python, you assign a variable a set of objects separated by a comma (`,`):

```pycon
>>> my_first_tuple = 1, 2, 3
>>> my_first_tuple
(1, 2, 3)
```

Typically, this assignment is also surrounded by parenthesis as well, BUT is not required.  However, I highly recommend that you do this for readability sake:

```pycon
>>> my_first_tuple = (1, 2, 3)
>>> my_first_tuple
(1, 2, 3)
```

You can access elements of the tuple by indexing into it (Python uses `0` to represent the first item in sequences):

```pycon
>>> my_first_tuple[0]
1
```

Be careful about trying to index into a tuple item outside of it's range:

```pycon
>>> my_first_tuple[100]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
```

Because the tuple is immutable, if you try to change one of the items in the tuple, you'll get an error:

```pycon
>>> my_first_tuple[0] = 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

### The NeoPixel LED

The NeoPixel LED is a simple output device that is used to create lighted colors on your CPX board.  These LEDs are actually 3 LEDs in one!

[![Neopixel LED with RGB color LEDs courtesy of adafruit](../../images/led_strips_single-neopixel.jpg)](https://blog.adafruit.com/2017/12/12/neopixels-five-years-in-adafruit-neopixels/)

There are three colored LEDs that make up this NeoPixel; Red, Green, and Blue (RGB).  By combining various combinations of these LEDs, the Neopixel is able to provide a wide range of different colors.

To make changes to the NeoPixels on the CPX, you'll need to access the `.pixels` object in the `cpx` module and call the `.fill()` function:

```python
from adafruit_circuitplayground.express import cpx

# Fill all the pixels with Red
cpx.pixels.fill((255, 0, 0))
```

You can also index into an individual pixel and change its color:

```python
# Fill the first pixel with Green
cpx.pixels[0].fill((0, 255, 0))
```

### The "Modulo" or "Mod" (`%`) Operator

The modulo or mod operator in Python is the percent (`%`) symbol.  The modulo operator is basically the remainder of a division.  For example, if we were to take 2 / 3, the answer would be 0 with a remainder of 2.  Now lets take 3 / 3, the answer would be 1 with remainder of 0.  Finally let's take 4 / 3, the answer is 1 with remainder of 1.  Getting the remainder value is done by using the modulo operator:

```pycon
>>> 2 % 3
2
>>> 3 % 3
0
>>> 4 % 3
1
```

For this lesson, we want to loop through items within a tuple and when we get into the end, wrap around to the beginning.  We can do that by using the mod `%` operator:

```python
my_first_tuple = (1, 2, 3)
my_index = 0

while True:
    my_index = (my_index + 1) % len(my_first_tuple)
```

## Putting It All Together

Go ahead and open up [`code.py`](code.py) associated with this exercise and take a look at the code.  Based on what you've learned in this lesson, what should happen when this code is executed?

If you said that all NexPixels will forever change color every 0.5 seconds, rotating between Red, Green, and Blue, then you got it!  To get this working on your board, copy and paste into the `code.py` on your CPE board.

## Make It Your Own

Now that you've gotten an idea of how to change the NeoPixels, are there other colors that you would like to display?  Try playing around with the different colors and add them to the `COLORS` tuple.  

## What Next

## Troubleshooting

If you run into a problem, feel free to create a github issue.
