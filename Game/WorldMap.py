import pygame

from pytmx import TiledTileLayer
from pytmx.util_pygame import load_pygame


class WorldMap:
    def __init__(self, filename):

        self._tmxData = load_pygame(filename)
        self._tileWidth = self._tmxData.tilewidth
        self._tileHeight = self._tmxData.tileheight

        mapWidth = self._tmxData.width * self._tmxData.tilewidth
        mapHeight = self._tmxData.height * self._tmxData.tileheight
        self._renderWorldMap = pygame.Surface((mapWidth, mapHeight))

        for layer in self._tmxData.visible_layers:
            if isinstance(layer, TiledTileLayer):
                for x, y, image in layer.tiles():
                    self._renderWorldMap.blit(image, (x * self._tileWidth, y * self._tileHeight))

    def getWorldMap(self):
        return self._renderWorldMap

    def getTileProperties(self, x, y, layer):
        return self._tmxData.get_tile_properties(x, y, layer)
