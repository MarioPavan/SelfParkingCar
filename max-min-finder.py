#!/usr/bin/python3

from time   import time, sleep
from ev3dev2.motor import LargeMotor,MoveSteering,OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import ColorSensor
# from ev3dev.auto import *

steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
col= ColorSensor()
# col.mode = 'COL-REFLECT'

def run():
  steer_pair.on(steering=0,speed=5)
  max_ref = 0
  min_ref = 100
  end_time = time() + 5
  while time() < end_time:
    read = col.reflected_light_intensity
    if max_ref < read:
      max_ref = read
    if min_ref > read:
      min_ref = read
  steer_pair.off()
  print( 'Max: ' + str(max_ref)) #29,30
  print( 'Min: ' + str(min_ref)) #21,21
  sleep(10)

run()