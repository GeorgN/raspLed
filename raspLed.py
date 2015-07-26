#!/usr/bin/env /usr/bin/python
# -*- coding: utf-8 -*-

#
# Copyright 2015 Franc Rodriguez.
#
    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this program. If not, see <http://www.gnu.org/licenses/>. 


# Description: Manage Led RGB

import RPi.GPIO as GPIO
import os
import sys
import getopt

# Pins LED
red = 22
green = 23
blue = 24

# GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Establecer modo pins
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

# Desactivar color
GPIO.output(red, 0)
GPIO.output(green, 0)
GPIO.output(blue, 0)

def main(argv):
    color = ""
    try:
        opts, args = getopt.getopt(argv,"hc:",["color="])
        if not opts:
            print "raspLed.py -c <red,green,blue,off>"
            sys.exit(2)
    except getopt.GetoptError:
         print "raspLed.py -c <red,green,blue,off>"
         sys.exit(2)
    for opt, arg in opts:
         if opt == "-h":
             print "raspLed.py -c <red,green,blue,off>"
             sys.exit()
         elif opt in ("-c", "--color"):
             color = arg

    if arg == 'red':
        GPIO.output(red, 1)
    elif arg == 'green':
        GPIO.output(green, 1)
    elif arg == 'blue':
        GPIO.output(blue, 1)
    elif arg == 'off':
        GPIO.output(blue, 0)
        GPIO.output(red, 0)
        GPIO.output(green, 0)

if __name__ == "__main__":
   main(sys.argv[1:])
