from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color
from pybricks.tools import wait

hub = PrimeHub()

hub.display.text("PRESS")
wait(2000)

if Button.CENTER in hub.buttons.pressed():
    hub.light.on(Color.GREEN)
    hub.display.text("PRESSED")
else:
    hub.light.on(Color.RED)
    hub.display.text("NOT PRESSED")