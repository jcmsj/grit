# Example file showing a basic pygame "game loop"
import pygame
from landscapes import load_landscapes, SCREEN_HEIGHT, SCREEN_WIDTH, asset
from location import Location
from state import State

pygame.init()

# Create the game window
pygame.display.set_caption("Grit")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load the buttons
button_1 = pygame.image.load(asset("drawing.svg"))# ("button_1.png")
button_2 = pygame.image.load(asset("drawing.svg"))# ("button_2.png")
button_3 = pygame.image.load(asset("drawing.svg"))# ("button_3.png")

# Set the button positions
button_1_x = 100
button_1_y = 100
button_2_x = 300
button_2_y = 100
button_3_x = 500
button_3_y = 100

# Define the game constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
# Landscapes thanks to freepik.com
LANDSCAPES = load_landscapes()
state = State()
# Start the game loop
while True:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # Handle other events here
        # Check if the buttons have been clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Detect button clicks
            if button_1.get_rect(x=button_1_x, y=button_1_y).collidepoint(event.pos):
                state.location = Location.Forest
            elif button_2.get_rect(x=button_2_x, y=button_2_y).collidepoint(event.pos):
                state.location = Location.Mountain
            elif button_3.get_rect(x=button_3_x, y=button_3_y).collidepoint(event.pos):
                state.location = Location.River

    # Draw the game screen
    screen.fill((0, 0, 0))

    # Draw the location image, scale it to the screen size
    # screen.blit(LANDSCAPES[state.location],
    screen.blit(LANDSCAPES[state.location], (0, 0))

    screen.blit(button_1, (button_1_x, button_1_y))
    screen.blit(button_2, (button_2_x, button_2_y))
    screen.blit(button_3, (button_3_x, button_3_y))

    # Update the display
    pygame.display.flip()
