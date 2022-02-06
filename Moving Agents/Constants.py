#   HW: Moving Agents
#   Author: Dylan Emerson
#   File: Constants.py

from Vector import *

# Screen constants
BACKGROUND_COLOR = (100, 149, 237)
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
SCREEN_SIZE = Vector(DISPLAY_WIDTH, DISPLAY_HEIGHT)
FRAME_RATE = 60

# Player constants
PLAYER_COLOR = (246, 240, 136)
PLAYER_SIZE = 10
PLAYER_SPEED = 1.5

# Enemy constants
ENEMY_COLOR = (89, 205, 144)
ENEMY_SIZE = 10
ENEMY_SPEED = 1
ENEMY_FLEE_RANGE = 100
ENEMY_TICKS_TO_WAIT = 800
ENEMY_ROTATION_SCALAR = 0.1

# Velocity Indicator (VI) constants
VI_COLOR = (0, 0, 255)
VI_LENGTH = 15