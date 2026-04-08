from pybricks.hubs import PrimeHub
from pybricks.tools import wait

# Displaying text.
#
# `char()` shows one character.
# `text()` scrolls a whole message across the screen.
#
# Try it:
# - Use your team name instead of "Hello, world!"
# - Add another `wait(...)` so the message has time to finish scrolling.

# Initialize the hub.
hub = PrimeHub()

# Display the letter A for two seconds.
hub.display.char("A")
wait(2000)

# Display text, one letter at a time.
hub.display.text("Hello, world!")