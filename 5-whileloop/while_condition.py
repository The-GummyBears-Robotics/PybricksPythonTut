from pybricks.hubs import PrimeHub
from pybricks.tools import wait

hub = PrimeHub()

count = 0

# Count from 0 to 9
while count < 10:
    hub.display.number(count)
    hub.speaker.beep(frequency=300 + count * 50, duration=100)
    wait(400)
    count += 1

hub.display.text("DONE!")