from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
distance_sensor = UltrasonicSensor(Port.C)

robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

# Target distance to maintain (300mm)
target = 300

# Follow an object, keeping roughly constant distance.
#
# This is proportional control (P-control):
# - `error = measured - target`
# - speed is proportional to error
#
# If far away -> positive error -> drive forward.
# If too close -> negative error -> drive backward.
# You may need to clamp speed in real robots to avoid oscillation.
while True:
    distance = distance_sensor.distance()
    
    # Calculate error
    error = distance - target
    
    # Proportional control - move toward/away to maintain distance
    speed = error * 0.5
    
    robot.drive(speed=speed, turn_rate=0)
    
    # Display current distance
    hub.display.number(distance // 10)
    
    wait(50)