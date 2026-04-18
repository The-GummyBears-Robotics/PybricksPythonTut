# Lab C — function returns a speed from distance (~15–20 min)
#
# Box bot + ultrasonic on C (same port idea as 8-sensors/distance-avoid.py).
# Goal: cruise_speed(distance_mm) returns a higher speed when far, lower when close.

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)
eyes = UltrasonicSensor(Port.C)


def cruise_speed(distance_mm):
    """Return forward speed; slow down near obstacles."""
    if distance_mm > 500:
        return 180
    if distance_mm > 250:
        return 100
    return 40


while True:
    d = eyes.distance()
    robot.drive(cruise_speed(d), 0)
    wait(40)
