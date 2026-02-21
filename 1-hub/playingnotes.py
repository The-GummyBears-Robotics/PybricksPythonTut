
# The play_notes() method plays a sequence of musical notes. 

from pybricks.hubs import PrimeHub

hub = PrimeHub()

hub.speaker.volume(80)

# Play "Mary Had a Little Lamb" using play_notes()
# Format: 'NOTE_OCTAVE/DURATION'  e.g. 'E4/4' = E in octave 4, quarter note
hub.speaker.play_notes([
    'E4/4', 'D4/4', 'C4/4', 'D4/4',
    'E4/4', 'E4/4', 'E4/2',
    'D4/4', 'D4/4', 'D4/2',
    'E4/4', 'G4/4', 'G4/2',
    'E4/4', 'D4/4', 'C4/4', 'D4/4',
    'E4/4', 'E4/4', 'E4/4', 'E4/4',
    'D4/4', 'D4/4', 'E4/4', 'D4/4',
    'C4/1',
], tempo=120)