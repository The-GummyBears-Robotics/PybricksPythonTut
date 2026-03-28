from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

hub = PrimeHub()
sensor = ColorSensor(Port.A)

while True:
    color = sensor.color()
    reflection = sensor.reflection()
    
    # Using `and` means BOTH conditions must be true.
    # This makes it harder to get false positives.
    # Example: you might read Color.BLACK sometimes even when you're not on the line,
    # so we also check reflection < 20 to confirm it is dark.
    if color == Color.BLACK and reflection < 20:
        hub.display.text("BLACK LINE")
        hub.speaker.beep(600, 100)
    else:
        hub.display.text("NO LINE")
    
    wait(200)