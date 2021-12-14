import math
import time

import wpilib
from wpilib.interfaces import GenericHID
import yaml

from shooter import Shooter


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        with open('config.yaml') as stream:
            config = yaml.load(stream, Loader=yaml.CLoader)

        controller_config = config['Controller']
        channel_config = config['Channels']

        print(controller_config)
        self.LEFT_TRIGGER_AXIS = controller_config['left_trigger_axis']
        self.RIGHT_TRIGGER_AXIS = controller_config['right_trigger_axis']
        self.A_BUTTON_NUM = controller_config['a_button_num']
        self.B_BUTTON_NUM = controller_config['b_button_num']
        self.X_BUTTON_NUM = controller_config['x_button_num']
        self.Y_BUTTON_NUM = controller_config['y_button_num']

        SHOOTER_CHANNEL = channel_config['shooter_channel']
        CONTROLLER_PORT = channel_config['controller_port']

        self.operator = Shooter(SHOOTER_CHANNEL)
        self.controller = GenericHID(CONTROLLER_PORT)

    def robotPeriodic(self):
        pass

    def teleopInit(self):
        self.shooter_mod = 0
        self.running = 0

    def teleopPeriodic(self):
        """
        Makes the motor spin. Right trigger -> 1, left trigger -> -0.2, 
        x reduces the speed, y reduces the speed more, b reduces the speed even more, 
        a reduces the speed the most
        """
        if self.controller.getRawAxis(self.LEFT_TRIGGER_AXIS) > 0.95:
            self.running = -0.2
        elif self.controller.getRawAxis(self.RIGHT_TRIGGER_AXIS) > 0.95:
            self.running = 1
        else:
            self.running = 0 

        if self.controller.getRawButton(self.A_BUTTON_NUM):
            self.shooter_mod = 0.2
        elif self.controller.getRawButton(self.B_BUTTON_NUM):
            self.shooter_mod = 0.4
        elif self.controller.getRawButton(self.Y_BUTTON_NUM):
            self.shooter_mod = 0.6
        elif self.controller.getRawButton(self.X_BUTTON_NUM):
            self.shooter_mod = 0.8
        else:
            self.shooter_mod = 1

        self.operator.set(self.running * self.shooter_mod)

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass


# You do need to include these lines for the code to run
if __name__=="__main__":
    wpilib.run(MyRobot)
