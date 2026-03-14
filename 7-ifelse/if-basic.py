from pybricks.hubs import PrimeHub
from pybricks.parameters import Button
from pybricks.tools import wait

hub = PrimeHub()

# Check if CENTER button is pressed
if Button.CENTER in hub.buttons.pressed():
    hub.display.text("YES")
    hub.speaker.beep(800, 300)

hub.display.text("DONE")