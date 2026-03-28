from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()
left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right = Motor(Port.B)
robot = DriveBase(left, right, wheel_diameter=56, axle_track=112)

# Gyro-assisted straight driving.
#
# `use_gyro(True)` tells DriveBase to use the IMU heading for better straightness.
# Usually this improves repeatability vs wheel-only correction.

# Enable gyro for better accuracy.
robot.use_gyro(True)

hub.display.text("GYRO ON")
wait(2000)

# Drive straight 1000mm
hub.light.on(Color.GREEN)
robot.straight(1000)

# Done
hub.light.on(Color.BLUE)
hub.display.text("DONE")