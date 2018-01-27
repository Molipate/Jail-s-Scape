import pytmx

from pytmx.util_pygame import load_pygame

class WorldMap:

    def __init__(self, filename):

        self._tmxData = load_pygame(filename)
        self._tileWidth = self._tmxData.tilewidth
        self._tileHeight = self._tmxData.tileheight

    def getWorldMap(self):
        return self._tmxData

    def getTileSize(self):
        return self._tmxData.tilewidth, self._tmxData.tileheight