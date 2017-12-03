import Adafruit_PCA9685
import time
import os
import pprint
import pygame
from time import sleep
from Adafruit_PWM_Servo_Driver import PWM
#pwm = Adafruit_PCA9685.PCA9685()
pwm = PWM(0x40)

# PWM setup
def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

# Configuration of the car's servo
servoConfig_channel     = 8
servoConfig_frequency 	= 50
servoConfig_resolution 	= 4096
servoConfig_posInit 	= 330
servoConfig_posStraight = 400
servoConfig_posMinLeft 	= 331
servoConfig_posMaxLeft 	= 600
servoConfig_posMinRight = 329
servoConfig_posMaxRight = 150


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
escConfig_posHHReverse = 200

class PS4Controller(object):
    """Class representing the PS4 controller. Pretty straightforward functionality."""

    #pwm.setPWM(7, 0, servoConfig_posStraight)
    controller = None
    axis_data = None
    button_data = None
    hat_data = None

    def init(self):
        """Initialize the joystick components"""

        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

    def listen(self):
        """Listen for events to happen"""

        if not self.axis_data:
            self.axis_data = {}

        if not self.button_data:
            self.button_data = {}
            for i in range(self.controller.get_numbuttons()):
                self.button_data[i] = False

        if not self.hat_data:
            self.hat_data = {}
            for i in range(self.controller.get_numhats()):
                self.hat_data[i] = (0, 0)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    self.axis_data[event.axis] = round(event.value,2)
                    #print(self.axis_data)

                    for key, value in self.axis_data.items() :
                        #print('{} : {}'.format(key, value))

                        if key == 0:

                            if value < 0:
                                pwm.setPWM(7, 0, servoConfig_posMaxLeft)
                                print(value)

                            elif value > 0:
                                pwm.setPWM(7, 0, servoConfig_posMaxRight)
                                print(value)

                            elif value == 0:
                                pwm.setPWM(7, 0, servoConfig_posStraight)








                """Finds the value of all of the buttons on the controller and adds them to a list"""
                button_values = []
                n = 0
                if event.type == pygame.JOYBUTTONDOWN:
                    self.button_data[event.button] = True

                    for i in self.button_data:
                        def button_value(num):
                            if self.button_data[num] == 1:
                                print("Button ID: %s") %(num)
                                if i == 0:
                                    print("Square Pressed...")
                                if i == 1:
                                    print("X Pressed...")
                                    pwm.setPWM(8, 0, escConfig_posIdle)
                                if i == 2:
                                    print("Circle Pressed...")
                                if i == 3:
                                    print("Triangle Pressed...")
                                if i == 4:
                                    print("Left Bumper Pressed...")
                                if i == 5:
                                    print("Right Bumper Pressed...")
                                if i == 6:
                                    print("Left Trigger Pressed...")
                                    pwm.setPWM(8, 0, escConfig_posHHReverse)
                                if i == 7:
                                    print("Right Trigger Pressed...")
                                    pwm.setPWM(8, 0, escConfig_posHHForward)



                            else:
                                pass
                        button_value(i)






                elif event.type == pygame.JOYBUTTONUP:
                    self.button_data[event.button] = False
                    print ("Buttons Released...")
                    print("\n...")
                    pwm.setPWM(8, 0, escConfig_posIdle)

                elif event.type == pygame.JOYHATMOTION:
                    self.hat_data[event.hat] = event.value
                    #print(self.hat_data)








if __name__ == "__main__":
    ps4 = PS4Controller()
    ps4.init()
    ps4.listen()
