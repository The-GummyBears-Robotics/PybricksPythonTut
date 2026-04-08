from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait, multitask, run_task

hub = PrimeHub()
left_motor  = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
drive_base  = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

# ── Task 1: drive a square ──────────────────────────────────────────
async def square():
    for side in range(4):
        await drive_base.straight(200)
        await drive_base.turn(90)

# ── Task 2: blink the hub light 10 times ───────────────────────────
async def blink():
    for i in range(10):
        hub.light.on(Color.RED)
        await wait(500)
        hub.light.on(Color.GREEN)
        await wait(500)

# ── Task 3: print hello after a delay ──────────────────────────────
async def hello(name):
    print("Hello!")
    await wait(2000)
    print(name)

# ── Main: run all three at once ────────────────────────────────────
async def main():
    print("Starting multitasking!")
    await multitask(square(), blink(), hello("Pybricks"))
    print("All done.")

run_task(main())