from pybricks.hubs import PrimeHub
from pybricks.tools import wait

hub = PrimeHub()

def beep_times(count, frequency):
    """Beep a specified number of times at a given frequency"""
    for _ in range(count):
        hub.speaker.beep(frequency=frequency, duration=100)
        wait(150)

# Call with different parameters
beep_times(3, 400)   # 3 beeps at 400 Hz
wait(500)
beep_times(5, 800)   # 5 beeps at 800 Hz
