from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ForceSensor
from pybricks.parameters import Port, Color, Icon
from pybricks.tools import wait

hub = PrimeHub()
sensor = ForceSensor(Port.A)

hub.display.text("PRESS ME")

while True:
    if sensor.pressed():
        # Sensor is pressed
        hub.light.on(Color.GREEN)
        hub.display.icon(Icon.HAPPY)
        hub.speaker.beep(800, 100)
    else:
        # Sensor is not pressed
        hub.light.off()
        hub.display.icon(Icon.ASLEEP)

    wait(50)