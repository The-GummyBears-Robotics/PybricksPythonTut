from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()
left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right = Motor(Port.B)
robot = DriveBase(left, right, wheel_diameter=56, axle_track=112)

robot.use_gyro(True)

# Reset heading to 0 (this is "North")
hub.imu.reset_heading(0)

hub.display.text("START")
wait(2000)

# Turn to face different directions
target_headings = [90, 180, 270, 0]  # East, South, West, North

for target in target_headings:
    current = hub.imu.heading()

    # Calculate turn needed
    turn_angle = target - current

    # Adjust for shortest path
    if turn_angle > 180:
        turn_angle = turn_angle - 360
    elif turn_angle < -180:
        turn_angle = turn_angle + 360

    hub.display.number(target)
    hub.light.on(Color.YELLOW)

    robot.turn(turn_angle)

    wait(1000)

hub.display.text("DONE")
hub.light.on(Color.GREEN)