import os
import pygame

from Constants import RenderLevels, Direction
from GameContext import GameContext
from Player import Player
from WorldMap import WorldMap

class GameManager:

    def __init__(self):

        self._gameContext = GameContext()
        self._worldMap = WorldMap(os.path.join("Assets", "WorldMap", "Datas", "Map", "map1.tmx"))
        self._player = Player()

        self._eventList = []
        self._elapsedTime = 0

        self._eventMap = {
            pygame.K_z: "onMove",
            pygame.K_q: "onMove",
            pygame.K_s: "onMove",
            pygame.K_d: "onMove",
        }

    def pushEvent(self, event):
        self._eventList.append(event)

    def update(self, elapsedTime):

        self._elapsedTime = elapsedTime
        self._eventList.reverse()

        for event in self._eventList:
            if event.key in self._eventMap.keys():
                eval("self._" + self._eventMap.get(event.key))(event.key)
                self._eventList.remove(event)

        self._eventList = []

    def getRenderFrame(self):
        return {
            RenderLevels.CONTEXT: self._gameContext,
            RenderLevels.WORLD_MAP: self._worldMap,
            RenderLevels.PLAYER: self._player
        }

    def _onMove(self, event):

        camera_x, camera_y = self._gameContext.getCameraPosition()
        player_x, player_y = self._player.getPosition()

        if event == Direction.UP:
            player_y -= 1
            camera_y += 1
        if event == Direction.DOWN:
            player_y += 1
            camera_y -= 1
        if event == Direction.LEFT:
            player_x -= 1
            camera_x += 1
        if event == Direction.RIGHT:
            player_x += 1
            camera_x -= 1

        if not self._worldMap.getTileProperties(player_x, player_y, 1):
            self._gameContext.setCameraPosition(camera_x, camera_y)
            self._player.setPostion((player_x, player_y))