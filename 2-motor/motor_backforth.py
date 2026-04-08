# Making the motor move back and forth.
#
# This is the simplest way to show direction:
# - positive speed spins one way
# - negative speed spins the other way
#
# Tip: the physical direction depends on how the motor is mounted.

from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize a motor on port A.
example_motor = Motor(Port.A)

# Make the motor run clockwise at 500 degrees per second.
example_motor.run(500)

# Wait for three seconds.
wait(3000)

# Make the motor run counterclockwise at 500 degrees per second.
example_motor.run(-500)

# Wait for three seconds.
wait(3000)