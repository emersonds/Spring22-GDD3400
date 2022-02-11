#   HW: Moving Agents
#   Author: Dylan Emerson
#   File: PygameTime.py

import pygame

import Constants as Const

clock = pygame.time.Clock()

deltaTime = clock.tick(Const.FRAME_RATE) / 1000