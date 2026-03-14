from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.tools import wait

hub = PrimeHub()

# Reset heading to 0 (call this "North")
hub.imu.reset_heading(0)

hub.display.text("COMPASS")
wait(1000)

while True:
    heading = hub.imu.heading()

    # 0-90° or 270-360° = North side
    # 90-270° = South side
    if heading < 90 or heading > 270:
        hub.display.char('N')
        hub.light.on(Color.BLUE)
    else:
        hub.display.char('S')
        hub.light.on(Color.RED)

    wait(200)