from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()

left_motor  = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

# Reading what the robot thinks it did.
#
# DriveBase tracks:
# - `distance()` in mm (how far it has driven)
# - `angle()` in degrees (how much it has turned)
#
# `reset()` sets both back to 0. This is useful before a mission step so
# you can measure movement from a known starting point.
robot.reset()  # Reset distance and angle to 0

# Drive and then print out the measured distance/angle.
robot.straight(500)
print("Distance driven:", robot.distance(), "mm")
print("Current angle:  ", robot.angle(), "degrees")

robot.turn(90)
print("After turn, angle:", robot.angle(), "degrees")