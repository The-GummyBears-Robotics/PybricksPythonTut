# Turn the hub LED on/off using a loop.
#
# This is a great “first loop” program:
# - repeat 5 times
# - turn red ON, wait
# - turn OFF, wait
#
# Try it:
# - change the number of repeats (5)
# - try other colors (GREEN/BLUE)
# - change the wait times (milliseconds)

from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.tools import wait

# Initialize the hub.
hub = PrimeHub()

# Turn the light on and off 5 times.
for i in range(5):

    # LED on (solid color).
    hub.light.on(Color.RED)
    wait(1000)

    # LED off.
    hub.light.off()
    wait(500)