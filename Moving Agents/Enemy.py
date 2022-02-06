#   HW: Moving Agents
#   Author: Dylan Emerson
#   File: Enemy.py

import pygame
import random

import Constants as Const
from Agent import Agent
from Player import *
from Vector import *

class Enemy(Agent):

    # Enemy constructor
    def __init__(self, position, speed, size):
        self.color = Const.ENEMY_COLOR
        self.target = Vector(random.randint(0, Const.DISPLAY_WIDTH), 
                             random.randint(0, Const.DISPLAY_HEIGHT))    # Get random initial target
        self.velocity = self.target     # Set velocity towards initial target
        self.last_target = 0    # Used for pygame timer

        super().__init__(position, speed, size)

    # Moves the enemy
    def update(self, player, screen):

        # Calculate distance to player (flee range)
        playerDist = self.position - player.position

        # Flee if player is within range
        if (playerDist.length() < Const.ENEMY_FLEE_RANGE):
            self.velocity = playerDist
            self.fleeing = True
            self.drawSeekFlee(screen, player)
        # Wander if player is not in range
        else:
            self.velocity = self.wander()

        self.setVelocity()

    # Wander behavior
    def wander(self):
        # Set up wander timer so the enemy doesn't change directions every frame
        # Waits Const.ENEMY_TICKS_TO_WAIT milliseconds before changing directions
        now = pygame.time.get_ticks()
        if (now - self.last_target > Const.ENEMY_TICKS_TO_WAIT):
            self.last_target = now

            # Set new target similar to previous move vector
            # From Dr. Dana's lecture 1/28/22
            self.target = Vector(-self.velocity.y, self.velocity.x) * random.uniform(-1, 1) * Const.ENEMY_ROTATION_SCALAR
        return self.velocity + self.target