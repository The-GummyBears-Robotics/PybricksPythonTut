from pybricks.hubs import PrimeHub
from pybricks.tools import wait

hub = PrimeHub()

# Beep 5 times
for i in range(5):
    hub.speaker.beep(frequency=500, duration=100)
    wait(200)

# Show numbers 0 to 4
for i in range(5):
    hub.display.number(i)
    wait(500)