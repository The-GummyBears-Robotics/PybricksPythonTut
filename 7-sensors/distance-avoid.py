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

# Drive and avoid obstacles
while True:
    distance = distance_sensor.distance()
    
    if distance < 300:
        # Obstacle ahead - back up and turn
        robot.straight(-100)
        robot.turn(90)  # turn right
        hub.speaker.beep(frequency=800, duration=100)
    else:
        # Path clear - drive forward
        robot.drive(speed=150, turn_rate=0)
    
    wait(50)