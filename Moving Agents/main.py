#   HW: Moving Agents
#   Author: Dylan Emerson
#   File: main.py

# Import pygame and pygame constants
import pygame
from pygame.locals import *

# Import custom classes
import Constants

# Initialize pygame
pygame.init()

# Display mode properties
screen = pygame.display.set_mode((Constants.DISPLAY_WIDTH, Constants.DISPLAY_HEIGHT))
clock = pygame.time.Clock()

# Gameplay loop
while True:
    # Quit the game when pygame is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Fill screen
    screen.fill(Constants.BACKGROUND_COLOR)

    # Refresh screen
    pygame.display.flip()
    clock.tick(Constants.FRAME_RATE)