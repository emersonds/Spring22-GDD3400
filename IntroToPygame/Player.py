import pygame
from Vector import Vector

class Player:

    # Player constructor
    def __init__(self, position, speed, size):
        self.position = position
        self.speed = speed
        self.velocity = Vector.zero()
        self.size = size

    # Moves the player
    def update(self):

        # Initialize movement vector
        move = Vector.zero()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]: move.y -= 1      # Up (positive y is down)
        if pressed[pygame.K_s]: move.y += 1      # Down
        if pressed[pygame.K_a]: move.x -= 1      # Left
        if pressed[pygame.K_d]: move.x += 1      # Right

        # Set velocity and move player
        self.velocity = move.normalize()    # Velocity is normalized movement vector
        self.position = self.velocity * self.speed
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size, self.size)
        
    # Draws the player on screen
    def draw(self, screen):
        pygame.draw.rect(screen, (27, 38, 79), pygame.Rect(self.position.x, self.position.y, self.size, self.size))

