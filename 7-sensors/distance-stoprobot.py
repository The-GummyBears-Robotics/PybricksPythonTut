from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.parameters import Port, Direction, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
distance_sensor = UltrasonicSensor(Port.C)

robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

# Drive forward until obstacle within 200mm
robot.drive(speed=200, turn_rate=0)
hub.display.icon(Icon.ARROW_RIGHT)

while True:
    if distance_sensor.distance() < 200:
        break
    wait(10)

robot.stop()
hub.display.icon(Icon.PAUSE)
hub.speaker.beep(frequency=600, duration=300)
print("Obstacle detected!")