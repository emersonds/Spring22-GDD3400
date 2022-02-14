#   HW: Moving Agents
#   Author: Dylan Emerson
#   File: Agent.py

import pygame
import math

import Constants as Const
import PygameTime as pt
from Vector import *

class Agent:
    # Constructor
    def __init__(self, position, speed, size, image):
        super().__init__()
        self.position = position
        self.speed = speed
        self.size = size
        self.surf = pygame.Surface([size.x, size.y])
        self.image = pygame.image.load(image)
        self.center = self.calcCenter()
        self.orientation = 0
        self.seeking = False
        self.fleeing = False
        self.rect = self.image.get_rect()
        self.upperLeft = self.rect.topleft
        self.rectCenter = self.calcRectCenter()
    
    def __str__(self):
        print("Size:", str(self.size), "\nPosition:", str(self.position), "\nVelocity:", str(self.velocity),
            "\nCenter:", str(self.center))

    def update(self):
        # Normalize velocity and move agent
        self.velocity = self.velocity.normalize()           # Normalize velocity
        self.position += self.velocity * self.speed   # Move agent by velocity * speed

        # Rotate the agent
        self.orientation = math.atan2(self.velocity.x, self.velocity.y)
        self.orientation = math.degrees(self.orientation)
        self.orientation += 180

        # update agent rect
        self.updateRect()

    # Draw the agent and their velocity
    def draw(self, screen):
        
        # Draw agent
        self.upperLeft = self.rect.topleft
        self.surf = pygame.transform.rotate(self.image, self.orientation)
        screen.blit(self.surf, [self.upperLeft[0], self.upperLeft[1]])
        self.rectCenter = self.calcRectCenter()
        
        # Draw bounding rect
        boundingRect = self.surf.get_bounding_rect()
        boundingRect = boundingRect.move(self.upperLeft)
        pygame.draw.rect(screen, (0, 0, 0, 0), boundingRect, 1)

        # Get agent center
        self.center = self.calcCenter()
        # Draw line from agent center showing their velocity
        pygame.draw.line(screen, (Const.DEBUG_VELOCITY_COLOR), (self.rectCenter.x, self.rectCenter.y),
            (self.rectCenter.x + self.velocity.x * Const.DEBUG_VELOCITY_LENGTH, self.rectCenter.y + self.velocity.y * Const.DEBUG_VELOCITY_LENGTH))

        # Keep agent in world bounds and apply boundary force
        self.checkBoundaries(screen)

    # Draw a line to another agent that self is seeking/fleeing from
    def drawSeekFlee(self, screen, lineTarget):
        # Check if seeking or fleeing
        if (self.seeking == True or self.fleeing == True):
            # Draw seek/flee line
            pygame.draw.line(screen, (Const.DEBUG_SEEKFLEE_COLOR), (self.rectCenter.x, self.rectCenter.y),
            (lineTarget.rectCenter.x, lineTarget.rectCenter.y))
    
    # Calculate the agent's center
    def calcCenter(self):
        return self.position + Vector(1, 1) * (self.size * 0.5)

    def calcRectCenter(self):
        center = self.surf.get_bounding_rect().center
        return Vector(center[0] + self.upperLeft[0], center[1] + self.upperLeft[1])

    # Returns true if a collision with other is detected
    def checkCollision(self, other):
        return (pygame.Rect.colliderect(self.rect, other.rect))

    def updateRect(self):
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)

    def checkBoundaries(self, screen):

        # Clamp agent into world bounds
        if (self.position.x < 0): self.position.x = 0   # Left
        if (self.position.x + self.size.x > Const.DISPLAY_WIDTH): self.position.x = Const.DISPLAY_WIDTH - self.size.x   # Right
        if (self.position.y < 0): self.position.y = 0   # Top
        if (self.position.y + self.size.y > Const.DISPLAY_HEIGHT): self.position.y = Const.DISPLAY_HEIGHT - self.size.y # Bottom

        # If agent is getting too close to a boundary, push agent away
        # Top
        if (self.rect.top < Const.WORLD_MIN_DISTANCE):  
            self.velocity.y += Const.WORLD_BOUNDARY_FORCE * self.speed * pt.deltaTime
            pygame.draw.line(screen, Const.DEBUG_SEEKFLEE_COLOR, (self.rect.centerx, 0),
                            self.rect.center)

        # Bottom
        if (self.rect.bottom > (Const.DISPLAY_HEIGHT - Const.WORLD_MIN_DISTANCE)):  
            self.velocity.y += -Const.WORLD_BOUNDARY_FORCE * self.speed * pt.deltaTime
            pygame.draw.line(screen, Const.DEBUG_SEEKFLEE_COLOR, (self.rect.centerx, Const.DISPLAY_HEIGHT),
                            self.rect.center)

        # Left
        if (self.rect.left < Const.WORLD_MIN_DISTANCE):  
            self.velocity.x += Const.WORLD_BOUNDARY_FORCE * self.speed * pt.deltaTime
            pygame.draw.line(screen, Const.DEBUG_SEEKFLEE_COLOR, (0, self.rect.centery),
                            self.rect.center)

        # Right                    
        if (self.rect.right > (Const.DISPLAY_WIDTH - Const.WORLD_MIN_DISTANCE)):  
            self.velocity.x += -Const.WORLD_BOUNDARY_FORCE * self.speed * pt.deltaTime
            pygame.draw.line(screen, Const.DEBUG_SEEKFLEE_COLOR, (Const.DISPLAY_WIDTH, self.rect.centery),
                            self.rect.center)