# Import pygame and pygame constants
import pygame
from pygame.locals import *

# Import custom classes Player and Vector
from Player import Player
from Vector import Vector

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

# Create player
player = Player(Vector(initX, initY), 5, square_size)

# Gameplay loop
while True:
    # Quit the game when pygame is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Fill screen
    screen.fill(background_color)

    # Move and draw the player
    player.update()
    player.draw(screen)

    # Fill screen and draw square
    #pygame.draw.rect(screen, square_color, pygame.Rect(initX, initY, square_width, square_height))

    # Refresh screen
    pygame.display.flip()
    clock.tick(60)