#The SPIKE Prime hub has a 5×5 LED matrix. 
# Icons are displayed using hub.display.icon() with either:
# Built-in Icon constants from pybricks.parameters
# Custom icons using a 2D list or matrix of brightness values (0–100)

from pybricks.hubs import PrimeHub
from pybricks.parameters import Icon
from pybricks.tools import wait

hub = PrimeHub()

# Cycle through common icons
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
    hub.display.icon(icon)
    wait(600)

hub.display.off()