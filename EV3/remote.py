#!/usr/bin/env python3
# the 'shebang' above is included so that the program
# can be launched in Python3 from within Brickman

# -----------------------------------------------------------------------------
# Copyright (c) 2015 Denis Demidov <dennis.demidov@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# -----------------------------------------------------------------------------

# This demo shows how to remote control an Explor3r robot
#
# Red buttons control left motor, blue buttons control right motor.
# Leds are used to indicate movement direction.

from time import sleep
from ev3dev.ev3 import *

# Connect two large motors on output ports B and C
lmotor = LargeMotor('outB')
rmotor = LargeMotor('outC')

# Connect remote control
rc = RemoteControl()

# Initialize button handler
# button = Button()   # not working so disabled

# Turn leds off
Leds.all_off()

def roll(motor, led_group, direction):
    """
    Generate remote control event handler. It rolls given motor into given
    direction (1 for forward, -1 for backward). When motor rolls forward, the
    given led group flashes green, when backward -- red. When motor stops, the
    leds are turned off.

    The on_press function has signature required by RemoteControl class.
    It takes boolean state parameter; True when button is pressed, False
    otherwise.
    """
    def on_press(state):
        if state:
            # Roll when button is pressed
            motor.run_forever(speed_sp=90*direction)
            Leds.set_color(led_group, direction > 0 and Leds.GREEN or Leds.RED)
        else:
            # Stop otherwise
            motor.stop(stop_action='brake')
            Leds.set(led_group, brightness_pct=0)

    return on_press

# Assign event handler to each of the remote buttons
rc.on_red_up    = roll(lmotor, Leds.LEFT,   1)
rc.on_red_down  = roll(lmotor, Leds.LEFT,  -1)
rc.on_blue_up   = roll(rmotor, Leds.RIGHT,  1)
rc.on_blue_down = roll(rmotor, Leds.RIGHT, -1)

# Enter event processing loop
#while not button.any():   #not working so commented out
while True:   #replaces previous line so use Ctrl-C to exit
    rc.process()
    sleep(0.01)
    
# Press Ctrl-C to exit