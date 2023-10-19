# Landscapes
# Assets by Freepik
from pygame import image, Surface, transform
from location import Location
from os import path
# Define the game constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

BASE = path.dirname(path.abspath(__file__))
asset = lambda file: path.join(BASE, "../assets", file)
# Landscapes thanks to freepik.com
def load_landscapes() -> dict[Location, Surface]:
    return {
        l: transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)) for l,img in
            # https://www.pygame.org/docs/tut/newbieguide.html#use-surface-convert
            {l:image.load(asset(src)) for l,src in {
                Location.Forest: "forest.jpg",
                Location.Mountain: "mntn.jpg",
                Location.River: "river.jpg",
                Location.Road: "road.png",
            }.items()
        }.items()
    }
