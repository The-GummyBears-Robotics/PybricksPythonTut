# Changing brightness and using custom colors.
#
# Two “hard” ideas in this file:
# - Brightness: you can multiply a color by a number from 0.0 to 1.0
#   (example: `Color.RED * 0.3` is a dim red).
# - Custom colors: `Color(h=..., s=..., v=...)` uses HSV (hue/saturation/value).
#   Hue is like “which color” (0–359), value is brightness.

from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.tools import wait

# Initialize the hub.
hub = PrimeHub()

# Show the color at 30% brightness.
hub.light.on(Color.RED * 0.3)

wait(2000)

# Use your own custom color.
hub.light.on(Color(h=30, s=100, v=50))

wait(2000)

# Go through all the colors.
for hue in range(360):
    # This slowly sweeps through every hue. If it goes too fast, increase the wait.
    hub.light.on(Color(hue))
    wait(10)