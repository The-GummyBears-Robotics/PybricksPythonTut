from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Different ways to stop a motor.
#
# After running, you can stop in multiple ways:
# - `stop()` or `coast`: let it spin down freely (smooth, but less precise)
# - `brake()`: stop quickly (good for quick stops)
# - `hold()`: stop and actively hold position (best for arms)
# - `run(0)`: also stops, but you normally use the methods above
#
# Try it: run the motor with a wheel attached and feel the difference.

# Initialize a motor on port A.
example_motor = Motor(Port.A)

# Run at 500 deg/s and then stop by coasting.
example_motor.run(500)
wait(1500)
example_motor.stop()
wait(1500)

# Run at 500 deg/s and then stop by braking.
example_motor.run(500)
wait(1500)
example_motor.brake()
wait(1500)

# Run at 500 deg/s and then stop by holding.
example_motor.run(500)
wait(1500)
example_motor.hold()
wait(1500)

# Run at 500 deg/s and then stop by running at 0 speed.
example_motor.run(500)
wait(1500)
example_motor.run(0)
wait(1500)