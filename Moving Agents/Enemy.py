#   HW: Moving Agents
#   Author: Dylan Emerson
#   File: Enemy.py

import pygame
import random

import Constants as Const
from Player import *
from Vector import *

class Enemy:

    # Enemy constructor
    def __init__(self, position, speed, size):
        self.position = position
        self.speed = speed
        self.size = size
        self.color = Const.ENEMY_COLOR
        self.center = self.calcCenter()
        self.target = Vector(random.randint(0, Const.DISPLAY_WIDTH), 
                             random.randint(0, Const.DISPLAY_HEIGHT))    # Get random initial target
        self.velocity = self.target     # Set velocity towards initial target
        self.last_target = 0    # Used for pygame timer

    # Print size, position, velocity, and center
    def __str__(self):
        print("Size:", str(self.size), "\nPosition:", str(self.position), "\nVelocity:", str(self.velocity),
            "\nCenter:", str(self.center))

    # Moves the enemy
    def update(self, player):

        # Calculate distance to player (flee range)
        playerDist = self.position - player.position

        # Flee if player is within range
        if (playerDist.length() < Const.ENEMY_FLEE_RANGE):
            self.velocity = playerDist
        # Wander if player is not in range
        else:
            self.velocity = self.wander()

        # Normalize velocity and move enemy
        self.velocity = self.velocity.normalize()           # Normalize velocity
        self.position += self.velocity * self.speed   # Scale it by a speed factor
        
    # Draws the enemy on screen
    def draw(self, screen):
        
        # Draw enemy
        pygame.draw.rect(screen, (self.color), pygame.Rect(self.position.x, self.position.y, self.size, self.size))

        # Draw line from center of enemy
        self.center = self.calcCenter()
        pygame.draw.line(screen, (Const.VI_COLOR), (self.center.x, self.center.y),
            (self.center.x + self.velocity.x * Const.VI_LENGTH, self.center.y + self.velocity.y * Const.VI_LENGTH))   # Draw line

    # Calculate the enemy's center
    def calcCenter(self):
        return Vector(self.position.x + 1 * (self.size * 0.5), self.position.y + 1 * (self.size * 0.5))

    # Wander behavior
    def wander(self):
        # Set up wander timer so the enemy doesn't change directions every frame
        # Waits Const.ENEMY_TICKS_TO_WAIT milliseconds before changing directions
        now = pygame.time.get_ticks()
        if (now - self.last_target > Const.ENEMY_TICKS_TO_WAIT):
            self.last_target = now

            # Set new target similar to previous move vector
            # From Dr. Dana's lecture 1/28/22
            self.target = Vector(-self.velocity.y, self.velocity.x) * random.uniform(-1, 1) * 0.2

            print(self.target)
        return self.velocity + self.target