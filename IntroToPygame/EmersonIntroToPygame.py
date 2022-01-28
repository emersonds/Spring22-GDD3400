# Import pygame and pygame constants
import pygame
from pygame.locals import *

# Initialize pygame
pygame.init()

# Display mode properties
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
background_color = (100, 149, 237)

# Base square
square_width = 60
square_height = 60
x = 30
y = 30
square_color = (27, 38, 79)

# Gameplay loop
while True:
    # Quit the game when pygame is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Move the square
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]: y -= 1      # Up (positive y is down)
    if pressed[pygame.K_s]: y += 1      # Down
    if pressed[pygame.K_a]: x -= 1      # Left
    if pressed[pygame.K_d]: x += 1      # Right

    # Fill screen and draw square
    screen.fill(background_color)
    pygame.draw.rect(screen, square_color, pygame.Rect(x, y, square_width, square_height))

    # Refresh screen
    pygame.display.flip()
    clock.tick(60)