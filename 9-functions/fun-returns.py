from pybricks.hubs import PrimeHub
from pybricks.pupdevices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

hub = PrimeHub()
sensor = UltrasonicSensor(Port.A)

def get_distance_cm():
    """Read distance and return centimeters.

    This function demonstrates RETURN values:
    - read sensor in mm
    - convert
    - give the result back to caller
    """
    distance_mm = sensor.distance()
    distance_cm = distance_mm / 10
    return distance_cm

# Use the returned value
while True:
    cm = get_distance_cm()
    print("Distance:", cm, "cm")
    hub.display.number(int(cm))
    wait(200)