import Adafruit_PCA9685
import time
import os
import pprint
import pygame
from time import sleep
pwm = Adafruit_PCA9685.PCA9685()

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

class PS4Controller(object):
    """Class representing the PS4 controller. Pretty straightforward functionality."""

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
                                if i == 7:
                                    print("Right Trigger Pressed...")


                            else:
                                pass
                        button_value(i)






                elif event.type == pygame.JOYBUTTONUP:
                    self.button_data[event.button] = False
                    print ("Buttons Released...")
                    print("\n...")
                elif event.type == pygame.JOYHATMOTION:
                    self.hat_data[event.hat] = event.value
                    #print(self.hat_data)








if __name__ == "__main__":
    ps4 = PS4Controller()
    ps4.init()
    ps4.listen()
