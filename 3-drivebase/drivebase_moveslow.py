from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

# Slow, gentle settings for precision.
#
# Slower speeds + gentler acceleration often give more consistent missions,
# especially on FLL mats where wheels can slip.
robot.settings(
    straight_speed=100,        # slow forward speed
    straight_acceleration=50,  # gentle acceleration
    turn_rate=45,              # slow turning
    turn_acceleration=30       # gentle turn acceleration
)

# A careful “course” with waits between moves.
robot.straight(200)
wait(500)
robot.turn(90)
wait(500)
robot.straight(150)