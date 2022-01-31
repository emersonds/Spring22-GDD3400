#   HW: Moving Agents
#   Author: Dylan Emerson
#   File: main.py

# Import pygame and pygame constants
import pygame
from pygame.locals import *

# Import custom classes


# Initialize pygame
pygame.init()

# Display mode properties
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
background_color = (100, 149, 237)

# Base square
square_size = 60
initX = 30
initY = 30
square_color = (27, 38, 79)

# Gameplay loop
while True:
    # Quit the game when pygame is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Fill screen
    screen.fill(background_color)

    # Refresh screen
    pygame.display.flip()
    clock.tick(60)