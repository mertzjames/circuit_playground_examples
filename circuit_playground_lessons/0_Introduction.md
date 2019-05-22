# Introduction

Welcome to your new Circuit Python Express (CPX).  This board is a very versatile board with lots of sensors and outputs.  In fact, there are about 48 different inputs and outputs that you can play with!

After going through this introduction you'll be able to:

* Understand the basic layout of your CPX board.
* Learn how to connect to and access the `code.py` file on your CPX board.
* Learn how connect and view any printed outputs from the CPX board as well as access the Python Repl.

There will also be a list of "Common Issues" that I've come across while using the board, with the known fixes or work arounds at the end of this introduction.

## An Overview the CPX Board

The CPX board comes with all sorts of inputs (such as sensors) and outputs (such as LED's) and other parts.  Let's take a look at a labeled version of your board:

[![Labeled CPX Board Courtesy of adafruit](/images/circuit_playground_express-labeled.jpg)](https://learn.adafruit.com/assets/46973)

Don't worry if some (or even all) of the things on this image don't make sense.  When you go through the examples, each of these will be explained in more detail in the examples.

| Part Name                  | Part Type                 | Description                                                                                              |
| -------------------------- | ------------------------- | -------------------------------------------------------------------------------------------------------- |
| "On" LED                   | Output (Light)            | A simple Green LED that indicates whether the board is receiving power or not.  You cannot control this. |
| Micro-B USB Jack           | Data Connection and Power | The connection that allows you to view the contents of the device and monitor it's serial output         |
| Pin 13 LED                 | Output (Light)            | A simple Red LED that you can access and use.  This will also flash when restarting or a fresh bootup.   |
| Connection Pads (14 total) | Input/Output              | These connection pads can be used as both inputs and output in certain cases.                            |
| Flash Memory               | Data Storage              | This is where the contents of the devices are actually stored!                                           |
| ATSAAMD21 Microcontroller  | Microcontroller           | A microcontroller is basically the "brains" of the device.                                               |
| NeoPixels (10 total)       | Output (Light)            | Very versatile LED's that can change color.                                                              |
| Light Sensor               | Input (Light)             | A sensor that measures the amount of light nearby.                                                       |
| Reset Button               | Input                     | A button that when pressed will reset the board.  You do not have any control of this button.            |
| Left and Right Buttons     | Input                     | Simple button that can be determined if pressed or not.                                                  |
| IR Out                     | Output (Infrared Light)   | An Infrared light source that can be used to send Infrared Pulses similar to what remotes do.            |
| IR In                      | Input (Infrared Light)    | An Infrared light detector.                                                                              |
| Motion Sensor              | Input                     | An Accelerometer that detects changes in acceleration, or motion (movement).                             |
| Speaker                    | Output (Audio)            | A small speaker that can play audio ranging from simple tones to complicated `.wav` files.               |
| Slide Switch               | Input                     | A simple switch that toggles from side to side                                                           |
| Microphone                 | Input (Audio)             | A small microphone that can be used to detect certains levels of sound                                   |
| Analog Output (A0 or AO)   | Output                    | A special connection pad that outputs analog voltages                                                    |
| JST Battery Connector      | Power                     | This provides power to the CPX.  When the USB cable is connected, this can or cannot be connected.       |

As you can see, there are a lot of parts that you can access on this board.  As you go through the examples in this repository, you'll be able to learn how to use each of them, and towards the end how to use multiple ones!

## Setting Up Your IDE Environment

I reccomend that you use [vscode](https://code.visualstudio.com/) with the [Microsoft Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) installed.

* Install Python3 (anaconda)
* Viewing the terminal

## How to connect to your CPX Board

TODO: Make this more of a list form and add pictures

Connecting to your CPE board is as simple as plugging it in to the USB port.  Using a USB-A to micro-USB cable, plug the USB-A side into the computer and the micro-USB side into the CPE board.  Once you've done that, the board should appear similar to that of a flash drive with the name "CIRCUITPY".  If this isn't working confirm that you've got the cables properly seated and that the cable you're using is a data cable and not a power only cable.  If it still doesn't work, you may need to re-install Circuit Python (TODO: Add reference to Circuit Python installation).  If you're running a version of Windows before 10, you'll need to install additional drivers.

## The Structure of the Filesystem and `code.py`

TODO: Overview of what is in the filesystem for the CPX and the key elements of `code.py`

## Getting Additional Python Libraries

TODO: I still haven't worked this out.  It needs updating.

In order to get the correct libraries for your specific board, you'll need to inspect the `boot_out.txt` file with the 'CIRCUITPY' volume.  An example output looks like this:

```text
Adafruit CircuitPython 4.0.0-beta.7 on 2019-04-13; Adafruit CircuitPlayground Express with samd21g18
```

Use this to determine which version is installed on the device.  In the case above, 4.x is installed.  Next, navigate to https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases and download the associated version.  In this case it would be `adafruit-circuitpython-bundle-4.x-mpy-YYYYMMDD.zip` where `YYYYMMDD` would be the most recent date release for the 4.x version.

Once you've downloaded that `.zip` file, extract it and look for the `adafruit_circuitplayground` folder, and copy that into the a `lib` folder on your `CIRCUITPY` device.

## Connecting to the serial output

TODO: Add windows example, also add using the adatools extension in vscode

To debug the code on the board itself, you'll need to connect via a serial terminal.  On Mac OS this can be done using `screen`, a built-in tool that allows you to remotely connect to the output of serial connections.  To connect to the board, in a terminal screen on VSCODE enter the following command:

```bash
screen /dev/tty.usbmodem* 115200
```

where `*` is replaced by a series of numbers associated with the board.  If you use the tab completions this should automatically fill in those numbers for you.

## Where to Go Next

Feel free to browse [all the lessons](/) or get started with the first lesson: [RGB Flashing Lights](/1_Light_up_your_world_with_LEDs/rgb_flashing_lights/rgb_flashing_lights.md).

## Common Issues
