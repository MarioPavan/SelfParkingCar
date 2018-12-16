#!/usr/bin/python3
from ev3dev2.sensor.lego import UltrasonicSensor
from time   import time, sleep
from ev3dev2.motor import LargeMotor,MoveSteering,OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button
from ev3dev2.led import Leds
import parking

power = 30 # Maximum power on any of the motors in percent.
minRef = 3 #from line
maxRef = 30 #from board
target = 4 #edge of line
# Finding the appropriate gain parameters can be difficult. 
# You can start with kp=1 and kd=ki=0.
# Increase power and test again.
kp = float(1) #Progressively reduce Kp by 0.05 until the robot follows a staight line with no or litte side to side movement. 
kd = 0 # Test with a curved line and increase kd by 1 untill it can follow the entire path. 
ki = float(0.0)# Progressively increase Ki by 0.01 until the robot follows the edge of a straight line with no oscillation. 
direction = 1


left_motor = LargeMotor(OUTPUT_B)
right_motor = LargeMotor(OUTPUT_C)
col= ColorSensor()
us = UltrasonicSensor()
btn = Button()
leds = Leds()  

def steering2(course, power):
    if course >= 0:
        if course > 100:
            power_right = 0
            power_left = power
        else:	
            power_left = power
            power_right = power - ((power * course) / 100)
    else:
        if course < -100:
            power_left = 0
            power_right = power
        else:
            power_right = power
            power_left = power + ((power * course) / 100)
    return (int(power_left), int(power_right))


def freeSpot(free_count,isFree):
    if us.distance_centimeters > 15: # to detect objects closer than 40cm
        # In the above line you can also use inches: us.distance_inches < 16
        leds.set_color('LEFT',  'RED')
        leds.set_color('RIGHT', 'RED')
        free_count+=1
        if free_count > 40:
            isFree=True
    else:
        free_count=0
        leds.set_color('LEFT',  'GREEN')
        leds.set_color('RIGHT', 'GREEN')
    return free_count,isFree

def run(power, target, kp, kd, ki, direction, minRef, maxRef):
    lastError = error = integral = 0
    left_motor.run_direct()
    right_motor.run_direct()

    free_count=0
    isFree=False

    while not btn.any() and not isFree:
        # if ts.value():
        # 	print ('Breaking loop') # User pressed touch sensor
        # 	break
        refRead = col.value()
        error = target - (100 * ( refRead - minRef ) / ( maxRef - minRef ))
        derivative = error - lastError
        lastError = error
        integral = float(0.5) * integral + error
        course = (kp * error + kd * derivative +ki * integral) * direction
        for (motor, pow) in zip((left_motor, right_motor), steering2(course, power)):
            motor.duty_cycle_sp = pow
        free_count,isFree=freeSpot(free_count,isFree)
        sleep(0.01) # Aprox 100Hz
    
    left_motor.stop()
    right_motor.stop()

    sleep(2)
    steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
    steer_pair.on_for_degrees(steering=0,speed=15,degrees=200,brake=False,block=True)
    parking.back_parl_park(steer_pair)
        


run(power, target, kp, kd, ki, direction, minRef, maxRef)

print ('Stopping motors')

