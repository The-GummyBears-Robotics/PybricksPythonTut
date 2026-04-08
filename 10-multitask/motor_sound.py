from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait, multitask, run_task

hub   = PrimeHub()
motor = Motor(Port.A)

async def spin_motor():
    await motor.run_angle(500, 720)  # spin 2 full rotations

async def beep():
    await hub.speaker.beep(500, 200)
    await wait(300)
    await hub.speaker.beep(800, 200)

async def main():
    await multitask(spin_motor(), beep())

run_task(main())