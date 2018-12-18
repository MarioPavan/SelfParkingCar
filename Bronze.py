#!/usr/bin/python3
from time   import time, sleep
from ev3dev2.motor import LargeMotor,MoveSteering,OUTPUT_B, OUTPUT_C
import parking
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
parking.back_parl_park_bronze(steer_pair)