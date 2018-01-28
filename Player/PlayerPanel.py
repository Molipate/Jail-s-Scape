import pygame


class PlayerPanel:

    def __init__(self):

        panelWidth, panelHeight = 1216, 180
        self._panel = pygame.Surface((panelWidth, panelHeight))
        self._panelPosition = (0, 704 - panelHeight)

        self._textZoneWidth, self._textZoneHeight = (500, 140)
        self._textZone = pygame.Surface((self._textZoneWidth, self._textZoneHeight))
        self._textZonePosition = (696, 20)

        self._font = pygame.font.Font("Assets/font.ttf", 30)
        self._text = []
        self.setText("You've been Jail !\nExplore the place to find items\nand build a trasmitter !\nMaybe you will escape ...")

        self._selectedBackground = pygame.Surface((64, 64))
        self._selectedBackground.fill((255, 255, 0))
        self._inventory = {}

    def _getItemPosition(self, itemPosition):
        return 26 + (itemPosition % 8) * 64, 26 + (itemPosition / 8) * 64

    def getSurface(self):

        self._panel.fill((140, 140, 140))
        self._textZone.fill((0, 0, 0))

        for i in range(len(self._inventory)):
            itemPosition = self._getItemPosition(i)
            item = self._inventory.get(i)
            sprite = item.getSprite()
            if item.isSelected():
                self._panel.blit(self._selectedBackground, itemPosition)
            self._panel.blit(sprite, itemPosition)

        for i in range(len(self._text)):
            self._textZone.blit(self._text[i], (20, 25 * (i + 1)))
        self._panel.blit(self._textZone, self._textZonePosition)
        return self._panel

    def getPosition(self):
        return self._panelPosition

    def setText(self, text):
        self._text = []
        for line in text.split("\n"):
            self._text.append(self._font.render(line, 1, (120, 255, 0)))

    def setInventory(self, inventory):
        self._inventory = inventory

    def selectItem(self, mousePosition):
        mouse_x, mouse_y = mousePosition
        for i in range(len(self._inventory)):
            item_x, item_y = self._getItemPosition(i)
            if item_x <= mouse_x <= item_x + 64 and item_y + 524 <= mouse_y <= item_y + 64 + 524:
                self._inventory.get(i).onSelect()