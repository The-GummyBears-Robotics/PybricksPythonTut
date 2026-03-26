from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Icon
from pybricks.tools import wait

hub = PrimeHub()

motor = Motor(Port.A)

# Detecting a stall using a `while` loop.
#
# A stall happens when the motor is trying to move but can't (hits an end stop).
# There are different ways to detect a stall; this file uses:
# - `motor.speed() == 0` (it has stopped moving)
# - `motor.control.done()` (the controller thinks the command is finished)
#
# Try it safely: keep the speed low so you don't damage a mechanism.

# Run motor until it hits something (stalls).
motor.run(300)
hub.display.icon(Icon.ARROW_RIGHT)

while True:
    # Check if motor has stalled
    if motor.speed() == 0 and motor.control.done():
        break
    wait(10)

motor.stop()
hub.display.icon(Icon.ANGRY)
hub.speaker.beep(frequency=800, duration=500)
print("Motor stalled!")