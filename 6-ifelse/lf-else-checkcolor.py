from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

hub = PrimeHub()
sensor = ColorSensor(Port.A)

while True:
    color = sensor.color()
    reflection = sensor.reflection()
    
    # Check if BOTH conditions are true
    if color == Color.BLACK and reflection < 20:
        hub.display.text("BLACK LINE")
        hub.speaker.beep(600, 100)
    else:
        hub.display.text("NO LINE")
    
    wait(200)