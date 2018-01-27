import pygame

from Constants import Direction

class Player:
    def __init__(self, posX=15, posY=92):

        self._position = (15, 92)
        self._speed = 2
        self._sprite = pygame.Surface((64, 64))
        self._sprite.fill((255, 0, 255))

    def getSprite(self):
        return self._sprite

    def getPosition(self):
        return self._position

    def setPostion(self, position):
        self._position = position

    def getSpeed(self):
        return self._speed