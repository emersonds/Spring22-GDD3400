#   HW: Moving Agents
#   Author: Dylan Emerson
#   File: main.py

# Import pygame and pygame constants
import pygame
from pygame.locals import *

# Import custom classes
import Constants as Const       # "Constants" is too much to type a lot, so refer to it as Const
from Enemy import *
from Player import *
from Vector import *

# Initialize pygame
pygame.init()

# Display mode properties
screen = pygame.display.set_mode((Const.DISPLAY_WIDTH, Const.DISPLAY_HEIGHT))
clock = pygame.time.Clock()

# Initialize player
player = Player(Vector(Const.SCREEN_SIZE.x * 0.5, Const.SCREEN_SIZE.y * 0.5), Const.PLAYER_SPEED, Const.PLAYER_SIZE)

# Initialize enemies
enemies = []

# Add 10 enemies randomly around the world
i = 0
while len(enemies) < Const.WORLD_MAX_ENEMIES:
   enemies.append(Enemy(Vector(random.uniform(0, Const.DISPLAY_WIDTH - Const.ENEMY_SIZE),
                                random.uniform(0, Const.DISPLAY_HEIGHT - Const.ENEMY_SIZE)), Const.ENEMY_SPEED, Const.ENEMY_SIZE))

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
    player.update(enemies, screen)
    player.draw(screen)

    #Draw enemies
    for enemy in enemies:
        enemy.update(player, screen)
        enemy.draw(screen)

    # Refresh screen
    pygame.display.flip()
    clock.tick(Const.FRAME_RATE)