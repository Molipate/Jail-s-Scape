import pygame

from Constants import GameState


class GraphicsManager:
    def __init__(self):

        self._tileSize = 64
        self._nbTileWidth = 19
        self._nbTileHeight = 11
        self._screen = pygame.display.set_mode((1216, 704))  # , pygame.FULLSCREEN)

    def render(self, frame):

        self._screen.fill((0, 0, 0))
        renderState = frame.get("renderState")

        if renderState == "game":
            self._renderGame(frame)

        pygame.display.flip()

    def _renderGame(self, frame):

        context = frame.get("context")
        worldMap = frame.get("worldMap")
        player = frame.get("player")
        playerPanel = frame.get("playerPanel")
        itemsManager = frame.get("items")

        def getPositionFromTile(tilePosition):
            tileSize = context.getTileSize()
            camera_x, camera_y = context.getCameraPosition()
            tile_x, tile_y = tilePosition
            return (tile_x - camera_x) * tileSize, (tile_y - camera_y) * tileSize

        self._screen.blit(worldMap.getWorldMap(), context.getCameraRenderPosition())

        for position, item in itemsManager.getItems().items():
            sprite = item.getSprite()
            self._screen.blit(sprite, getPositionFromTile(position))

        player_x, player_y = player.getPosition()
        self._screen.blit(player.getSprite(), getPositionFromTile((player_x, player_y - 1)))

        self._screen.blit(playerPanel.getSurface(), playerPanel.getPosition())
