from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.tools import wait

hub = PrimeHub()

# Looping through a list.
#
# Here, we don’t use `range(...)`. Instead, we make a list of Colors and loop
# over the items directly. Each time through the loop, `color` becomes the next
# Color from the list.
#
# Try it:
# - Reorder the list to change the “light show”.
# - Add `Color.CYAN` or `Color.WHITE` if available on your hub.
# - Change `wait(500)` to control how long each color stays on.

# List of colors to cycle through.
colors = [Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW, Color.MAGENTA]

for color in colors:
    hub.light.on(color)
    wait(500)

hub.light.off()