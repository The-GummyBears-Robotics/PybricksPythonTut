from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

hub = PrimeHub()
sensor = ColorSensor(Port.A)

# Reflection reading (line-following foundation).
#
# `reflection()` is usually around 0..100:
# - low numbers = dark surface (like black line)
# - high numbers = bright surface (like white mat)
#
# Teams usually calibrate thresholds on their own table lighting.

# Read reflection continuously.
while True:
    reflection = sensor.reflection()
    
    print("Reflection:", reflection, "%")
    
    # Show on display (0-9 scale)
    hub.display.number(reflection // 10)
    
    wait(200)