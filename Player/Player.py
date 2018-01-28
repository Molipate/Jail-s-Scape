import pygame

from Constants import Direction
from Items.ItemsManager import Item
from PlayerPanel import PlayerPanel

class Player:
    def __init__(self, player_x=15, player_y=92):

        self._position = (player_x, player_y)
        self._inventory = {}
        self._panel = PlayerPanel()
        self._sprite = pygame.image.load("Assets/Perso/Main 2-2@2.png")

    def getSprite(self):
        return self._sprite

    def getPosition(self):
        return self._position

    def setPostion(self, position):
        self._position = position

    def pickItem(self, item):
        self._inventory.update({len(self._inventory): item})
        self._panel.setInventory(self._inventory)
        self._panel.setText("You found : %s\nClick on item to combine them,\nMaybe you'll get a new one" % item.getName())

    def getPanel(self):
        return self._panel

    def tryCombine(self, itemsManager):

        selectedItem = [item for _, item in self._inventory.items() if item.isSelected()]
        selectedItemIdent = [item.getIdent() for item in selectedItem]
        selectedItemIdent.sort()

        if selectedItemIdent == [1, 2, 3, 4]:

            self.pickItem(Item(ident=5, sprite=itemsManager.getSprite(5), name="Transmitter", description="You're free now !"))
            for ident, item in self._inventory.items():
                if item in selectedItem:
                    self._inventory.pop(ident)

        itemList = [item for _, item in self._inventory.items()]
        print itemList
        self._inventory = {}
        for i in range(len(itemList)):
            self._inventory.update({i: itemList[i]})

        print self._inventory
        self._panel.setInventory(self._inventory)

