# Example 4: Read Motor Angle
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

hub = PrimeHub()

motor = Motor(Port.A)

# Reset angle to zero
motor.reset_angle(0)

# Run and print angle every 200ms
motor.run(300)

for _ in range(10):
    print("Angle:", motor.angle(), "degrees")
    wait(200)

motor.stop()
print("Final angle:", motor.angle(), "degrees")