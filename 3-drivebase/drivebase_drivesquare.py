from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()

left_motor  = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

# Drive a square (4 sides × 400mm, turn right 90° each corner), method 1

robot.straight(400)
wait(200)
robot.turn(90)
wait(200)

robot.straight(400)
wait(200)
robot.turn(90)
wait(200)

robot.straight(400)
wait(200)
robot.turn(90)
wait(200)

robot.straight(400)
wait(200)
robot.turn(90)
wait(200)


# Drive a square (4 sides × 400mm, turn right 90° each corner), method 2
for i in range(4):
    robot.straight(400)
    wait(200)
    robot.turn(90)
    wait(200)
    
# Drive a square (4 sides × 400mm, turn right 90° each corner), method 3

def drivesquare ():
        
