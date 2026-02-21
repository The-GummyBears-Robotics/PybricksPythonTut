from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.tools import wait

hub = PrimeHub()

# List of colors to cycle through
colors = [Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW, Color.MAGENTA]

for color in colors:
    hub.light.on(color)
    wait(500)

hub.light.off()