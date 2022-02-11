#   HW: Moving Agents
#   Author: Dylan Emerson
#   File: main.py

# Import pygame and pygame constants
import pygame
from pygame.locals import *

# Import custom classes
import Constants as Const       # "Constants" is too much to type a lot, so refer to it as Const
import PygameTime as pt
from Sheep import *
from Dog import *
from Vector import *

# Initialize pygame
pygame.init()

# Display mode properties
screen = pygame.display.set_mode((Const.DISPLAY_WIDTH, Const.DISPLAY_HEIGHT))

# Initialize dog
dog = Dog(Vector(Const.SCREEN_SIZE.x * 0.5, Const.SCREEN_SIZE.y * 0.5), Const.DOG_SPEED, Const.DOG_SIZE)

# Initialize enemies
sheepList = []

# Add 10 enemies randomly around the world
i = 0
while len(sheepList) < Const.WORLD_MAX_SHEEP:
   sheepList.append(Sheep(Vector(random.uniform(0, Const.DISPLAY_WIDTH - Const.SHEEP_SIZE),
                                random.uniform(0, Const.DISPLAY_HEIGHT - Const.SHEEP_SIZE)), Const.SHEEP_SPEED, Const.SHEEP_SIZE))

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
    dog.update(sheepList, screen)
    dog.draw(screen)

    #Draw enemies
    for sheep in sheepList:
        sheep.update(dog, screen)
        sheep.draw(screen)

    # Refresh screen
    pygame.display.flip()
    pt.clock.tick(Const.FRAME_RATE)