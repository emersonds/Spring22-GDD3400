#   HW: Moving Agents
#   Author: Dylan Emerson
#   File: Agent.py

import pygame
import math
import random

import Constants as Const 
from Vector import *

class Agent:
    # Constructor
    def __init__(self, position, speed, size):
        self.position = position
        self.speed = speed
        self.size = size
        self.center = self.calcCenter()
        self.seeking = False
        self.fleeing = False
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size, self.size)
    
    def __str__(self):
        print("Size:", str(self.size), "\nPosition:", str(self.position), "\nVelocity:", str(self.velocity),
            "\nCenter:", str(self.center))

    def update(self):
        # Normalize velocity and move enemy
        self.velocity = self.velocity.normalize()           # Normalize velocity
        self.position += self.velocity * self.speed   # Scale it by a speed factor
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size, self.size)

        # Clamp agent into world bounds
        if (self.position.x < 0): self.position.x = 0
        if (self.position.x + self.size > Const.DISPLAY_WIDTH): self.position.x = Const.DISPLAY_WIDTH - self.size
        if (self.position.y < 0): self.position.y = 0
        if (self.position.y + self.size > Const.DISPLAY_HEIGHT): self.position.y = Const.DISPLAY_HEIGHT - self.size

    # Draw the agent and their velocity
    def draw(self, screen):
         
        # Draw agent
        pygame.draw.rect(screen, (self.color), pygame.Rect(self.position.x, self.position.y, self.size, self.size))

        # Draw line from agent center showing direction
        self.center = self.calcCenter()
        pygame.draw.line(screen, (Const.DEBUG_VELOCITY_COLOR), (self.center.x, self.center.y),
            (self.center.x + self.velocity.x * Const.DEBUG_VELOCITY_LENGTH, self.center.y + self.velocity.y * Const.DEBUG_VELOCITY_LENGTH))   # Draw line

    # Draw a line to another agent that self is seeking/fleeing from
    def drawSeekFlee(self, screen, lineTarget):
        if (self.seeking == True or self.fleeing == True):
            pygame.draw.line(screen, (Const.DEBUG_SEEKFLEE_COLOR), (self.center.x, self.center.y),
            (lineTarget.center.x, lineTarget.center.y))   # Draw line
    
    # Calculate the player's center
    def calcCenter(self):
        return Vector(self.position.x + 1 * (self.size / 2), self.position.y + 1 * (self.size / 2))

    def checkCollision(self, other):
        return (pygame.Rect.colliderect(self.rect, other.rect))