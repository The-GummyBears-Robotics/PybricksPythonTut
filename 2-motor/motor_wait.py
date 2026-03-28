from pybricks.pupdevices import Motor
from pybricks.parameters import Port

# Two motors at the same time (waiting vs not waiting).
#
# Most motor commands "block" (your program waits until the motor finishes).
# Here we use `wait=False` so the track motor starts moving, and then the code
# immediately continues to start the gripper motor.
#
# This is how you make mechanisms move together.

# Initialize motors on port A and B.
track_motor = Motor(Port.A)
gripper_motor = Motor(Port.B)

# Make the track motor start moving,
# but don't wait for it to finish.
track_motor.run_angle(500, 360, wait=False)

# Now make the gripper motor rotate. This
# means they move at the same time.
gripper_motor.run_angle(200, 720)