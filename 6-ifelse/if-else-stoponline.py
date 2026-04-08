from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Icon, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Setup
hub = PrimeHub()
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
color_sensor = ColorSensor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

# Show ready
hub.display.text("READY")
wait(2000)

# Start driving
robot.drive(speed=200, turn_rate=0)
hub.display.icon(Icon.ARROW_RIGHT)
hub.light.on(Color.GREEN)

# Keep checking for black line
while True:
    reflection = color_sensor.reflection()

    # Reflection is 0..100-ish: lower = darker, higher = brighter.
    # This threshold (20) depends on lighting + sensor height + mat.
    # In practice, teams calibrate this number on their competition table.
    if reflection < 20:  # Black line detected
        # STOP!
        robot.stop()
        hub.display.icon(Icon.PAUSE)
        hub.light.on(Color.RED)
        hub.speaker.beep(frequency=800, duration=500)
        break  # Exit the loop

    wait(10)

hub.display.text("DONE")