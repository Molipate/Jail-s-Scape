from Item import Item, ItemImage
from Event import MapItem

class DataManager:

    def __init__(self):
        self._itemList = []
        self._itemImage = []
        self._eventList = []
        self.loadData()

    def _builtin_ItemImage(self, **kw):
        self._itemImage.append( ItemImage(** kw))

    def _builtin_Item(self, **kw):
        self._itemList.append( Item(** kw) )

    def _builtin_MapItem(self, **kw):
        self._eventList.append( MapItem(** kw) )

    def loadData(self):
        symbols = {
            "Item": self._builtin_Item,
            "ItemImage": self._builtin_ItemImage,
            "MapItem": self._builtin_MapItem,
        }

        execfile("Assets/Item/Items.conf", symbols)
        execfile("Assets/Event/Events.conf", symbols)

