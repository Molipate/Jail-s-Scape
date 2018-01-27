
class DataManager:

    def __init__(self):
        self._itemList=[]
        self.loadData()

    def _builtin_Item(self, **kw):
        self._itemList.append(Item(** kw))

    def loadData(self):
        symbols = {
            "Item": self._builtin_Item,
        }

        execfile("strpath", symbols)