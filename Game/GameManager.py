import os

from Constants import RenderLevels
from WorldMap import WorldMap

class GameManager:

    def __init__(self):

        self._worldMap = WorldMap(os.path.join("Assets", "WorldMap", "Datas", "Map", "map1.tmx"))

    def update(self):
        pass

    def getRenderFrame(self):
        return {
            RenderLevels.CONTEXT: None,
            RenderLevels.WORLD_MAP: self._worldMap,
        }