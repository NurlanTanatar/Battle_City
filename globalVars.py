import pygame
from enum import Enum
screen = pygame.display.set_mode((1200, 600))
class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4