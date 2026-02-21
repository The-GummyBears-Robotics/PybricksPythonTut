from pybricks.hubs import PrimeHub
from pybricks.tools import wait

hub = PrimeHub()

# Count from 1 to 10 (range starts at 1, ends before 11)
for count in range(1, 11):
    hub.display.number(count)
    hub.speaker.beep(frequency=count * 50, duration=100)
    wait(300)

hub.display.off()