import pygame

from Constants import GameState, Direction

class ControlsManager:
    def __init__(self):
        self._gameState = None
        self._currentState = None

        pygame.key.set_repeat(10, 100)

    def handleEvent(self, currentState):

        self._setCurrentState(currentState)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return GameState.QUIT

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    return GameState.QUIT

                self._gameState.get(self._currentState).pushEvent(event)

        return True

    def _setCurrentState(self, currentState):
        self._currentState = currentState

    def setGameState(self, gameStates):
        self._gameState = gameStates
