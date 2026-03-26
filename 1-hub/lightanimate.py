from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.tools import wait
from umath import sin, pi

# This file is the same idea as `light_animate.py`:
# using `hub.light.animate()` to cycle through a list of colors.
#
# Tip for kids: when two files look similar, compare them to spot what changed.

# Initialize the hub.
hub = PrimeHub()

# Make an animation with multiple colors.
hub.light.animate([Color.RED, Color.GREEN, Color.NONE], interval=500)

wait(10000)

# Make the color RED grow faint and bright using a sine pattern.
hub.light.animate([Color.RED * (0.5 * sin(i / 15 * pi) + 0.5) for i in range(30)], 40)

wait(10000)

# Cycle through a rainbow of colors.
hub.light.animate([Color(h=i * 8) for i in range(45)], interval=40)

wait(10000)