
# Twinkle Twinkle Little Star with `play_notes()`.
#
# This is a longer list, but it’s still the same idea:
# - a list of note strings
# - grouped into phrases with comments
# - played at a certain tempo
#
# Try it:
# - Change `tempo`
# - Copy just the first 2 lines of notes to make a shorter “demo version”

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

