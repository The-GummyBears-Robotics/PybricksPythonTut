# The speaker plays beeps of different frequencies and durations. 
# A typical audible beep is 500 Hz — higher values produce higher
# tones. Duration is in milliseconds.

from pybricks.hubs import PrimeHub
from pybricks.tools import wait

hub = PrimeHub()

# Simple single beep (500 Hz, 500ms)
hub.speaker.beep(frequency=500, duration=500)

wait(200)

# Higher pitch beep
hub.speaker.beep(frequency=1000, duration=300)