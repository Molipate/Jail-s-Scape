import pygame

from Constants import GameState, RenderLevels

class GraphicsManager:
    def __init__(self):

        self._gameState = None
        self._screen = pygame.display.set_mode((1216, 704))#, pygame.FULLSCREEN)

    def setGameState(self, gameStates):
        self._gameState = gameStates

    def render(self, currentState):

        self._screen.fill((255, 255, 65))
        if currentState == GameState.GAME:
            self._renderGame(self._gameState.get(currentState).getRenderFrame())

        pygame.display.flip()

    def _renderGame(self, game):

        context = game.get(RenderLevels.CONTEXT)

        def _renderWorldMap(datas):
            camera_x, camera_y = context.getCameraPosition()
            self._screen.blit(datas.getWorldMap(), (camera_x * 64, camera_y * 64))

        def _renderPlayer(datas):
            sprite = datas.getSprite()
            player_x, player_y = context.getPlayerPosition()
            self._screen.blit(sprite, (player_x * 64, player_y * 64))

        for level, datas in game.items():
            if level == RenderLevels.WORLD_MAP:
                _renderWorldMap(datas)

            if level == RenderLevels.PLAYER:
                _renderPlayer(datas)