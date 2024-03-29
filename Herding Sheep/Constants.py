#   HW: Moving Agents
#   Author: Dylan Emerson
#   File: Constants.py

from Vector import *

# Screen constants
BACKGROUND_COLOR = (100, 149, 237)
DISPLAY_WIDTH = 1024
DISPLAY_HEIGHT = 768
SCREEN_SIZE = Vector(DISPLAY_WIDTH, DISPLAY_HEIGHT)
FRAME_RATE = 60

# World constants
WORLD_MAX_SHEEP = 100
WORLD_MIN_DISTANCE = 25
WORLD_BOUNDARY_FORCE = 2

# Agent constants
AGENT_WIDTH = 16
AGENT_HEIGHT = 32

# Dog constants
DOG_COLOR = (246, 240, 136)
DOG_SPEED = 1
DOG_SEEK_WEIGHT = 2

# Sheep constants
SHEEP_COLOR = (89, 205, 144)
SHEEP_SPEED = 0.75
SHEEP_FLEE_RANGE = 100
SHEEP_WANDER_TICKS = 800        # 8 milliseconds
SHEEP_NEIGHBORHOOD_TICKS = 16     # 16 milliseconds
SHEEP_ROTATION_SCALAR = 0.1
SHEEP_WANDER_WEIGHT = 0.5
SHEEP_FLEE_WEIGHT = 0.7

# Flocking constants
SHEEP_NEIGHBOR_RADIUS = 75
SHEEP_BOUNDARY_RADIUS = 50
SHEEP_ALIGNMENT_WEIGHT = 0.3
SHEEP_SEPARATION_WEIGHT = 0.325
SHEEP_COHESION_WEIGHT = 0.3
SHEEP_DOG_INFLUENCE_WEIGHT = 0.2
SHEEP_BOUNDARY_INFLUENCE_WEIGHT = 0.2
MIN_ATTACK_DIST = 200

# Debug constants
DEBUG_VELOCITY_LENGTH = 25
DEBUG_VELOCITY_COLOR = (0, 0, 255)
DEBUG_NEIGHBOR_COLOR = (0, 255, 0)
DEBUG_SEEKFLEE_COLOR = (255, 0, 0)
ENABLE_DOG = True
ENABLE_ALIGNMENT = True
ENABLE_COHESION = True
ENABLE_SEPARATION = True
ENABLE_BOUNDARIES = True
DEBUGGING = True
DEBUG_LINE_WIDTH = 1
DEBUG_VELOCITY = DEBUGGING
DEBUG_BOUNDARIES = DEBUGGING
DEBUG_NEIGHBORS = DEBUGGING
DEBUG_DOG_INFLUENCE = DEBUGGING
DEBUG_BOUNDING_RECTS = DEBUGGING