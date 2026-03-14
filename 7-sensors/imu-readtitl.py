from pybricks.hubs import PrimeHub
from pybricks.tools import wait

hub = PrimeHub()

# Read tilt continuously
while True:
    pitch, roll = hub.imu.tilt()
    
    print("Pitch:", pitch, "degrees")
    print("Roll:", roll, "degrees")
    print("---")
    
    wait(500)