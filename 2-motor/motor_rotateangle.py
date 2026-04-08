# Example: Rotate by a specific angle.
#
# `run_angle(speed, angle_deg)` rotates a RELATIVE amount:
# - 360 degrees = one full turn
# - negative angle goes the other way
#
# If you need to go to an exact “position”, look for `run_target(...)` examples.
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

hub = PrimeHub()

motor = Motor(Port.A)

# Rotate 360 degrees forward (one full turn)
motor.run_angle(300, 360)
wait(500)

# Rotate 180 degrees backward
motor.run_angle(300, -180)
wait(500)

# Rotate with custom positive direction
motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
motor.run_angle(300, 90)   # 90 deg counterclockwise