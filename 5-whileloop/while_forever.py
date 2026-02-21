from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.tools import wait

hub = PrimeHub()

# Blink light forever
while True:
    hub.light.on(Color.RED)
    wait(500)
    hub.light.on(Color.GREEN)
    wait(500)