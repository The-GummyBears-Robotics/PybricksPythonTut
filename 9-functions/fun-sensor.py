from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

hub = PrimeHub()

color_sensor = ColorSensor(Port.A)
distance_sensor = UltrasonicSensor(Port.B)

def is_line_detected():
    """Return True when reflection is dark enough to count as a black line."""
    reflection = color_sensor.reflection()
    return reflection < 20  # Black threshold

def is_obstacle_close():
    """Return True when object is closer than 300 mm."""
    distance = distance_sensor.distance()
    return distance < 300

def check_environment():
    """Combine smaller checks into one status label.

    This is decomposition: small single-purpose functions feed a higher-level
    decision function.
    """
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