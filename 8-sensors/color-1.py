from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

hub = PrimeHub()
sensor = ColorSensor(Port.A)

# Read and display detected colors
while True:
    detected = sensor.color()

    print("Color:", detected)

    # Match the hub light to detected color
    if detected == Color.RED:
        hub.light.on(Color.RED)
    elif detected == Color.BLUE:
        hub.light.on(Color.BLUE)
    elif detected == Color.GREEN:
        hub.light.on(Color.GREEN)
    elif detected == Color.YELLOW:
        hub.light.on(Color.YELLOW)
    elif detected == Color.WHITE:
        hub.light.on(Color.WHITE)
    else:
        hub.light.off()

    wait(100)