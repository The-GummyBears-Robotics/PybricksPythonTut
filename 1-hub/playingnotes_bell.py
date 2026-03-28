
# Playing a song with `play_notes()`.
#
# The comments inside the list label each lyric phrase, so students can
# connect code → music.
#
# Try it:
# - Lower `tempo` to slow it down (or raise it to speed up).
# - Change one note and listen for how it sounds “wrong” (debugging by ear!).

from pybricks.hubs import PrimeHub

hub = PrimeHub()
hub.speaker.volume(80)

hub.speaker.play_notes([
    # "Jingle bells, jingle bells"
    'E4/4', 'E4/4', 'E4/2',
    'E4/4', 'E4/4', 'E4/2',
    # "jingle all the way"
    'E4/4', 'G4/4', 'C4/4', 'D4/4', 'E4/1',
    # "Oh what fun it is to ride"
    'F4/4', 'F4/4', 'F4/4', 'F4/4',
    'F4/4', 'E4/4', 'E4/4', 'E4/4',
    # "in a one horse open sleigh"
    'E4/4', 'D4/4', 'D4/4', 'E4/4', 'D4/2', 'G4/2',
], tempo=140)