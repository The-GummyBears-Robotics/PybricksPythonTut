from pybricks.hubs import PrimeHub
from pybricks.tools import wait

hub = PrimeHub()

count = 0

# `while` with a condition.
#
# This loop runs until `count < 10` becomes False.
# The line `count += 1` is critical: without it, the loop would never end.
#
# Try it:
# - Change 10 to 5 (shorter).
# - Change the beep formula to make a different sound pattern.

# Count from 0 to 9.
while count < 10:
    hub.display.number(count)
    hub.speaker.beep(frequency=300 + count * 50, duration=100)
    wait(400)
    count += 1

hub.display.text("DONE!")