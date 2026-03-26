from pybricks.hubs import PrimeHub
from pybricks.parameters import Button
from pybricks.tools import wait

hub = PrimeHub()

# Select a number from 0-9
number = 0

# Same menu idea as `menu-icons.py`, but with numbers.
# `% 10` wraps around from 9 -> 0 and 0 -> 9.

hub.display.number(number)

while True:
    pressed = hub.buttons.pressed()
    
    if Button.LEFT in pressed:
        number = (number - 1) % 10
        hub.display.number(number)
        hub.speaker.beep(frequency=400, duration=50)
        wait(200)
    
    elif Button.RIGHT in pressed:
        number = (number + 1) % 10
        hub.display.number(number)
        hub.speaker.beep(frequency=600, duration=50)
        wait(200)
    
    elif Button.CENTER in pressed:
        hub.speaker.beep(frequency=800, duration=200)
        break
    
    wait(10)

print("Selected number:", number)