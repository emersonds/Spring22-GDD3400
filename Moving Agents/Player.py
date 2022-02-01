#   HW: Moving Agents
#   Author: Dylan Emerson
#   File: Player.py

from tkinter import CENTER
import pygame

import Constants as Const
from Vector import Vector

class Player:

    # Player constructor
    def __init__(self, position, speed, size):
        self.position = position
        self.speed = speed
        self.size = size
        self.velocity = Vector.zero()
        self.color = Const.PLAYER_COLOR
        self.center = self.calcCenter()

    # Print size, position, velocity, and center
    def __str__(self):
        print("Size:", str(self.size), "\nPosition:", str(self.position), "\nVelocity:", str(self.velocity),
            "\nCenter:", str(self.center))

    # Moves the player
    def update(self):

        # Initialize movement vector
        self.velocity = Vector.zero()                       # Zero out velocity so the player doesn't slide in between movements.

        # Set velocity and move player
        self.velocity = self.velocity.normalize()           # Normalize velocity
        self.position += self.velocity.scale(self.speed)    # Scale it by a speed factor
        
    # Draws the player on screen
    def draw(self, screen):
        
        # Draw player
        pygame.draw.rect(screen, (self.color), pygame.Rect(self.position.x, self.position.y, self.size, self.size))

        # Draw line from player showing direction
        pygame.draw.line(screen, (Const.VI_COLOR), (self.center.x, self.center.y),
            (self.center.x + self.velocity.x * Const.VI_LENGTH, self.center.y + self.velocity.y * Const.VI_LENGTH))   # Draw line

    # Calculate the player's center
    def calcCenter(self):
        return Vector(self.position.x + 1 * (self.size / 2), self.position.y + 1 * (self.size / 2))