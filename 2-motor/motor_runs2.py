# Example 1: Run Motor Continuously
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

hub = PrimeHub()

# Connect motor to Port A
motor = Motor(Port.A)

# Run forward at 500 degrees/second
motor.run(500)
wait(2000)    # run for 2 seconds

# Stop the motor
motor.stop()
wait(500)

# Run backward (negative speed)
motor.run(-500)
wait(2000)

motor.stop()