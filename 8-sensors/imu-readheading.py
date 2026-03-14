from pybricks.hubs import PrimeHub
from pybricks.tools import wait

hub = PrimeHub()

# Reset heading to 0 at start
hub.imu.reset_heading(0)

while True:
    heading = hub.imu.heading()
    
    print("Heading:", heading, "degrees")
    
    # Display cardinal direction
    if 337.5 <= heading or heading < 22.5:
        hub.display.char('N')
    elif 22.5 <= heading < 67.5:
        hub.display.text("NE")
    elif 67.5 <= heading < 112.5:
        hub.display.char('E')
    elif 112.5 <= heading < 157.5:
        hub.display.text("SE")
    elif 157.5 <= heading < 202.5:
        hub.display.char('S')
    elif 202.5 <= heading < 247.5:
        hub.display.text("SW")
    elif 247.5 <= heading < 292.5:
        hub.display.char('W')
    else:
        hub.display.text("NW")
    
    wait(200)