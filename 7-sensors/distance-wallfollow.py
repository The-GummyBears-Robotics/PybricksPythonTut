from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
distance_sensor = UltrasonicSensor(Port.C)  # mounted on side

robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

# Target distance from wall (200mm)
target = 200

# Follow wall at constant distance
while True:
    distance = distance_sensor.distance()
    
    # Calculate error
    error = distance - target
    
    # Proportional control for turning
    # If too close to wall, turn away (left)
    # If too far from wall, turn toward it (right)
    turn_rate = error * 0.3
    
    robot.drive(speed=150, turn_rate=turn_rate)
    
    wait(10)