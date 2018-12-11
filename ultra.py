#!/usr/bin/env python3
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.led import Leds
from time import sleep

us = UltrasonicSensor()
leds = Leds()

leds.all_off() # stop the LEDs flashing (as well as turn them off)

if us.distance_centimeters < 10: # to detect objects closer than 40cm
    # In the above line you can also use inches: us.distance_inches < 16
    leds.set_color('LEFT',  'RED')
    leds.set_color('RIGHT', 'RED')
else:
    leds.set_color('LEFT',  'GREEN')
    leds.set_color('RIGHT', 'GREEN')

sleep (0.01) # Give the CPU a rest
