import os

import pygame

from Constants import Direction, Event
from Context import Context
from Items.ItemsManager import ItemsManager
from Player.Player import Player
from WorldMap import WorldMap


class GameManager:
    def __init__(self):

        self._context = Context()
        self._worldMap = WorldMap(os.path.join("Assets", "WorldMap", "Datas", "Map", "map1.tmx"))
        self._itemsManager = ItemsManager()
        self._player = Player()
        self._elapsedTime = 0

    def update(self, elapsedTime, eventList):

        self._elapsedTime = elapsedTime
        for event in eventList:
            if event == Event.MOVE_UP:
                self._onMove(Direction.UP)
            if event == Event.MOVE_DOWN:
                self._onMove(Direction.DOWN)
            if event == Event.MOVE_LEFT:
                self._onMove(Direction.LEFT)
            if event == Event.MOVE_RIGHT:
                self._onMove(Direction.RIGHT)

            if event == Event.PICK:
                self._onPick()

            if event == Event.SELECT:
                self._onSelectItem()

        self._player.tryCombine()

    def getRenderFrame(self):
        return {
            "renderState": "game",
            "context": self._context,
            "worldMap": self._worldMap,
            "player": self._player,
            "playerPanel": self._player.getPanel(),
            "items": self._itemsManager,
        }

    def _onMove(self, direction):

        player_x, player_y = self._player.getPosition()
        if direction == Direction.UP:
            player_y -= 1
        if direction == Direction.DOWN:
            player_y += 1
        if direction == Direction.LEFT:
            player_x -= 1
        if direction == Direction.RIGHT:
            player_x += 1

        if not self._worldMap.getTileProperties(player_x, player_y, 1):
            self._player.setPostion((player_x, player_y))
            self._context.setCameraPosition((player_x - 9, player_y - 5))

    def _onPick(self):
        player_x, player_y = self._player.getPosition()
        items = self._itemsManager.getItems()
        item = None

        if items.has_key((player_x - 1, player_y)):
            item = self._itemsManager.popItem((player_x - 1, player_y))
        elif items.has_key((player_x + 1, player_y)):
            item = self._itemsManager.popItem((player_x + 1, player_y))
        elif items.has_key((player_x, player_y - 1)):
            item = self._itemsManager.popItem((player_x, player_y - 1))
        elif items.has_key((player_x, player_y + 1)):
            item = self._itemsManager.popItem((player_x, player_y + 1))

        if item:
            self._player.pickItem(item)

    def _onSelectItem(self):
        self._player.getPanel().selectItem(pygame.mouse.get_pos())