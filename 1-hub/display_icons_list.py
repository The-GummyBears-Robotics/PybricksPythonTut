# The SPIKE Prime hub has a 5×5 LED matrix display.
#
# This program stores many built-in icons in a Python list, then shows them one-by-one.
# Key idea: you can put anything you want to repeat through into a list, then loop over it.
#
# Try it:
# - Change the `wait(600)` to make the “animation” faster/slower.
# - Remove icons you don’t like, or add new `Icon.*` values.

from pybricks.hubs import PrimeHub
from pybricks.parameters import Icon
from pybricks.tools import wait

hub = PrimeHub()

# Cycle through common icons.
icons = [
    Icon.HAPPY,
    Icon.SAD,
    Icon.ANGRY,
    Icon.HEART,
    Icon.SKULL,
    Icon.SURPRISED,
    Icon.ASLEEP,
    Icon.UP,
    Icon.DOWN,
    Icon.LEFT,
    Icon.RIGHT,
    Icon.SQUARE,
    Icon.TRIANGLE,
    Icon.DIAMOND,
    Icon.STAR,
    Icon.MUSIC,
    Icon.PAUSE,
    Icon.CIRCLE,
    Icon.ARROW_RIGHT,
    Icon.TARGET,
]

for icon in icons:
    # Show one icon, then pause so your eyes can see it.
    hub.display.icon(icon)
    wait(600)

# Turn the display off (blank screen).
hub.display.off()