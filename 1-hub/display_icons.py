# The SPIKE Prime hub has a 5×5 LED matrix display.
#
# This program shows a few built-in icons from `pybricks.parameters.Icon`.
# `hub.display.icon(...)` shows one icon until you change it (or turn the display off).
#
# Try it:
# - Swap the icon order.
# - Change the wait times to make a “story” animation.
# - Look up other `Icon.*` options and add them here.

from pybricks.hubs import PrimeHub
from pybricks.parameters import Icon
from pybricks.tools import wait

hub = PrimeHub()

# Display a happy face.
hub.display.icon(Icon.HAPPY)
wait(1000)

# Display a sad face.
hub.display.icon(Icon.SAD)
wait(1000)

# Display a heart.
hub.display.icon(Icon.HEART)
wait(1000)

# Display an arrow pointing up.
hub.display.icon(Icon.UP)
wait(1000)

# Turn off display (go blank).
hub.display.off()