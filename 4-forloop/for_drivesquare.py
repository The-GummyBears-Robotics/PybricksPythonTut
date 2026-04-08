from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

# Drive a square using a loop.
#
# `range(4)` repeats the same straight+turn 4 times:
# - side 0
# - side 1
# - side 2
# - side 3
#
# Even though we don't use `side` in the commands, it’s useful for debugging:
# you can print it, or show it on the display to see which side you're on.
for side in range(4):
    robot.straight(400)   # drive forward 400mm
    wait(200)
    robot.turn(90)        # turn right 90 degrees
    wait(200)