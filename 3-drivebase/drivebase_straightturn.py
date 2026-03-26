# Example: Basic straight driving and turning with DriveBase.
#
# DriveBase is a helper that uses TWO motors as a “robot”.
# The two most important numbers are your robot’s geometry (in millimeters):
# - wheel_diameter: your wheel size
# - axle_track: distance between the left and right wheels
#
# If these are wrong, the robot will overshoot/undershoot distances and turns.

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()

left_motor  = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

# Straight distances are in millimeters.
# Positive = forward, negative = backward.
robot.straight(500)
wait(300)

# Turns are in degrees.
# Positive/negative depends on motor directions, but in this file:
# positive = right, negative = left (see the last turn).
robot.turn(90)
wait(300)

# Drive forward another 300mm
robot.straight(300)
wait(300)

# Turn left 90 degrees (negative = left)
robot.turn(-90)
wait(300)

# Drive backward 200mm (negative = backward)
robot.straight(-200)