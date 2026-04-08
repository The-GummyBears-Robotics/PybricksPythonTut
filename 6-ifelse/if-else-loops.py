from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.tools import wait

hub = PrimeHub()

while True:
    # Only one of these branches runs each loop.
    # The first True condition wins because we use `elif`.
    if Button.LEFT in hub.buttons.pressed():
        hub.display.icon(Icon.ARROW_LEFT)
        hub.speaker.beep(400, 100)
    
    elif Button.RIGHT in hub.buttons.pressed():
        hub.display.icon(Icon.ARROW_RIGHT)
        hub.speaker.beep(600, 100)
    
    elif Button.CENTER in hub.buttons.pressed():
        hub.display.icon(Icon.HAPPY)
        hub.speaker.beep(800, 100)
    
    else:
        # No buttons pressed.
        hub.display.icon(Icon.PAUSE)
    
    wait(10)