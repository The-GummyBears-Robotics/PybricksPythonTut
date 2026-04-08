from pybricks.hubs import PrimeHub
from pybricks.pupdevices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

hub = PrimeHub()
sensor = UltrasonicSensor(Port.A)

# Continuously measure and display distance
while True:
    distance = sensor.distance()

    print("Distance:", distance, "mm")

    # Display on hub (in cm, 0-99 range)
    hub.display.number(distance // 10)

    wait(200)