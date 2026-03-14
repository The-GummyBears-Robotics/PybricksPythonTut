from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Color, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
color_sensor = ColorSensor(Port.C)

robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

# Drive until red line detected
robot.drive(speed=200, turn_rate=0)
hub.display.icon(Icon.ARROW_RIGHT)

while True:
    if color_sensor.color() == Color.RED:
        break
    wait(10)

robot.stop()
hub.display.icon(Icon.PAUSE)
hub.speaker.beep(frequency=600, duration=300)
print("Red detected!")