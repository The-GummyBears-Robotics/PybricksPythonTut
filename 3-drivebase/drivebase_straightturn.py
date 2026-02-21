# Example 1: Basic Straight & Turn

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()

left_motor  = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

# Drive forward 500mm (half a meter)
robot.straight(500)
wait(300)

# Turn right 90 degrees
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