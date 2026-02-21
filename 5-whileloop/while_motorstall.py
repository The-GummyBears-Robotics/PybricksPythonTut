from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Icon
from pybricks.tools import wait

hub = PrimeHub()

motor = Motor(Port.A)

# Run motor until it hits something (stalls)
motor.run(300)
hub.display.icon(Icon.ARROW_RIGHT)

while True:
    # Check if motor has stalled
    if motor.speed() == 0 and motor.control.done():
        break
    wait(10)

motor.stop()
hub.display.icon(Icon.ANGRY)
hub.speaker.beep(frequency=800, duration=500)
print("Motor stalled!")