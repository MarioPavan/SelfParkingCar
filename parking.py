#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor,MoveSteering,OUTPUT_B, OUTPUT_C
from time import sleep

# speed=40
# degrees=600

# modified_steering=5

# steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
# tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)

def go_and_turn(steer_pair):
    steer_pair.on_for_rotations(steering=0,speed=40,rotations=4,brake=False,block=True)
    steer_pair.on_for_degrees(steering=-40,speed=30,degrees=500,brake=False,block=True)
    steer_pair.on_for_degrees(steering=0,speed=30,degrees=100,brake=False,block=True)
    steer_pair.on_for_degrees(steering=-32,speed=30,degrees=500,brake=False,block=True)
    steer_pair.on_for_rotations(steering=-2,speed=25,rotations=2,brake=True,block=True)
    sleep(3)


def parl_park(steer_pair):
    park_steer=40
    steer_speed=25
    steer_degrees=300

    steer_pair.on_for_degrees(steering=park_steer,speed=steer_speed,degrees=steer_degrees,brake=False,block=True)
    steer_pair.on_for_degrees(steering=10,speed=15,degrees=190,brake=False,block=True)
    steer_pair.on_for_degrees(steering=0,speed=15,degrees=150,brake=False,block=True)
    steer_pair.on_for_degrees(steering=-park_steer-10,speed=steer_speed,degrees=steer_degrees,brake=False,block=True)
    steer_pair.on_for_degrees(steering=0,speed=-15,degrees=30,brake=False,block=True)

def back_parl_park(steer_pair):
    park_steer=36.3
    steer_speed=25
    steer_degrees=85
    steer_pair.on_for_degrees(steering=park_steer,speed=-steer_speed,degrees=steer_degrees,brake=False,block=True)
    steer_pair.on_for_degrees(steering=10,speed=-15,degrees=250,brake=False,block=True)
    # steer_pair.on_for_degrees(steering=0,speed=-15,degrees=160,brake=False,block=True)
    steer_pair.on_for_degrees(steering=-park_steer,speed=-steer_speed,degrees=55,brake=False,block=True)
    steer_pair.on_for_degrees(steering=20,speed=15,degrees=200,brake=False,block=True)
    steer_pair.on_for_degrees(steering=-15,speed=-15,degrees=80,brake=False,block=True)

def back_parl_park_bronze(steer_pair):
    park_steer=36.3
    steer_speed=25
    steer_degrees=100
    steer_pair.on_for_degrees(steering=park_steer,speed=-steer_speed,degrees=steer_degrees,brake=False,block=True)
    steer_pair.on_for_degrees(steering=10,speed=-15,degrees=230,brake=False,block=True)
    # steer_pair.on_for_degrees(steering=0,speed=-15,degrees=160,brake=False,block=True)
    steer_pair.on_for_degrees(steering=-park_steer,speed=-steer_speed,degrees=70,brake=False,block=True)
    steer_pair.on_for_degrees(steering=15,speed=15,degrees=190,brake=False,block=True)
    steer_pair.on_for_degrees(steering=-15,speed=-15,degrees=100,brake=False,block=True)    


