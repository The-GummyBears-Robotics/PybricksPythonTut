# run untill stall
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Icon
from pybricks.tools import wait

hub = PrimeHub()

motor = Motor(Port.A)

# Run until the motor stalls (hits something)
hub.display.icon(Icon.ARROW_RIGHT)
motor.run_until_stalled(300)

# Stalled! Show warning
hub.display.icon(Icon.ANGRY)
hub.speaker.beep(frequency=800, duration=500)

print("Motor stalled at:", motor.angle(), "degrees")