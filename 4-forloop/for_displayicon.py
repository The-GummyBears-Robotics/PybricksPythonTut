from pybricks.hubs import PrimeHub
from pybricks.parameters import Icon
from pybricks.tools import wait

hub = PrimeHub()

# Looping through a list of icons.
#
# Just like colors, icons can go in a list too.
# Each loop step shows one icon and waits so you can see it.
#
# Try it:
# - Add more icons.
# - Make it faster/slower by changing `wait(800)`.

# List of mood icons.
moods = [Icon.HAPPY, Icon.SAD, Icon.ANGRY, Icon.SURPRISED, Icon.ASLEEP]

for mood in moods:
    hub.display.icon(mood)
    wait(800)

hub.display.off()