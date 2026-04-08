from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import multitask, run_task

motor_a = Motor(Port.A)
motor_b = Motor(Port.B)

async def move_a():
    await motor_a.run_angle(500, 360)

async def move_b():
    await motor_b.run_angle(300, 720)

async def main():
    # Both motors move simultaneously instead of one after the other
    await multitask(move_a(), move_b())

run_task(main())
