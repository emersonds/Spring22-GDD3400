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
    def __init__(self, position, speed, size):
        self.color = Const.SHEEP_COLOR
        self.target = Vector(random.randint(0, Const.DISPLAY_WIDTH), 
                             random.randint(0, Const.DISPLAY_HEIGHT))    # Get random initial target
        self.velocity = self.target     # Set velocity towards initial target
        self.last_target = 0    # Used for pygame timer
        self.tagged = False     # Used for movement checking

        # Call parent constructor
        super().__init__(position, speed, size)

    # Moves the enemy
    def update(self, dog, screen):

        # Get direction to player/flee vector
        dogDist = self.position - dog.position

        # Check if tagged, wander/flee if not tagged
        if (self.tagged == False):
            # Flee if player is within range
            if (dogDist.length() < Const.SHEEP_FLEE_RANGE):
                self.velocity = self.flee(dogDist)
                self.drawSeekFlee(screen, dog)
            # Wander if player is not in range
            else:
                self.velocity += self.wander()
        # Stand in place if tagged
        else:
            self.velocity = Vector.zero()

        # Check for collisions
        self.collided = self.checkCollision(dog)
        if (self.collided == True):
            self.tagged = True

        # Call parent update
        super().update()

    # Wander behavior
    def wander(self):
        # Set up wander timer so the enemy doesn't change directions every frame
        # Waits Const.ENEMY_TICKS_TO_WAIT milliseconds before changing directions
        now = pygame.time.get_ticks()
        if (now - self.last_target > Const.SHEEP_TICKS_TO_WAIT):
            self.last_target = now

            # Set new target similar to previous move vector
            # From Dr. Dana's lecture 1/28/22
            self.target = Vector(-self.velocity.y, self.velocity.x) * random.uniform(-1, 1) * Const.SHEEP_ROTATION_SCALAR
        self.appliedForce = self.target * Const.SHEEP_WANDER_WEIGHT
        return self.appliedForce.normalize() * pt.deltaTime * Const.SHEEP_SPEED

    # Flee behavior
    def flee(self, dogDist):
        # Calculate distance to player (flee range)

        self.fleeing = True
        self.appliedForce = dogDist * Const.SHEEP_FLEE_WEIGHT
        return self.appliedForce.normalize() * pt.deltaTime * Const.SHEEP_SPEED