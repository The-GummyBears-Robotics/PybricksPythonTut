from pybricks.hubs import PrimeHub
from pybricks.parameters import Color, Button
from pybricks.tools import wait, multitask, run_task

hub = PrimeHub()

async def blink():
    while True:
        hub.light.on(Color.CYAN)
        await wait(400)
        hub.light.off()
        await wait(400)

async def wait_for_button():
    while Button.CENTER not in hub.buttons.pressed():
        await wait(50)
    print("Button pressed — stopping!")

async def main():
    await multitask(blink(), wait_for_button(), race=True)
    hub.light.off()

run_task(main())