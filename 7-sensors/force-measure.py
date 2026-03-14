from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ForceSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

hub = PrimeHub()
sensor = ForceSensor(Port.A)

hub.display.text("FORCE")
wait(1000)

while True:
    force = sensor.force()  # Force in Newtons (N)

    # Show force value on display
    hub.display.number(int(force))

    # Print detailed info
    print(f"Force: {force:.1f} N")

    # Change light color based on force
    if force > 5:
        hub.light.on(Color.RED)      # Hard press
    elif force > 2:
        hub.light.on(Color.YELLOW)   # Medium press
    elif force > 0:
        hub.light.on(Color.GREEN)    # Light press
    else:
        hub.light.off()              # Not pressed

    wait(100)