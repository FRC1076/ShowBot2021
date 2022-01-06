import math
import time
import wpilib
from shooter import Shooter
from wpilib import interfaces
import rev


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        SHOOTER_ID = 1 # The channel the Spark is on
        
        shooter_controller = rev.CANSparkMax(SHOOTER_ID, rev.CANSparkMaxLowLevel.MotorType.kBrushless)
        self.shooter = Shooter(shooter_controller)
        self.operator = wpilib.XboxController(0)
        
        # Change these depending on the controller
        self.left_trigger_axis = 2 
        self.right_trigger_axis = 5
        print("running!")


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
        if self.operator.getRawAxis(self.right_trigger_axis) > 0.95:
            print("got trigger")
            self.running = 1
        elif self.operator.getRawAxis(self.left_trigger_axis) > 0.95:
            self.running = -0.2
        else:
            self.running = 0 

        if self.operator.getAButton():
            print("got A button!")
            self.shooter_mod = 0.2
        elif self.operator.getBButton():
            self.shooter_mod = 0.4
        elif self.operator.getYButton():
            self.shooter_mod = 0.6
        elif self.operator.getXButton():
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
