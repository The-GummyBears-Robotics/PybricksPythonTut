# Same teaching idea as ../teaching/functions-intro.html (blink_times demo).
#
# Parameters let one function handle many cases — change n, ms_on, ms_off.

from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.tools import wait

hub = PrimeHub()


def blink_times(n, ms_on=500, ms_off=300):
    """Blink the hub LED red `n` times.

    n: how many blinks
    ms_on / ms_off: milliseconds on and off (defaults like a quick flash)
    """
    for _ in range(n):
        hub.light.on(Color.RED)
        wait(ms_on)
        hub.light.off()
        wait(ms_off)


blink_times(3)
wait(500)
blink_times(5, ms_on=200, ms_off=200)
