import pygame

from Constants import GameState, RenderLevels

class GraphicsManager:

    def __init__(self):

        self._gameState = None
        self._screen = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF)

    def setGameState(self, gameStates):
        self._gameState = gameStates

    def render(self, currentState):

        renderState = self._gameState.get(currentState)

        if currentState == GameState.GAME:
            pass
            #self._renderGame(renderState)

    def _renderGame(self, game):

        for level, datas in game:
            if level == RenderLevels.WORLD_MAP:

