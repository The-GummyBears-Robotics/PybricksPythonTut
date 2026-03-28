from pybricks.hubs import PrimeHub
from pybricks.pupdevices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

hub = PrimeHub()
sensor = UltrasonicSensor(Port.A)

# Distance measurement basics.
#
# Ultrasonic sensor returns distance in millimeters.
# We also show `distance // 10` on the hub display (roughly centimeters).
# Integer division (`//`) drops decimals.

# Continuously measure and display distance.
while True:
    distance = sensor.distance()
    
    print("Distance:", distance, "mm")
    
    # Display on hub (in cm, 0-99 range)
    hub.display.number(distance // 10)
    
    wait(200)