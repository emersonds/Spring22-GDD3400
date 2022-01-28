import pygame
from Vector import Vector

class Player:

    # Default player speed
    speed = 3

    # Player constructor
    def __init__(self, position, velocity, size):
        self.position = position
        self.velocity = velocity
        self.size = size

    # Moves the player
    def update(self):

        # Initialize movement vector
        self.velocity = Vector.zero()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]: self.velocity.y -= 1      # Up (positive y is down)
        if pressed[pygame.K_s]: self.velocity.y += 1      # Down
        if pressed[pygame.K_a]: self.velocity.x -= 1      # Left
        if pressed[pygame.K_d]: self.velocity.x += 1      # Right

        # Set velocity and move player
        self.velocity = self.velocity.normalize()            # Normalize velocity
        self.position += self.velocity.scale(self.speed)     # Scale it by a speed factor
        #self.rect = pygame.Rect(self.position.x, self.position.y, self.size, self.size)
        
    # Draws the player on screen
    def draw(self, screen):
        # Draw player
        pygame.draw.rect(screen, (27, 38, 79), pygame.Rect(self.position.x, self.position.y, self.size, self.size))

        # Draw line from player showing direction
        center = Vector(self.position.x + 1 * (self.size / 2), self.position.y + 1 * (self.size / 2))     # Get center of player
        pygame.draw.line(screen, (255, 0, 0), (center.x, center.y), (center.x + self.velocity.x * 100, \
            center.y + self.velocity.y * 100))   # Draw line

