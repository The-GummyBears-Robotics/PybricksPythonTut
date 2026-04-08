from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.tools import wait

hub = PrimeHub()

# Menu options
options = [Icon.HAPPY, Icon.HEART, Icon.STAR, Icon.MUSIC, Icon.CIRCLE]
current = 0

# Show first option
hub.display.icon(options[current])

# Menu loop
while True:
    pressed = hub.buttons.pressed()

    if Button.LEFT in pressed:
        # Previous option (wrap around)
        current = (current - 1) % len(options)
        hub.display.icon(options[current])
        hub.speaker.beep(frequency=400, duration=50)
        wait(200)

    elif Button.RIGHT in pressed:
        # Next option (wrap around)
        current = (current + 1) % len(options)
        hub.display.icon(options[current])
        hub.speaker.beep(frequency=600, duration=50)
        wait(200)

    elif Button.CENTER in pressed:
        # Selected!
        hub.speaker.beep(frequency=800, duration=200)
        break

    wait(10)

print("Selected option:", current)
hub.display.text("GO!")