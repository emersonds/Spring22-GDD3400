#   HW: Moving Agents
#   Author: Dylan Emerson
#   File: Dog.py

import random

import Constants as Const
import PygameTime as pt
from Agent import Agent
from Vector import *

class Dog(Agent):

    # Player constructor
    def __init__(self, position, speed, size, sprite):
        self.color = Const.DOG_COLOR
        self.velocity = Vector.zero()
        self.targetSelected = False     # Used for setting targets
        self.collided = False   # Used for changing targets

        # Call parent constructor
        super().__init__(position, speed, size, sprite)

    # Moves the player
    def update(self, sheepList, screen):

        # Target random enemy
        if (self.targetSelected == False):
            self.setTarget(sheepList)
        # Seek target enemy
        else:
            # Set velocity and move player
            self.seeking = True
            self.drawSeekFlee(screen, self.target)
            self.velocity += self.setForce()
        
        # Check for collisions
        self.collided = self.checkCollision(self.target)
        # Change targets on collision with target
        if (self.collided == True):
            self.setTarget(sheepList)

        # Call parent update
        super().update()
    
    # Set random target in enemies list
    def setTarget(self, sheepList):
        # If no target is found, set target to self to freeze movement
        self.target = self

        # Find a random target
        i = 0
        while i < len(sheepList):
            randIndex = random.randint(0, len(sheepList) - 1)
            # Check if potential target has been tagged
            if (sheepList[randIndex].tagged == False):
                # If random target hasn't been tagged, set target
                self.target = sheepList[randIndex]
                self.targetSelected = True
                break
            # Loop until a target has been set or there are no targets remaining
            i += 1
        
        # No targets left
        if (self.target == self):
            print("No targets remaining.")

    # Calculate direction and applied force
    def setForce(self):
        self.direction = (self.target.position - self.position).normalize()
        self.appliedForce = self.direction * Const.DOG_SEEK_WEIGHT
        return self.appliedForce.normalize() * pt.deltaTime * Const.DOG_SPEED