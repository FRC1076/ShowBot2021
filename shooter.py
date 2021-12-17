import wpilib


class Shooter:
    def __init__(self, motor_controller, channel):
        self.shooter = motor_controller(channel)

    def set(self, value) -> None:
        self.shooter.set(value)
