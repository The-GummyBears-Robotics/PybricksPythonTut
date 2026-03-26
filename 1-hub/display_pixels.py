from pybricks.hubs import PrimeHub
from pybricks.tools import wait

# Individual pixels on the 5×5 display.
#
# `hub.display.pixel(row, col, brightness)` turns on ONE dot.
# - row and col go from 0 to 4
# - brightness is 0–100 (0 means off)
#
# Try it: light up a diagonal line by turning on (0,0), (1,1), (2,2), ...

# Initialize the hub.
hub = PrimeHub()

# Turn on the pixel at row 1, column 2.
hub.display.pixel(1, 2)
wait(2000)

# Turn on the pixel at row 2, column 4, at 50% brightness.
hub.display.pixel(2, 4, 50)
wait(2000)

# Turn off the pixel at row 1, column 2.
hub.display.pixel(1, 2, 0)
wait(2000)
