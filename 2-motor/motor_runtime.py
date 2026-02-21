# Example 3: Run for a Set Time
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

hub = PrimeHub()

motor = Motor(Port.A)

# Run at 400 deg/s for 1.5 seconds, then brake
motor.run_time(400, 1500, then=Stop.BRAKE)
wait(500)

# Run backward for 1 second, then coast to stop
motor.run_time(-400, 1000, then=Stop.COAST)
wait(500)

# Run forward for 2 seconds, then hold position
motor.run_time(400, 2000, then=Stop.HOLD)