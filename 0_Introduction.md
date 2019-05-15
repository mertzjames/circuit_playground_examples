# Introduction

Welcome to your new Circuit Python Express (CPE)

## How to connect to your CPE Board

Connecting to your CPE board is as simple as plugging it in to the USB port.  Using a USB-A to micro-USB cable, plug the USB-A side into the computer and the micro-USB side into the CPE board.  Once you've done that, the board should appear similar to that of a flash drive with the name "CIRCUITPY".  If this isn't working confirm that you've got the cables properly seated and that the cable you're using is a data cable and not a power only cable.  If it still doesn't work, you may need to re-install Circuit Python.  If you're running a version of Windows before 10, you'll need to install additional drivers.

## Getting the Python Libraries

In order to get the correct libraries for your specific board, you'll need to inspect the `boot_out.txt` file with the 'CIRCUITPY' volume.  An example output looks like this:

```
Adafruit CircuitPython 4.0.0-beta.7 on 2019-04-13; Adafruit CircuitPlayground Express with samd21g18
```

Use this to determine which version is installed on the device.  In the case above, 4.x is installed.  Next, navigate to https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases and download the associated version.  In this case it would be `adafruit-circuitpython-bundle-4.x-mpy-YYYYMMDD.zip` where `YYYYMMDD` would be the most recent date release for the 4.x version.

Once you've downloaded that `.zip` file, you can extract it and then use that to reference your Python libs.

## Connecting to the serial output

To debug the code on the board itself, you'll need to connect via a serial terminal.  On Mac OS this can be done using `screen`, a built-in tool that allows you to remotely connect to the output of serial connections.  To connect to the board, in a terminal screen on VSCODE enter the following command:

```
screen /dev/tty.usbmodem* 115200
```

where `*` is replaced by a series of numbers associated with the board.  If you use the tab completions this should automatically fill in those numbers for you.
