from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.tools import wait

hub = PrimeHub()

# `while` loops repeat as long as the condition is True.
#
# `while True:` means “loop forever” (until the program is stopped on the hub).
# This is common for programs that should keep running, like a status light.
#
# Try it:
# - Change colors or wait times.
# - Add a third color.

# Blink light forever.
while True:
    hub.light.on(Color.RED)
    wait(500)
    hub.light.on(Color.GREEN)
    wait(500)