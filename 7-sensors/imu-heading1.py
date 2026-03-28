from pybricks.hubs import PrimeHub
from pybricks.tools import wait

hub = PrimeHub()

hub.imu.reset_heading(0)

# Super simple heading split demo.
#
# This intentionally splits heading into two halves only.
# Good first step before building more detailed compass logic.
while True:
    heading = hub.imu.heading()

    # Simple: heading 0-179 = North, 180-359 = South
    if heading < 180:
        hub.display.char('N')
    else:
        hub.display.char('S')

    wait(200)