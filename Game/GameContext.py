import pygame


class GameContext:

    def __init__(self, playerPosition=(6, 5), cameraSize=(1216, 704)):

        self._playerPosition = playerPosition
        self._cameraPosition = (0, 0)

    def getPlayerPosition(self):
        return self._playerPosition

    def getCameraPosition(self):
        return self._cameraPosition

    def setCameraPosition(self, x, y):
        self._cameraPosition = (x, y)