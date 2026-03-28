# Example: Read motor angle while it spins.
#
# `motor.angle()` returns degrees since the last reset (or since power-on).
# This is how you can measure movement for arms, wheels, and mechanisms.
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

hub = PrimeHub()

motor = Motor(Port.A)

# Reset angle to zero so our printout starts at 0.
motor.reset_angle(0)

# Run and print angle every 200 ms (milliseconds).
motor.run(300)

for _ in range(10):
    print("Angle:", motor.angle(), "degrees")
    wait(200)

motor.stop()
print("Final angle:", motor.angle(), "degrees")