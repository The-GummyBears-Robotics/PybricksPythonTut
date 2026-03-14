from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color, Icon
from pybricks.tools import wait

hub = PrimeHub()
sensor = ColorSensor(Port.A)

# React differently to each color
while True:
    detected = sensor.color()
    
    if detected == Color.RED:
        hub.light.on(Color.RED)
        hub.display.icon(Icon.ANGRY)
        hub.speaker.beep(400, 100)
    
    elif detected == Color.BLUE:
        hub.light.on(Color.BLUE)
        hub.display.icon(Icon.HAPPY)
        hub.speaker.beep(600, 100)
    
    elif detected == Color.GREEN:
        hub.light.on(Color.GREEN)
        hub.display.icon(Icon.HEART)
        hub.speaker.beep(800, 100)
    
    elif detected == Color.YELLOW:
        hub.light.on(Color.YELLOW)
        hub.display.icon(Icon.STAR)
        hub.speaker.beep(1000, 100)
    
    else:
        hub.light.off()
        hub.display.icon(Icon.PAUSE)
    
    wait(200)