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
            self.setVelocity()
    
    # Set random target in enemies list
    def setTarget(self, enemies):
        randIndex = random.randint(0, len(enemies) - 1)
        self.target = enemies[randIndex]
        self.targetSelected = True
