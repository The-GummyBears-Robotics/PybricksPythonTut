from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

hub = PrimeHub()

color_sensor = ColorSensor(Port.A)
distance_sensor = UltrasonicSensor(Port.B)

def is_line_detected():
    """Check if black line is under sensor"""
    reflection = color_sensor.reflection()
    return reflection < 20  # Black threshold

def is_obstacle_close():
    """Check if obstacle is within 300mm"""
    distance = distance_sensor.distance()
    return distance < 300

def check_environment():
    """Check both sensors and report status"""
    line = is_line_detected()
    obstacle = is_obstacle_close()
    
    if line and obstacle:
        return "LINE_AND_OBSTACLE"
    elif line:
        return "LINE_ONLY"
    elif obstacle:
        return "OBSTACLE_ONLY"
    else:
        return "CLEAR"

# Use the functions
while True:
    status = check_environment()
    print("Status:", status)
    hub.display.text(status)
    wait(500)