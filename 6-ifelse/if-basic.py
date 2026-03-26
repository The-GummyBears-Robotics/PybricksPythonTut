from pybricks.hubs import PrimeHub
from pybricks.parameters import Button
from pybricks.tools import wait

hub = PrimeHub()

# Simple `if` statement.
#
# `if ...:` runs the indented block only when the condition is True.
# Here we check whether the CENTER button is currently pressed.
#
# Note: this checks "right now". If you want to WAIT until a button is pressed,
# use a `while` loop (see the while-loop lessons).

# Check if CENTER button is pressed.
if Button.CENTER in hub.buttons.pressed():
    hub.display.text("YES")
    hub.speaker.beep(800, 300)

hub.display.text("DONE")