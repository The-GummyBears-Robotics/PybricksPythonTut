
# The play_notes() method plays a sequence of musical notes. 

from pybricks.hubs import PrimeHub

hub = PrimeHub()
hub.speaker.volume(80)

hub.speaker.play_notes([
    # "Happy birthday to you"
    'G4/8.', 'G4/16', 'A4/4', 'G4/4', 'C5/4', 'B4/2',
    # "Happy birthday to you"
    'G4/8.', 'G4/16', 'A4/4', 'G4/4', 'D5/4', 'C5/2',
    # "Happy birthday dear [name]"
    'G4/8.', 'G4/16', 'G5/4', 'E5/4', 'C5/4', 'B4/4', 'A4/2',
    # "Happy birthday to you"
    'F5/8.', 'F5/16', 'E5/4', 'C5/4', 'D5/4', 'C5/2',
], tempo=90)