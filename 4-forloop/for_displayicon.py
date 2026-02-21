from pybricks.hubs import PrimeHub
from pybricks.parameters import Icon
from pybricks.tools import wait

hub = PrimeHub()

# List of mood icons
moods = [Icon.HAPPY, Icon.SAD, Icon.ANGRY, Icon.SURPRISED, Icon.ASLEEP]

for mood in moods:
    hub.display.icon(mood)
    wait(800)

hub.display.off()