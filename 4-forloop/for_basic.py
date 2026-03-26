from pybricks.hubs import PrimeHub
from pybricks.tools import wait

hub = PrimeHub()

# `for` loops repeat a block of code a set number of times.
#
# `range(5)` produces the numbers 0, 1, 2, 3, 4 (5 numbers total).
# We don’t actually use `i` here, but the loop still repeats 5 times.
#
# Try it: change 5 to 3, or 10.

# Beep 5 times.
for i in range(5):
    hub.speaker.beep(frequency=500, duration=100)
    wait(200)

# Show numbers 0 to 4.
# (Same loop idea as above, but now we DO use `i`.)
for i in range(5):
    hub.display.number(i)
    wait(500)