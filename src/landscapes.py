# Landscapes
# Assets by Freepik
from pygame import image, Surface, transform
from location import Location

# Define the game constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
# Landscapes thanks to freepik.com
LANDSCAPES: dict[Location, Surface] = {
    l: transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)) for l,img in
        # https://www.pygame.org/docs/tut/newbieguide.html#use-surface-convert
        {l:image.load(src).convert() for l,src in {
            Location.Forest: "assets/forest.jpg",
            Location.Mountain: "assets/mntn.jpg",
            Location.River: "assets/river.jpg",
            Location.Road: "assets/road.png",
        }.items()
    }.items()
}
