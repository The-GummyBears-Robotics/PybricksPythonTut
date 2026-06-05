from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Drive a square: three ways to write the same behavior.
#
# All three methods should make the robot:
# - drive forward 400 mm
# - turn 90 degrees
# repeated 4 times.
#
# This file is a great example of why loops and functions matter:
# method 1 is repetitive, method 2 is short with a loop, and method 3 is meant
# to be a reusable function (but is unfinished right now).

hub = PrimeHub()

left_motor  = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

# Drive a square (4 sides × 400mm, turn right 90° each corner), method 1

robot.straight(400)
wait(200)
robot.turn(90)
wait(200)

robot.straight(400)
wait(200)
robot.turn(90)
wait(200)

robot.straight(400)
wait(200)
robot.turn(90)
wait(200)

robot.straight(400)
wait(200)
robot.turn(90)
wait(200)


# Drive a square (4 sides × 400mm, turn right 90° each corner), method 2
for i in range(4):
    robot.straight(400)
    wait(200)
    robot.turn(90)
    wait(200)
    
# Drive a square (4 sides × 400mm, turn right 90° each corner), method 3
def drive_square(side_length=400, turn_angle=90):
    for i in range(4):
        robot.straight(side_length)
        wait(200)
        robot.turn(turn_angle)
        wait(200)

drive_square()
