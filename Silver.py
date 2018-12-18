#!/usr/bin/env python3
from datetime import datetime
from threading import Timer
from time import sleep
import time
import parking

from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.led import Leds
from ev3dev2.motor import LargeMotor,MoveSteering,OUTPUT_B, OUTPUT_C

modified_steering=5
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
us = UltrasonicSensor()
leds = Leds()    

print("running main")
running=True
steer_pair.on(steering=0,speed=15)
count=0
while(running):
    if us.distance_centimeters > 15: # to detect objects closer than 40cm
        # In the above line you can also use inches: us.distance_inches < 16
        leds.set_color('LEFT',  'RED')
        leds.set_color('RIGHT', 'RED')
        count+=1
        if count > 20:
            steer_pair.off()
            running=False
    else:
        count=0
        leds.set_color('LEFT',  'GREEN')
        leds.set_color('RIGHT', 'GREEN')

    sleep (0.1) # Give the CPU a rest

sleep(3)
if not running:
    steer_pair.on_for_degrees(steering=0,speed=15,degrees=160,brake=False,block=True)
    parking.back_parl_park(steer_pair)          
