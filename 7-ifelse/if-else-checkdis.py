from pybricks.hubs import PrimeHub
from pybricks.pupdevices import UltrasonicSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

hub = PrimeHub()
sensor = UltrasonicSensor(Port.A)

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