class Event:
    def __init__(self):
        pass

class MapItem(Event):

    def __init__(self, itemID, X, Y, hidden, quantity):
        Event.__init__(self)
        self.itemID = itemID
        self.posX = X
        self.posY = Y
        self.hidden = hidden
        self.quantity = quantity
