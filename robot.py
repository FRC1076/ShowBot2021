import math
import time
import wpilib
from shooter import Shooter


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        CONTROLLER_PORT = 0  # Port the controller is connected to, usually 0
        SHOOTER_CHANNEL = 1  # The channel the motor controller is on
        SHOOTER_CONTROLLER = wpilib.Spark  # The motor controller we're using
        
        self.shooter = Shooter(SHOOTER_CONTROLLER, SHOOTER_CHANNEL)
        self.controller = wpilib.XboxController(CONTROLLER_PORT)

        # Change these depending on the controller
        self.LEFT_TRIGGER_AXIS = 2
        self.RIGHT_TRIGGER_AXIS = 5

    def robotPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        """ Makes the motor spin

        Gets input from a controller and interprets it as follows:
        Right trigger -> full speed forwards, left trigger -> a fifth of the speed backwards
        This input can then be modified by pressing buttons as follows:
        x reduces the speed, y reduces the speed more, b reduces the speed even more, a reduces the speed the most
        """

        if self.controller.getRawAxis(self.LEFT_TRIGGER_AXIS) > 0.95:
            self.running = -0.2
        elif self.controller.getRawAxis(self.RIGHT_TRIGGER_AXIS) > 0.95:
            self.running = 1
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


if __name__ == "__main__":
    wpilib.run(MyRobot)
