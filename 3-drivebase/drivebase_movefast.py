from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase

hub = PrimeHub()

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

# Fast, aggressive settings for speed
robot.settings(
    straight_speed=500,         # fast forward speed
    straight_acceleration=300,  # quick acceleration
    turn_rate=200,              # fast turning
    turn_acceleration=150       # quick turn start
)

# Race through a course
robot.straight(600)
robot.turn(90)
robot.straight(400)
robot.turn(90)
robot.straight(600)