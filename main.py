import pygame

from ControlsManager import ControlsManager
from Constants import GameState
from Game.GameManager import GameManager
from Graphics.GraphicsManager import GraphicsManager


class GameEngine:

    def __init__(self):

        self._game = GameManager()
        self._controls = ControlsManager(self._game)
        self._graphics = GraphicsManager(self._game)

        self._clock = pygame.time.Clock()
        self._minTimePerFrame = 1.0 / 60 * 1000
        self._elapsedTime = 0

        self.context = GameState.MAIN_MENU

        self._running = True

    def start(self):
        while self._running:

            self._elapsedTime += self._clock.tick()
            if self._elapsedTime >= self._minTimePerFrame:
                self._game.update()
                self._elapsedTime = 0

            self._graphics.render()
            self._running = self._controls.handleEvent()

if __name__ == '__main__':

    pygame.init()
    pygame.font.init()

    gameEngine = GameEngine()
    gameEngine.start()

    pygame.font.quit()
    pygame.quit()