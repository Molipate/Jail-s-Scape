import pygame

from Constants import GameState

class ControlsManager:
    def __init__(self, gameState):
        self._gameState = gameState
        self._currentState = None

        self._eventMap = {

        }

    def handleEvent(self, currentState):

        self._setCurrentState(currentState)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return GameState.QUIT

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    return GameState.QUIT

                if event.key in self._eventMap.keys():
                    eval("self._" + self._eventMap.get(event.key))(event)

        return True

    def _setCurrentState(self, currentState):
        self._currentState = currentState
