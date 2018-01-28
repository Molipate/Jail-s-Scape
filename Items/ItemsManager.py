import pygame


class Item:
    def __init__(self, ident, sprite, name, description):
        self._ident = ident
        self._sprite = sprite
        self._name = name
        self._description = description
        self._selected = False

    def getIdent(self):
        return self._ident

    def getSprite(self):
        return self._sprite

    def getName(self):
        return self._name

    def isSelected(self):
        return self._selected

    def onSelect(self):
        print self._selected
        self._selected = not self._selected

class ItemsManager:
    def __init__(self):
        self._items = {}
        self._itemSprite = {}
        self.loadData()

    def _builtin_ItemSprite(self, spriteID, filename):
        self._itemSprite.update({spriteID: pygame.image.load(filename)})

    def _builtin_Item(self, ident, spriteID, name, description, position):
        self._items.update({position: Item(ident, self.getSprite(spriteID), name, description)})

    def loadData(self):
        symbols = {
            "Item": self._builtin_Item,
            "ItemSprite": self._builtin_ItemSprite,
        }

        execfile("Assets/Item/Items.conf", symbols)

    def getItems(self):
        return self._items

    def getSprite(self, spriteID):
        return self._itemSprite.get(spriteID)

    def popItem(self, item):
        return self._items.pop(item)

