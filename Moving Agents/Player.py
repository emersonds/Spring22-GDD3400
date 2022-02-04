#   HW: Moving Agents
#   Author: Dylan Emerson
#   File: Player.py

import pygame
import math

import Constants as Const
from Enemy import *
from Vector import *

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
    def update(self, enemies):

        # Initialize movement vector
        self.velocity = Vector.zero()                       # Zero out velocity so the player doesn't slide in between movements.

        # Initialize closest enemy to first enemy in the list
        minDistance = math.sqrt((enemies[0].position.x - self.position.x)**2 + (enemies[0].position.y - self.position.y)**2)
        closestEnemy = enemies[0]
        # Check distance from each enemy
        for enemy in enemies:
            enemyDistance = math.sqrt((enemy.position.x - self.position.x)**2 + (enemy.position.y - self.position.y)**2)
            if (enemyDistance < minDistance):
                minDistance = enemyDistance
                closestEnemy = enemy

        # Set velocity and move player
        self.velocity = closestEnemy.position - self.position
        self.velocity = self.velocity.normalize()           # Normalize velocity
        self.position += self.velocity.scale(self.speed)    # Scale it by a speed factor
        
    # Draws the player on screen
    def draw(self, screen):
        
        # Draw player
        pygame.draw.rect(screen, (self.color), pygame.Rect(self.position.x, self.position.y, self.size, self.size))

        # Draw line from player center showing direction
        self.center = self.calcCenter()
        pygame.draw.line(screen, (Const.VI_COLOR), (self.center.x, self.center.y),
            (self.center.x + self.velocity.x * Const.VI_LENGTH, self.center.y + self.velocity.y * Const.VI_LENGTH))   # Draw line

    # Calculate the player's center
    def calcCenter(self):
        return Vector(self.position.x + 1 * (self.size / 2), self.position.y + 1 * (self.size / 2))