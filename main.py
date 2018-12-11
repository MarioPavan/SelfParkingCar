#!/usr/bin/env python3
from datetime import datetime
from threading import Timer
from time import sleep
import time

from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.led import Leds
from ev3dev2.motor import LargeMotor,MoveSteering,OUTPUT_B, OUTPUT_C

import motor

modified_steering=5
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
us = UltrasonicSensor()
leds = Leds()    

if __name__ == '__main__':

    running=True
    steer_pair.on(steering=0,speed=15,brake=False,block=True)

    while(running):
        if us.distance_centimeters < 5: # to detect objects closer than 40cm
            # In the above line you can also use inches: us.distance_inches < 16
            leds.set_color('LEFT',  'RED')
            leds.set_color('RIGHT', 'RED')
            steer_pair.off()
            steer_pair.on_for_degrees(steering=0,speed=15,degrees=150,brake=False,block=True)
            motor.parl_park(steer_pair)
        else:
            leds.set_color('LEFT',  'GREEN')
            leds.set_color('RIGHT', 'GREEN')

        sleep (0.01) # Give the CPU a rest
            

    # back_parl_park(steer_pair)