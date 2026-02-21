# run two motors together 
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

hub = PrimeHub()

# Left and right drive motors
left_motor  = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, positive_direction=Direction.CLOCKWISE)

# Drive forward
left_motor.run(400)
right_motor.run(400)
wait(2000)

# Turn (spin left motor back)
left_motor.run(-300)
right_motor.run(300)
wait(800)

# Drive forward again
left_motor.run(400)
right_motor.run(400)
wait(2000)

# Stop both
left_motor.stop()
right_motor.stop()