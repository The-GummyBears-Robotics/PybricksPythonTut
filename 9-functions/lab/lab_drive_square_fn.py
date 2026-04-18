# Lab A — drive a square using ONE function (~15–20 min)
#
# Box bot: left motor on A, right on B (same idea as 3-drivebase/).
# Goal: write one_side(robot) so each call = one edge + one 90° turn.
# Then run it four times (teacher: square = 4 identical corners).
#
# Stretch: add parameter edge_mm so the square can change size.

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)


def one_side(robot):
    """Drive one side of the square: straight, then turn 90°."""
    robot.straight(300)
    wait(150)
    robot.turn(90)
    wait(150)


# Drive a full square
for _ in range(4):
    one_side(robot)

hub.speaker.beep(600, 200)
