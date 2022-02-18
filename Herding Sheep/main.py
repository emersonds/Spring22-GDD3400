#   HW: Moving Agents
#   Author: Dylan Emerson
#   File: main.py

# Import pygame and pygame constants
import pygame
from pygame.locals import *

# Import custom classes
import Constants as Const       # "Const" is too much to type a lot, so refer to it as Const
import PygameTime as pt
from Sheep import *
from Dog import *
from Vector import *

# Initialize pygame
pygame.init()

# Display mode properties
screen = pygame.display.set_mode((Const.DISPLAY_WIDTH, Const.DISPLAY_HEIGHT))

# Define function for handling debugging (lines, forces, etc.)
def handleDebugging(event):        
    # Handle the Debugging for Forces
    if event.type == pygame.KEYUP:

        # Toggle Dog Influence
        if event.key == pygame.K_1:
            Const.ENABLE_DOG = not Const.ENABLE_DOG
            print("Toggle Dog Influence", Const.ENABLE_DOG)

        # Toggle Alignment Influence
        if event.key == pygame.K_2: 
            Const.ENABLE_ALIGNMENT = not Const.ENABLE_ALIGNMENT
            print("Toggle Alignment Influence", Const.ENABLE_ALIGNMENT)

        # Toggle Separation Influence
        if event.key == pygame.K_3: 
            Const.ENABLE_SEPARATION = not Const.ENABLE_SEPARATION
            print("Toggle Separation Influence", Const.ENABLE_SEPARATION)

        # Toggle Cohesion Influence
        if event.key == pygame.K_4: 
            Const.ENABLE_COHESION = not Const.ENABLE_COHESION
            print("Toggle Cohesion Influence", Const.ENABLE_COHESION)

        # Toggle Boundary Influence
        if event.key == pygame.K_5: 
            Const.ENABLE_BOUNDARIES = not Const.ENABLE_BOUNDARIES
            print("Toggle Boundary Influence", Const.ENABLE_BOUNDARIES)

        # Toggle Dog Influence Lines
        if event.key == pygame.K_6: 
            Const.DEBUG_DOG_INFLUENCE = not Const.DEBUG_DOG_INFLUENCE
            print("Toggle Dog Influence Lines", Const.DEBUG_DOG_INFLUENCE)
    
        # Toggle Velocity Lines
        if event.key == pygame.K_7: 
            Const.DEBUG_VELOCITY = not Const.DEBUG_VELOCITY
            print("Toggle Velocity Lines", Const.DEBUG_VELOCITY)

        # Toggle Neighbor Lines
        if event.key == pygame.K_8: 
            Const.DEBUG_NEIGHBORS = not Const.DEBUG_NEIGHBORS
            print("Toggle Neighbor Lines", Const.DEBUG_NEIGHBORS)

        # Toggle Boundary Force Lines
        if event.key == pygame.K_9: 
            Const.DEBUG_BOUNDARIES = not Const.DEBUG_BOUNDARIES
            print("Toggle Boundary Force Lines", Const.DEBUG_BOUNDARIES)

        # Toggle Bounding Box Lines
        if event.key == pygame.K_0: 
            Const.DEBUG_BOUNDING_RECTS = not Const.DEBUG_BOUNDING_RECTS
            print("Toggle Bounding Box Lines", Const.DEBUG_BOUNDING_RECTS)

# Initialize dog
dog = Dog(Vector(Const.SCREEN_SIZE.x * 0.5, Const.SCREEN_SIZE.y * 0.5), Const.DOG_SPEED,
        Vector(Const.AGENT_WIDTH, Const.AGENT_HEIGHT), "dog.png")

# Initialize enemies
sheepList = []

# Add 10 enemies randomly around the world
i = 0
while len(sheepList) < Const.WORLD_MAX_SHEEP:
   sheepList.append(Sheep(Vector(random.uniform(0, Const.DISPLAY_WIDTH - Const.AGENT_HEIGHT),
                                random.uniform(0, Const.DISPLAY_HEIGHT - Const.AGENT_HEIGHT)),
                                Const.SHEEP_SPEED, Vector(Const.AGENT_WIDTH, Const.AGENT_HEIGHT),
                                "sheep.png"))

# Gameplay loop
while True:

    # Quit the game when pygame is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        else:
            handleDebugging(event)


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