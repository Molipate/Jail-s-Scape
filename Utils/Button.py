import pygame

class Button:

    def __init__(self):

        self._background = pygame.Surface()
        self._foreground = pygame.Surface()

    def isHover(self):
        return False