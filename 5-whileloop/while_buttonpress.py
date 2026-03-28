from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.tools import wait

hub = PrimeHub()

hub.display.icon(Icon.HAPPY)

# Waiting for an event (button press).
#
# This pattern is called “polling”: we repeatedly check the buttons.
# The `wait(10)` is important so we don’t waste CPU (and it also helps battery life).
#
# Try it:
# - Change Button.CENTER to Button.LEFT or Button.RIGHT.
# - Show a different icon when the button is pressed.

# Wait for CENTER button press.
while True:
    if Button.CENTER in hub.buttons.pressed():
        break
    wait(10)

hub.display.icon(Icon.SURPRISED)
hub.speaker.beep(frequency=800, duration=200)