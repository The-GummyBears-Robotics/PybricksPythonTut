# Example: Run a motor continuously (forward and backward).
#
# Important units:
# - motor speed is in degrees/second (deg/s)
# - wait times are in milliseconds (ms)
#
# Tip: If "forward" is backwards on your robot, you can flip the motor direction
# (see other examples using `positive_direction=...`).
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

hub = PrimeHub()

# Connect motor to Port A
motor = Motor(Port.A)

# Run forward at 500 degrees/second.
motor.run(500)
wait(2000)    # run for 2 seconds

# Stop the motor (default stop is "coast").
motor.stop()
wait(500)

# Run backward (negative speed).
motor.run(-500)
wait(2000)

motor.stop()