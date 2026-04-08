from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait, multitask, run_task

hub   = PrimeHub()
motor = Motor(Port.A)
sonar = UltrasonicSensor(Port.C)

async def drive_forward():
    """Keep driving until something stops us."""
    motor.run(500)
    await wait(10_000)   # drive up to 10 seconds
    motor.stop()

async def watch_for_obstacle():
    """Stop as soon as object is closer than 100 mm."""
    while sonar.distance() > 100:
        await wait(50)
    motor.stop()

async def blink_while_moving():
    """Blink forever (will be cancelled by race)."""
    while True:
        hub.light.on(Color.YELLOW)
        await wait(300)
        hub.light.off()
        await wait(300)

async def main():
    # race=True → stops ALL tasks the moment ONE finishes
    await multitask(drive_forward(), watch_for_obstacle(), blink_while_moving(), race=True)
    hub.light.on(Color.RED)
    print("Obstacle detected — stopped!")

run_task(main())