# Lab A — multi-stage shapes with functions (~20–30 min)
#
# Box bot: left motor on A, right on B (same idea as 3-drivebase/).
#
# Stage 1 (starter): one call = one square side, then call it 4 times.
#   No parameters yet: edit edge_mm inside the function to resize the square.
# Stage 2: smarter size control with one parameter (edge_mm).
# Stage 3: regular polygons (triangle / pentagon / hexagon) with angle hints.
#
# Angle hint for Stage 3:
#   turn angle = 360 / number_of_sides
#   - Triangle (3): 120°
#   - Pentagon (5): 72°
#   - Hexagon (6): 60°

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

# Use hub gyro for straighter driving and more repeatable turns.
# Pybricks docs: DriveBase.use_gyro(True)
robot.use_gyro(True)
robot.reset(0, 0)

# Slower turn rate usually reduces overshoot on classroom bots.
straight_speed, straight_accel, turn_rate, turn_accel = robot.settings()
robot.settings(straight_speed, straight_accel, 120, turn_accel)


def one_side():
    """Stage 1: one square side (global robot, no parameters yet)."""
    edge_mm = 300
    robot.straight(edge_mm)
    wait(150)
    robot.turn(90)
    wait(150)


# Stage 1: Drive a full square (same behavior as the original lab).
for _ in range(4):
    one_side()

# Stage 2 challenge:
# - Change the function header to: def one_side(edge_mm):
# - Replace this loop call with: one_side(200) or one_side(450)
# - Keep using global robot inside the function.


def draw_regular_polygon(sides, side_mm=300):
    """Stage 3: draw any regular polygon with `sides` edges."""
    turn_deg = 360 / sides
    for _ in range(sides):
        robot.straight(side_mm)
        wait(150)
        robot.turn(turn_deg)
        wait(150)


# Stage 3 challenge (uncomment ONE line to test):
# draw_regular_polygon(3, 280)   # Equilateral triangle
# draw_regular_polygon(5, 220)   # Pentagon
# draw_regular_polygon(6)        # Hexagon (default side_mm=300)

hub.speaker.beep(600, 200)
