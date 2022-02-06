#   HW: Moving Agents
#   Author: Dylan Emerson
#   File: Player.py

import pygame
import math
import random

import Constants as Const
from Agent import Agent
from Enemy import *
from Vector import *

class Player(Agent):

    # Player constructor
    def __init__(self, position, speed, size):
        self.color = Const.PLAYER_COLOR
        self.velocity = Vector.zero()
        self.targetSelected = False
        super().__init__(position, speed, size)
        self.collided = False

    # Moves the player
    def update(self, enemies, screen):

        # Target random enemy
        if (self.targetSelected == False):
            self.setTarget(enemies)
        else:
            # Set velocity and move player
            self.seeking = True
            self.drawSeekFlee(screen, self.target)
            self.velocity = self.target.position - self.position
        
        # Check for collisions
        self.collided = self.checkCollision(self.target)
        if (self.collided == True):
            self.setTarget(enemies)

        super().update()
    
    # Set random target in enemies list
    def setTarget(self, enemies):
        self.target = self  # If no target is found, set target to self to freeze movement
        # Find a random target
        i = 0
        while i < len(enemies):
            randIndex = random.randint(0, len(enemies) - 1)
            # If random target hasn't been tagged, set target
            if (enemies[randIndex].tagged == False):
                self.target = enemies[randIndex]
                self.targetSelected = True
                break
            # Loop until a target has been set or there are no targets remaining
            i += 1
