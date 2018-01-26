import pygame


class ControlsManager:

    def __init__(self, game):
        self._game = game

    def handleEvent(self):

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    return False

        return True