import math
import time
import wpilib
from shooter import Shooter
from wpilib import interfaces


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        SHOOTER_ID = 1

        self.shooter = Shooter(SHOOTER_ID)
        self.controller = wpilib.XboxController(0)
        self.right_hand = wpilib.interfaces.GenericHID.Hand.kRightHand
        self.left_hand = wpilib.interfaces.GenericHID.Hand.kLeftHand

    def robotPeriodic(self):
        pass

    def teleopInit(self):
        self.shooter_mod = 1
        self.running = 0

    def teleopPeriodic(self):

        if self.controller.getTriggerAxis(self.right_hand) > 0.95:
            self.running = 1
        elif self.controller.getTriggerAxis(self.left_hand) > 0.95:
            self.running = -0.2
        else:
            self.running = 0

        if self.controller.getAButton():
            self.shooter_mod = 0.2
        elif self.controller.getBButton():
            self.shooter_mod = 0.4
        elif self.controller.getXButton():
            self.shooter_mod = 0.8
        elif self.controller.getYButton():
            self.shooter_mod = 0.6
        else:
            self.shooter_mod = 1

        self.shooter.set(self.running * self.shooter_mod)

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass
