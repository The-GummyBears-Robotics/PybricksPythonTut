#The SPIKE Prime hub has a 5×5 LED matrix. 
# Icons are displayed using hub.display.icon() with either:
# Built-in Icon constants from pybricks.parameters
# Custom icons using a 2D list or matrix of brightness values (0–100)

from pybricks.hubs import PrimeHub
from pybricks.parameters import Icon
from pybricks.tools import wait

hub = PrimeHub()

# Display a happy face
hub.display.icon(Icon.HAPPY)
wait(1000)

# Display a sad face
hub.display.icon(Icon.SAD)
wait(1000)

# Display a heart
hub.display.icon(Icon.HEART)
wait(1000)

# Display an arrow pointing up
hub.display.icon(Icon.UP)
wait(1000)

# Turn off display
hub.display.off()