import pytmx

from pytmx.util_pygame import load_pygame

class WorldMap:

    def __init__(self, filename):

        self._tmxData = load_pygame(filename)
        #self._tileWidth = self._tmxData.