from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.tools import wait

hub = PrimeHub()

hub.display.icon(Icon.HAPPY)

# Wait for CENTER button press
while True:
    if Button.CENTER in hub.buttons.pressed():
        break
    wait(10)

hub.display.icon(Icon.SURPRISED)
hub.speaker.beep(frequency=800, duration=200)