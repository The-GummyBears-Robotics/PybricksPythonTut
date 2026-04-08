from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait, multitask, run_task

hub   = PrimeHub()
motor = Motor(Port.A)

async def move():
    await motor.run_angle(200, 1080)  # slow, takes a while

async def timeout():
    await wait(1000)  # 1 second limit
    print("Timed out!")

async def main():
    await multitask(move(), timeout(), race=True)
    motor.stop()

run_task(main())