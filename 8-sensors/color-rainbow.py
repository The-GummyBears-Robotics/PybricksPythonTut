from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

hub = PrimeHub()
sensor = ColorSensor(Port.A)

# Cycle sensor lights through different patterns
while True:
    # Blink all together
    for _ in range(3):
        sensor.lights.on(100)
        wait(200)
        sensor.lights.off()
        wait(200)

    # Wave pattern (left to right)
    for _ in range(3):
        sensor.lights.on((100, 0, 0))
        wait(150)
        sensor.lights.on((0, 100, 0))
        wait(150)
        sensor.lights.on((0, 0, 100))
        wait(150)

    # Fade in/out
    for brightness in range(0, 101, 10):
        sensor.lights.on(brightness)
        wait(50)
    for brightness in range(100, -1, -10):
        sensor.lights.on(brightness)
        wait(50)