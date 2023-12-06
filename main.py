"""Main file"""
import sys

from game.game import Game

HINTS = False
AUTO = False

def to_lower(data: str):
    """Return lower case version of the passed string"""
    return data.lower()

# Iterate over args, skipping the first since that's the file,
# and convert each to lower case.
# Converts the map object back to a list.
args = list(map(to_lower, sys.argv[1:]))

# For simple arugments, this will work. However,
# for more complex arugments, I would recommend the "argparse" module/library.
if len(args) > 0:
    if "hints" in args:
        HINTS = True
    if "auto" in args:
        AUTO = True

# Initialize the game
game = Game(HINTS, AUTO)

try:
    game.start()
except KeyboardInterrupt:
    print()
    print()
    print("User quit; Thanks for playing!")
