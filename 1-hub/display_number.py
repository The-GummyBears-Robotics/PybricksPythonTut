from pybricks.hubs import PrimeHub
from pybricks.tools import wait

# Counting on the hub display.
#
# `hub.display.number(n)` shows a number on the 5×5 screen.
# We use a `for` loop to count up, pausing each time so you can see it.
#
# Try it:
# - Change the range (count to 20, or count down).
# - Change `wait(200)` (milliseconds) to speed up or slow down.

# Initialize the hub.
hub = PrimeHub()

# Count from 0 to 99.
for i in range(100):
    hub.display.number(i)
    wait(200)