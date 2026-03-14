from pybricks.hubs import PrimeHub
from pybricks.parameters import Icon, Color
from pybricks.tools import wait

hub = PrimeHub()

def celebrate():
    """Play a celebration animation"""
    hub.display.icon(Icon.HAPPY)
    hub.speaker.play_notes(['C5/8', 'E5/8', 'G5/4'], tempo=150)
    hub.light.blink(Color.GREEN, [200, 200])
    wait(2000)
    hub.light.off()

# Call the function
celebrate()
wait(500)
celebrate()  # Call it again!