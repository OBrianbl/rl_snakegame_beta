import pygame
import random
from enum import Enum
from collections import namedtuple

# search pygame pygame.init()
#https://www.pygame.org/docs/ref/pygame.html#pygame.init
pygame.init()
font = pygame.font.Font('arial.tff', 25)

class SnakeGame:
    def __init__(self, w = 640, h = 480):
        """
        
        Args:
            w (int): width of game screen
            h (int): height of game screen
        Returns:
            None
        """