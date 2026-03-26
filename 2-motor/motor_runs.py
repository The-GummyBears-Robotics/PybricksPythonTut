from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Motor speed basics.
#
# Ports (A, B, C, ...) are where your motors plug into the hub.
# `run(speed)` uses speed in degrees/second:
# - positive speed spins one direction
# - negative speed spins the other direction
#
# `dc(power)` uses “raw power” in percent (-100..100). It’s less precise than `run()`,
# but it’s useful for quick tests.

# Initialize a motor on port A.
example_motor = Motor(Port.A)

# Run at 500 deg/s (degrees per second) and then stop (default is coast).
print("Demo of run")
example_motor.run(500)
wait(1500)
example_motor.stop()
wait(1500)

# Run at 50% duty cycle ("power") and then stop.
print("Demo of dc")
example_motor.dc(50)
wait(1500)
example_motor.stop()
wait(1500)

# `run_time(speed, time_ms)` runs for a time (milliseconds).
print("Demo of run_time")
example_motor.run_time(500, 2000)
wait(1500)

# `run_angle(speed, angle_deg)` rotates a RELATIVE amount from where you are now.
print("Demo of run_angle")
example_motor.run_angle(500, 90)
wait(1500)

# `run_target(speed, target_angle_deg)` goes to an ABSOLUTE angle.
# This makes more sense after you reset the angle to something known.
print("Demo of run_target to 0")
example_motor.run_target(500, 0)
wait(1500)

# Target angles can be negative too.
print("Demo of run_target to -90")
example_motor.run_target(500, -90)
wait(1500)

# `run_until_stalled(...)` keeps trying until the motor can't turn anymore
# (for example: it hits a wall, or your mechanism reaches the end).
print("Demo of run_until_stalled")
example_motor.run_until_stalled(500)
print("Done")
wait(1500)