from pybricks.hubs import PrimeHub
from pybricks.tools import wait

hub = PrimeHub()

# Tilt reading.
#
# `hub.imu.tilt()` returns (pitch, roll) in degrees.
# - pitch: forward/back tilt
# - roll: left/right tilt
# Great for balance games or “tilt to control” activities.

# Read tilt continuously.
while True:
    pitch, roll = hub.imu.tilt()
    
    print("Pitch:", pitch, "degrees")
    print("Roll:", roll, "degrees")
    print("---")
    
    wait(500)