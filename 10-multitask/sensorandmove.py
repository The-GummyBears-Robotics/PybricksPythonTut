from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait, multitask, run_task

hub    = PrimeHub()
motor  = Motor(Port.A)
sensor = ColorSensor(Port.C)

async def drive():
    await motor.run_angle(300, 1080)

async def watch_color():
    while True:
        if sensor.color() == Color.RED:
            print("Saw red!")
        await wait(100)  # check every 100ms

async def main():
    # Watch the sensor the whole time the motor is running
    await multitask(drive(), watch_color(), race=True)

run_task(main())