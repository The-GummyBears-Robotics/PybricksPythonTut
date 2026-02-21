
# The play_notes() method plays a sequence of musical notes. 

from pybricks.hubs import PrimeHub

hub = PrimeHub()
hub.speaker.volume(80)

hub.speaker.play_notes([
    # "Twinkle twinkle"
    'C4/4', 'C4/4', 'G4/4', 'G4/4',
    # "little star"
    'A4/4', 'A4/4', 'G4/2',
    # "how I wonder"
    'F4/4', 'F4/4', 'E4/4', 'E4/4',
    # "what you are"
    'D4/4', 'D4/4', 'C4/2',
    # "up above the world so high"
    'G4/4', 'G4/4', 'F4/4', 'F4/4',
    'E4/4', 'E4/4', 'D4/2',
    # "like a diamond in the sky"
    'G4/4', 'G4/4', 'F4/4', 'F4/4',
    'E4/4', 'E4/4', 'D4/2',
    # "twinkle twinkle little star"
    'C4/4', 'C4/4', 'G4/4', 'G4/4',
    'A4/4', 'A4/4', 'G4/2',
    # "how I wonder what you are"
    'F4/4', 'F4/4', 'E4/4', 'E4/4',
    'D4/4', 'D4/4', 'C4/2',
], tempo=120)

