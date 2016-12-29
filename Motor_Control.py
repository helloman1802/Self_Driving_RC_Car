#!/usr/bin/python

import sys
sys.path.insert(0, '/home/pi/Adafruit-Raspberry-Pi-Python-Code/Adafruit_PWM_Servo_Driver')

from Adafruit_PWM_Servo_Driver import PWM
import time


# Configuration of the car's servo
servoConfig_channel     = 8
servoConfig_frequency 	= 50
servoConfig_resolution 	= 4096
servoConfig_posInit 	= 330
servoConfig_posStraight = 330
servoConfig_posMinLeft 	= 331
servoConfig_posMaxLeft 	= 460
servoConfig_posMinRight = 329
servoConfig_posMaxRight = 215


# Configuration of the car's ESC
escConfig_channel 		= 9
escConfig_frequency 	= 50
escConfig_resolution 	= 4096
escConfig_posInit 		= 335
escConfig_posIdle 		= 335
escConfig_posMinForward	= 357
escConfig_posMaxForward	= 450
escConfig_posMinReverse	= 324
escConfig_posMaxReverse	= 210
escConfig_posHalfForward = 400
escConfig_posHHForward = 374
escConfig_posHalfReverse = 310
escConfig_posHHReverse = 260


# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)


pwm.setPWMFreq(50)             # Set frequency to 60 Hz is brushed ECS
#Brushless ESC is on 100Hz based off of ocilliscople.
# ESC on channel 8
#Servo on channel 7
pwm.setPWM(8, 0, 335)#Idle is 335
pwm.setPWM(7, 0, 215 )
time.sleep(1)

pwm.setPWM(8, 0, escConfig_posHHForward )
pwm.setPWM(7, 0, 460 )
time.sleep(1)

pwm.setPWM(8, 0, escConfig_posHalfForward )
pwm.setPWM(7, 0, 460 )
time.sleep(1)

pwm.setPWM(8, 0, escConfig_posMaxForward )
pwm.setPWM(7, 0, 215 )
time.sleep(3)




pwm.setPWM(8, 0, escConfig_posIdle)
pwm.setPWM(7, 0, 460 )
time.sleep(1)

pwm.setPWM(8, 0, escConfig_posMaxReverse )
pwm.setPWM(7, 0, 215 )
time.sleep(1)


pwm.setPWM(8, 0, escConfig_posIdle)
pwm.setPWM(7, 0, 460 )
time.sleep(1)

pwm.setPWM(8, 0, escConfig_posHalfReverse )
pwm.setPWM(7, 0, 215 )
time.sleep(2)

pwm.setPWM(8, 0, escConfig_posHHReverse )
pwm.setPWM(7, 0, 460 )
time.sleep(2)

pwm.setPWM(8, 0, escConfig_posMaxReverse )
pwm.setPWM(7, 0, 215 )
time.sleep(1)

pwm.setPWM(8, 0, escConfig_posIdle)
pwm.setPWM(7, 0, 330 )
sys.exit("ALL DONE")
