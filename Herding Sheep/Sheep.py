#   HW: Moving Agents
#   Author: Dylan Emerson
#   File: Sheep.py

import pygame
import random

import Constants as Const
import PygameTime as pt
from Agent import Agent
from Vector import *

class Sheep(Agent):

    # Enemy constructor
    def __init__(self, position, speed, size, sprite):
        self.color = Const.SHEEP_COLOR
        self.target = Vector(random.randint(0, Const.DISPLAY_WIDTH), 
                             random.randint(0, Const.DISPLAY_HEIGHT))    # Get random initial target
        self.velocity = self.target     # Set velocity towards initial target
        self.last_target = 0    # Used for pygame timer
        self.last_neighborhood = 0  # Used for neighborhood timer
        self.tagged = False     # Used for movement checking
        self.image = sprite
        self.neighbors = []
        self.neighborVector = Vector.zero()

        # Call parent constructor
        super().__init__(position, speed, size, sprite)

    # Moves the enemy
    def update(self, dog, screen):

        # Get direction to player/flee vector
        dogDist = self.position - dog.position

        # Flocking forces
        self.alignment = self.computeAlignment()
        self.cohesion = self.computeCohesion()
        self.separation = self.computeSeparation()

        # Flee if player is within range
        if (dogDist.length() < Const.SHEEP_FLEE_RANGE and Const.ENABLE_DOG):
            self.velocity += self.flee(dogDist)
            if Const.DEBUG_DOG_INFLUENCE:
                self.drawSeekFlee(screen, dog)
        # Wander if player is not in range
        else:
            self.forces = self.alignment * Const.SHEEP_ALIGNMENT_WEIGHT * Const.ENABLE_ALIGNMENT \
                + self.cohesion * Const.SHEEP_COHESION_WEIGHT * Const.ENABLE_COHESION \
                + self.separation * Const.SHEEP_SEPARATION_WEIGHT * Const.ENABLE_SEPARATION
            self.forces.normalize()
            self.velocity += self.forces * pt.deltaTime * Const.SHEEP_SPEED

        # Check for collisions
        self.collided = self.checkCollision(dog)
        if (self.collided == True):
            self.tagged = True

        # Call parent update
        super().update()

    def draw(self, screen):
        if Const.DEBUG_NEIGHBORS:
            for neighbor in self.neighbors:
                pygame.draw.line(screen, Const.DEBUG_NEIGHBOR_COLOR, (self.rectCenter.x, self.rectCenter.y),
                (neighbor.rect.center[0], neighbor.rect.center[1]))

        super().draw(screen)

    # # Wander behavior
    # def wander(self):
    #     # Set up wander timer so the enemy doesn't change directions every frame
    #     # Waits Const.ENEMY_TICKS_TO_WAIT milliseconds before changing directions
    #     now = pygame.time.get_ticks()
    #     if (now - self.last_target > Const.SHEEP_TICKS_TO_WAIT):
    #         self.last_target = now

    #         # Set new target similar to previous move vector
    #         # From Dr. Dana's lecture 1/28/22
    #         self.target = Vector(-self.velocity.y, self.velocity.x) * random.uniform(-1, 1) * Const.SHEEP_ROTATION_SCALAR
    #     self.appliedForce = self.target * Const.SHEEP_WANDER_WEIGHT
    #     return self.appliedForce.normalize() * pt.deltaTime * Const.SHEEP_SPEED

    # Flee behavior
    def flee(self, dogDist):
        # set self to fleeing and apply flee force
        self.fleeing = True
        self.appliedForce = dogDist * Const.SHEEP_FLEE_WEIGHT
        return self.appliedForce.normalize() * pt.deltaTime * Const.SHEEP_SPEED

    def calculateNeighbors(self, herd):
        # Set up neighborhood timer
        # Waits 16.33 milliseconds (Const.SHEEP_NEIGHBORHOOD_TICKS) then loops
        # through potential neighbors
        now = pygame.time.get_ticks()
        if (now - self.last_neighborhood > Const.SHEEP_NEIGHBORHOOD_TICKS):
            self.last_neighborhood = now

            # Remove all previous neighbors
            self.neighbors.clear()


            # Calculate neighbors
            for neighbor in herd:
                # If the current neighbor isn't the same sheep
                if (neighbor != self):
                    # Get vector from self to neighbor
                    neighborDist = neighbor.position - self.position
                    if (neighborDist.length() < Const.SHEEP_NEIGHBOR_RADIUS):
                        self.neighbors.append(neighbor)

# Computes alignment flocking behavior
    def computeAlignment(self):
        # Set neighbor count variable
        neighborCount = len(self.neighbors)

        neighborVector = Vector.zero()

        # Make sure neighbor count isn't 0
        if neighborCount == 0:
            return neighborVector
        elif neighborCount > 0:
            for neighbor in self.neighbors:
                # Alignment behavior adds neighbor velocity to computation vector
                neighborVector += neighbor.velocity

            # Divide computation by neighbor vector and normalize to get final vector
            neighborVector.x /= neighborCount
            neighborVector.y /= neighborCount
            neighborVector.normalize()
            return neighborVector

    # Computes cohesion flocking behavior
    def computeCohesion(self):
        # Set neighbor count variable
        neighborCount = len(self.neighbors)

        neighborVector = Vector.zero()

        # Make sure neighbor count isn't 0
        if neighborCount == 0:
            return neighborVector
        elif neighborCount > 0:
            for neighbor in self.neighbors:
                # Cohesion behavior adds neighbor position to computation vector
                neighborVector += neighbor.position
            
            # Divide computation by neighbor vector and normalize to get final vector
            neighborVector.x /= neighborCount
            neighborVector.y /= neighborCount
            neighborVector = Vector(neighborVector.x - self.position.x,
                                            neighborVector.y - self.position.y)
            neighborVector.normalize()
            return neighborVector

    # Computes separation flocking behavior
    def computeSeparation(self):
        # Set neighbor count variable
        neighborCount = len(self.neighbors)

        neighborVector = Vector.zero()

        # Make sure neighbor count isn't 0
        if neighborCount == 0:
            return neighborVector
        elif neighborCount > 0:
            for neighbor in self.neighbors:
                # Separation behavior adds neighbor distance to computation vector
                neighborVector += neighbor.position - self.position
            
            # Divide computation by neighbor vector,
            # Negate the vector to steer away from neighbors,
            # then normalize to get final vector
            neighborVector.x /= neighborCount
            neighborVector.y /= neighborCount
            neighborVector *= -1
            neighborVector.normalize()
            return neighborVector