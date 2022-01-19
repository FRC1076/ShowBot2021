#
# See the documentation for more details on how this works
#
# The idea here is you provide a simulation object that overrides specific
# pieces of WPILib, and modifies motors/sensors accordingly depending on the
# state of the simulation. An example of this would be measuring a motor
# moving for a set period of time, and then changing a limit switch to turn
# on after that period of time. This can help you do more complex simulations
# of your robot code without too much extra effort.
#

import wpilib.simulation

from pyfrc.physics.core import PhysicsInterface
from pyfrc.physics import motor_cfgs, tankmodel
from pyfrc.physics.units import units

import rev
import robotmap


class PhysicsEngine:
    """
    Simulates a motor moving something that strikes two limit switches,
    one on each end of the track. Obviously, this is not particularly
    realistic, but it's good enough to illustrate the point
    """

    def __init__(self, physics_controller: PhysicsInterface):

        self.physics_controller = physics_controller

        # Motors
        self.l_motor = wpilib.simulation.SimDeviceSim("LEFT", robotmap.RIGHT_MIDDLE_ID)
        self.r_motor = wpilib.simulation.SimDeviceSim("RIGHT", robotmap.LEFT_MIDDLE_ID)

        self.dio1 = wpilib.simulation.DIOSim(1)
        self.dio2 = wpilib.simulation.DIOSim(2)
        self.ain2 = wpilib.simulation.AnalogInputSim(2)

        self.motor = wpilib.simulation.PWMSim(4)

        # Gyro
        self.gyro = wpilib.simulation.AnalogGyroSim(1)

        self.position = 0

        # Change these parameters to fit your robot!
        bumper_width = 3.25 * units.inch


        # fmt: off
        self.drivetrain = tankmodel.TankModel.theory(
            motor_cfgs.MOTOR_CFG_CIM,           # motor configuration
            110 * units.lbs,                    # robot mass
            10.71,                              # drivetrain gear ratio
            2,                                  # motors per side
            22 * units.inch,                    # robot wheelbase
            23 * units.inch + bumper_width * 2, # robot width
            32 * units.inch + bumper_width * 2, # robot length
            6 * units.inch,                     # wheel diameter
        )
        # fmt: on

    def update_sim(self, now: float, tm_diff: float) -> None:
        """
        Called when the simulation parameters for the program need to be
        updated.

        :param now: The current time as a float
        :param tm_diff: The amount of time that has passed since the last
                        time that this function was called
        """

        # Simulate the drivetrain
        left_motor_speed = self.l_motor.getDouble("Velocity").get()       
        right_motor_speed = self.r_motor.getDouble("Velocity").get()

        # print(left_motor_speed, right_motor_speed)
            
        transform = self.drivetrain.calculate(left_motor_speed, right_motor_speed, tm_diff)
        pose = self.physics_controller.move_robot(transform)

        # print(pose)

        # update position (use tm_diff so the rate is constant)
        self.position += self.motor.getSpeed() * tm_diff * 3

