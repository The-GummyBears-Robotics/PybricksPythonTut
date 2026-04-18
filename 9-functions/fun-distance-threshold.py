# Same teaching idea as ../teaching/functions-intro.html (too_close slider demo).
#
# Pairs with sensor driving examples like ../8-sensors/distance-avoid.py

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

hub = PrimeHub()
sensor = UltrasonicSensor(Port.A)


def too_close(distance_mm, threshold_mm=300):
    """Return True if an obstacle is closer than threshold (millimeters)."""
    return distance_mm < threshold_mm


def path_clear(distance_mm, threshold_mm=300):
    """Return True if there is enough space (inverse of too_close)."""
    return distance_mm >= threshold_mm


# Try it with live readings
while True:
    d = sensor.distance()
    close = too_close(d)
    hub.display.text("CLOSE" if close else "OK")
    wait(200)
