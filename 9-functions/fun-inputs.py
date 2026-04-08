from pybricks.hubs import PrimeHub
from pybricks.tools import wait

hub = PrimeHub()

def beep_times(count, frequency):
    """Beep `count` times at `frequency` Hz.

    This function has PARAMETERS (inputs), so the same function can do
    different jobs based on values you pass in.
    """
    for _ in range(count):
        hub.speaker.beep(frequency=frequency, duration=100)
        wait(150)

# Call with different parameters
beep_times(3, 400)   # 3 beeps at 400 Hz
wait(500)
beep_times(5, 800)   # 5 beeps at 800 Hz
