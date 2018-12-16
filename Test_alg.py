#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor,MoveSteering,OUTPUT_B, OUTPUT_C
from time import sleep

# speed=40
# degrees=600

modified_steering=5

steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
# tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)

def ltest(steer_pair):
    steer_pair.on_for_rotations(steering=0,speed=30,rotations=2,brake=False,block=True)
    steer_pair.on_for_rotations(steering=-50,speed=30,rotations=1.2,brake=False,block=True)
    steer_pair.on_for_rotations(steering=0,speed=30,rotations=2,brake=False,block=True)
    steer_pair.on_for_rotations(steering=-50,speed=30,rotations=1.2,brake=False,block=True)
    steer_pair.on_for_rotations(steering=0,speed=30,rotations=2,brake=False,block=True)
    steer_pair.on_for_rotations(steering=-50,speed=30,rotations=1.2,brake=False,block=True)
    steer_pair.on_for_rotations(steering=0,speed=30,rotations=2,brake=False,block=True)
    steer_pair.on_for_rotations(steering=-50,speed=30,rotations=1.15,brake=False,block=True)

def rtest(steer_pair):
    steer_pair.on_for_rotations(steering=0,speed=30,rotations=6,brake=False,block=True)
    #steer_pair.on_for_rotations(steering=50,speed=30,rotations=1.25,brake=False,block=True)
    #steer_pair.on_for_rotations(steering=0,speed=30,rotations=2,brake=False,block=True)
    #steer_pair.on_for_rotations(steering=50,speed=30,rotations=1.25,brake=False,block=True)
    #steer_pair.on_for_rotations(steering=0,speed=30,rotations=2,brake=False,block=True)
    #steer_pair.on_for_rotations(steering=50,speed=30,rotations=1.25,brake=False,block=True)
    #steer_pair.on_for_rotations(steering=0,speed=30,rotations=2,brake=False,block=True)
    #steer_pair.on_for_rotations(steering=50,speed=30,rotations=1.1,brake=False,block=True)
    #steer_pair.on_for_rotations(steering=0,speed=40,rotations=4,brake=False,block=True)
sleep(3)
    
#ltest(steer_pair)
rtest(steer_pair)   
