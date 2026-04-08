from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.tools import wait

# Light blinking patterns.
#
# Key idea: `hub.light.blink(color, pattern)` repeats forever until you call it again.
# The `pattern` list alternates ON and OFF times in milliseconds:
#   [on_ms, off_ms] or [on_ms, off_ms, on_ms, off_ms, ...]
#
# Try it: change the numbers, add more pairs, or switch colors.

# Initialize the hub.
hub = PrimeHub()

# Keep blinking red on and off.
hub.light.blink(Color.RED, [500, 500])

wait(10000)

# Keep blinking green slowly and then quickly.
hub.light.blink(Color.GREEN, [500, 500, 50, 900])

wait(10000)