#!/usr/bin/env python3
from ev3dev.ev3 import *
import os
os.system('setfont Lat15-TerminusBold14')
mL = LargeMotor('outB'); mL.stop_action = 'hold'
mR = LargeMotor('outC'); mR.stop_action = 'hold'
# print('Hello, my name is EV3!')
Sound.speak('Son of biscuit!! Idiot').wait()
mL.run_to_rel_pos(position_sp= 840, speed_sp = 250)
mR.run_to_rel_pos(position_sp=-840, speed_sp = 250)
mL.wait_while('running')
mR.wait_while('running')