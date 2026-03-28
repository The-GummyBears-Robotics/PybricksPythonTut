# Beeps are the “hello world” of sound.
#
# `beep(frequency=..., duration=...)`:
# - frequency is in Hertz (Hz). Bigger number = higher pitch.
# - duration is in milliseconds (ms). Bigger number = longer beep.
#
# Try it:
# - Make a “doorbell”: two beeps with different pitches.
# - Put beeps in a loop to make an alarm.

from pybricks.hubs import PrimeHub
from pybricks.tools import wait

hub = PrimeHub()

# Simple single beep (500 Hz, 500ms)
hub.speaker.beep(frequency=500, duration=500)

wait(200)

# Higher pitch beep
hub.speaker.beep(frequency=1000, duration=300)