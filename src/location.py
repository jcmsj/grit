from enum import Enum
from random import choices, choice

class Location(Enum):
    Road = 0
    Mountain = 1
    River = 2
    Forest = 3

    def random():
        # weighted random pick, make Road extremely unlikely
        return choice(choices(LOCATIONS, weights=[5, 25, 32, 38]))
LOCATIONS = list(Location)
