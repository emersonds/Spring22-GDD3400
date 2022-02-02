#   HW: Moving Agents
#   Author: Dylan Emerson
#   File: main.py

# Import pygame and pygame constants
import pygame
from pygame.locals import *

# Import custom classes
import Constants as Const       # "Constants" is too much to type a lot, so refer to it as Const
from Player import Player
from Vector import Vector

# Initialize pygame
pygame.init()

# Display mode properties
screen = pygame.display.set_mode((Const.DISPLAY_WIDTH, Const.DISPLAY_HEIGHT))
clock = pygame.time.Clock()

# Initialize player
player = Player(Vector(Const.SCREEN_SIZE.x / 2, Const.SCREEN_SIZE.y / 2), Const.PLAYER_SPEED, Const.PLAYER_SIZE)

# Gameplay loop
while True:
    # Quit the game when pygame is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Fill screen
    screen.fill(Const.BACKGROUND_COLOR)

    # Draw player
    player.update()
    player.draw(screen)

    # Refresh screen
    pygame.display.flip()
    clock.tick(Const.FRAME_RATE)