import pygame

from Constants import GameState
from ControlsManager import ControlsManager
from Game.GameManager import GameManager
from Graphics.GraphicsManager import GraphicsManager
from Menu.MainMenu import MainMenu


class GameEngine:
    def __init__(self):

        self._controls = ControlsManager()
        self._graphics = GraphicsManager()

        self.gameStates = {
            GameState.MAIN_MENU: MainMenu(),
            GameState.GAME: GameManager(),
        }

        #Give gameStates to controls and graphics
        self._controls.setGameState(self.gameStates)
        self._graphics.setGameState(self.gameStates)

        self._clock = pygame.time.Clock()
        self._minTimePerFrame = 1.0 / 60 * 1000
        self._elapsedTime = 0

        self._currentState = GameState.MAIN_MENU
        self._running = True

    def start(self):
        while self._running:

            self._elapsedTime += self._clock.tick()
            if self._elapsedTime >= self._minTimePerFrame:
                self.gameStates.get(self._currentState).update(self._elapsedTime)
                self._graphics.render(self._currentState)
                self._elapsedTime = 0

            self._currentState = self._controls.handleEvent(self._currentState)
            if self._currentState == GameState.QUIT:
                self._running = False


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Jail's Scape")
    #pygame.display.set_icon(pygame.image.load("/home/antoine/Images/Wallpaper/icons.png"))

    gameEngine = GameEngine()
    gameEngine.start()

    pygame.font.quit()
    pygame.quit()
