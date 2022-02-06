#   HW: Moving Agents
#   Author: Dylan Emerson
#   File: Agent.py

import pygame
import math
import random

import Constants as Const 
from Vector import *

class Agent:
    def __init__(self, position, speed, size):
        self.position = position
        self.speed = speed
        self.size = size
        self.center = self.calcCenter()
    
    def __str__(self):
        print("Size:", str(self.size), "\nPosition:", str(self.position), "\nVelocity:", str(self.velocity),
            "\nCenter:", str(self.center))

    def draw(self, screen):
         
        # Draw agent
        pygame.draw.rect(screen, (self.color), pygame.Rect(self.position.x, self.position.y, self.size, self.size))

        # Draw line from agent center showing direction
        self.center = self.calcCenter()
        pygame.draw.line(screen, (Const.VI_COLOR), (self.center.x, self.center.y),
            (self.center.x + self.velocity.x * Const.VI_LENGTH, self.center.y + self.velocity.y * Const.VI_LENGTH))   # Draw line
    
    # Calculate the player's center
    def calcCenter(self):
        return Vector(self.position.x + 1 * (self.size / 2), self.position.y + 1 * (self.size / 2))