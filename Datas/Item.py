class Item:
    def __init__(self, itemID, spriteID, itemName, itemDesc, itemEffect, stackable):
        self._id=itemID
        self._name=itemName
        self._desc=itemDesc
        self._effect=itemEffect
        self._stackable=stackable

class ItemImage:

    def __init__(self, itemID, imagePath):
        self.itemID = itemID
        self.path = imagePath
