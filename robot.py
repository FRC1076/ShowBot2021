import math
import time
import wpilib
from shooter import Shooter
from wpilib import interfaces


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        SHOOTER_ID = 1 # The channel the Spark is on

        self.shooter = Shooter(SHOOTER_ID)
        self.controller = wpilib.XboxController(0)
        # self.right_hand = wpilib.interfaces.GenericHID.Hand.kRightHand
        # self.left_hand = wpilib.interfaces.GenericHID.Hand.kLeftHand

        # Change these depending on the controller
        self.left_trigger_axis = 2 
        self.right_trigger_axis = 5

    def robotPeriodic(self):
        pass

    def teleopInit(self):
        self.shooter_mod = 1
        self.running = 0

    def teleopPeriodic(self):
        """
        Makes the motor spin. Right trigger -> 1, left trigger -> -0.2, 
        x reduces the speed, y reduces the speed more, b reduces the speed even more, 
        a reduces the speed the most
        """
        if self.controller.getRawAxis(self.right_trigger_axis) > 0.95:
            self.running = 1
        elif self.controller.getRawAxis(self.left_trigger_axis) > 0.95:
            self.running = -0.2
        else:
            self.running = 0 

        if self.controller.getAButton():
            self.shooter_mod = 0.2
        elif self.controller.getBButton():
            self.shooter_mod = 0.4
        elif self.controller.getYButton():
            self.shooter_mod = 0.6
        elif self.controller.getXButton():
            self.shooter_mod = 0.8
        else:
            self.shooter_mod = 1

        self.shooter.set(self.running * self.shooter_mod)

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass


# You do need to include these lines for the code to run
if __name__=="__main__":
    wpilib.run(MyRobot)
