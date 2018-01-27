import pygame

class GameState:
    MAIN_MENU = 0
    GAME = 1
    PAUSE = 2
    QUIT = 3

class RenderLevels:
    CONTEXT = 0
    WORLD_MAP = 1
    PLAYER = 2

class Direction:
    UP=pygame.K_z
    DOWN=pygame.K_s
    LEFT=pygame.K_q
    RIGHT=pygame.K_d
