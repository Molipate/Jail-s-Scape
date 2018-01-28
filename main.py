import pygame

from Constants import GameState, Event, Direction
from Game.GameManager import GameManager
from Graphics.GraphicsManager import GraphicsManager
from Menu.MainMenu import MainMenu


class GameEngine:
    def __init__(self):

        self._eventMap = {}
        self._graphics = GraphicsManager()
        self.gameStates = {
            GameState.MAIN_MENU: MainMenu(),
            GameState.GAME: GameManager(),
        }

        self._clock = pygame.time.Clock()
        self._minTimePerFrame = 1.0 / 60 * 1000
        self._elapsedTime = 0

        self._currentState = GameState.GAME
        self._running = True

    def start(self):
        while self._running:

            self._elapsedTime += self._clock.tick()
            if self._elapsedTime >= self._minTimePerFrame:
                state = self.gameStates.get(self._currentState)
                state.update(self._elapsedTime, self._eventMap)
                self._graphics.render(state.getRenderFrame())

                self._eventMap = []
                self._elapsedTime = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._currentState = GameState.QUIT

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self._currentState = GameState.QUIT

                    if event.key == pygame.K_z:
                        self._eventMap.append(Event.MOVE_UP)
                    if event.key == pygame.K_q:
                        self._eventMap.append(Event.MOVE_LEFT)
                    if event.key == pygame.K_s:
                        self._eventMap.append(Event.MOVE_DOWN)
                    if event.key == pygame.K_d:
                        self._eventMap.append(Event.MOVE_RIGHT)

                    if event.key == pygame.K_e:
                        self._eventMap.append(Event.PICK)

                if event.type == pygame.MOUSEBUTTONUP:
                    self._eventMap.append(Event.SELECT)

            if self._currentState == GameState.QUIT:
                self._running = False  # self._onQuit()


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()

    pygame.display.set_caption("Jail's Scape")
    # pygame.display.set_icon(pygame.image.load("/home/antoine/Images/Wallpaper/icons.png"))
    pygame.key.set_repeat(10, 100)

    gameEngine = GameEngine()
    gameEngine.start()

    pygame.font.quit()
    pygame.quit()
