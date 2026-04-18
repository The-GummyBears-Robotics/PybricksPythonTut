# Lab B — helper function for a “victory” sound (~10–15 min)
#
# Box bot: DriveBase on A/B as usual.
# Goal: put repeated beeps in victory_chirp(hub), then call it after a move.

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)


def victory_chirp(hub):
    """Short happy sound — change frequencies or counts."""
    hub.speaker.beep(600, 80)
    wait(60)
    hub.speaker.beep(900, 120)


robot.straight(400)
wait(200)
victory_chirp(hub)

robot.turn(180)
wait(200)
victory_chirp(hub)
