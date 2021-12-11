import math
import time
import wpilib
from shooter import Shooter
from wpilib import interfaces


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        SHOOTER_ID = 1

        self.shooter = Shooter(1)
        self.controller = wpilib.XboxController(0)
        self.right_hand = wpilib.interfaces.GenericHID.Hand.kRightHand
        self.left_hand = wpilib.interfaces.GenericHID.Hand.kLeftHand

    def robotPeriodic(self):

    def teleopInit(self):
        self.shooter_mod = 1.0
        self.active_button = "None"
        self.running = 0

    def teleopPeriodic(self):

        if controller.getTriggerAxis(kRightHand) > 0.95:
            self.running = 1
        elif controller.getTriggerAxis(kLeftHand)
            self.running = -0.2
        else:
            self.running = 0

        if controller.getAButton():
            self.active_button = 0.2
        elif controller.getBButton():
            self.active_button = 0.4
        elif controller.getXButton():
            self.active_button = 0.8
        elif controller.getYButton():
            self.shooter_mod = 0.6
        else:
            self.shooter_mod = 1

        self.shooter.set(self.running * self.shooter_mod)

    def autonInit(self):

    def autonPeriodic(self):
