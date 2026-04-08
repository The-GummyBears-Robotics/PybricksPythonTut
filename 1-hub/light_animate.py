from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.tools import wait
from umath import sin, pi

# LED animation.
#
# `hub.light.animate([...], interval=...)` cycles through a LIST of colors.
# You can build that list by hand, or generate it with a loop/list-comprehension.
#
# Tricky line below:
# - `sin(...)` makes a smooth wave from -1 to +1
# - we scale/shift it into 0..1 to use as brightness
# - `Color.RED * brightness` dims the color (0 = off, 1 = full)

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