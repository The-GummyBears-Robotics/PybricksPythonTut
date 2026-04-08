from pybricks.hubs import PrimeHub
from pybricks.tools import wait

hub = PrimeHub()

# Counting with `range(start, stop)`.
#
# `range(1, 11)` counts 1, 2, 3, ... 10.
# The `stop` number (11) is NOT included — this is a common beginner “gotcha”.
#
# Also notice the beep frequency:
# - `count * 50` makes the pitch go higher as the number goes up.
#
# Try it:
# - Make it count down: `range(10, 0, -1)`
# - Change 50 to 100 to make the pitch change faster.
for count in range(1, 11):
    hub.display.number(count)
    hub.speaker.beep(frequency=count * 50, duration=100)
    wait(300)

hub.display.off()