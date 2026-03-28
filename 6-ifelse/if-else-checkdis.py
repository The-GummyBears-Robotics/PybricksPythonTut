from pybricks.hubs import PrimeHub
from pybricks.pupdevices import UltrasonicSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

hub = PrimeHub()
sensor = UltrasonicSensor(Port.A)

# `if / elif / else` picks exactly ONE branch.
#
# We use distance thresholds (in mm) to decide what to show:
# - < 100 mm: too close
# - 100..299 mm: near
# - 300+ mm: far
#
# Important: the order matters! We check the smallest threshold first.
while True:
    distance = sensor.distance()
    
    if distance < 100:
        hub.light.on(Color.RED)
        hub.display.text("TOO CLOSE")
    
    elif distance < 300:
        hub.light.on(Color.YELLOW)
        hub.display.text("NEAR")
    
    else:
        hub.light.on(Color.GREEN)
        hub.display.text("FAR")
    
    wait(100)