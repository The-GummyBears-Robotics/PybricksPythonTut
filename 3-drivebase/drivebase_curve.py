from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()

left_motor  = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

# Drive a curve: radius=200mm, sweep 90 degrees to the right
robot.curve(radius=200, angle=90)
wait(300)

# Drive a curve to the left (negative radius)
robot.curve(radius=-200, angle=90)
wait(300)

# Full circle: radius=150mm, 360 degrees
robot.curve(radius=150, angle=360)