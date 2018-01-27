import pygame

from Constants import GameState, RenderLevels
from pytmx import TiledTileLayer

class GraphicsManager:
    def __init__(self):

        self._gameState = None
        self._screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)

    def setGameState(self, gameStates):
        self._gameState = gameStates

    def render(self, currentState):

        self._screen.fill((255, 255, 65))
        if currentState == GameState.GAME:
            self._renderGame(self._gameState.get(currentState).getRenderFrame())

        pygame.display.flip()

    def _renderGame(self, game):

        def _renderWorldMap(datas):

            worldMap = datas.getWorldMap()
            tileWidth, tileHeight = datas.getTileSize()

            for layer in worldMap.visible_layers:
                if isinstance(layer, TiledTileLayer):
                    for x, y, image in layer.tiles():
                        self._screen.blit(image, ((x - 15) * tileWidth, (y - 10) * tileHeight))

        for level, datas in game.items():
            if level == RenderLevels.WORLD_MAP:
                _renderWorldMap(datas)