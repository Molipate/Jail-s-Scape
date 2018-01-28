import pygame


class GameState:
    MAIN_MENU = 0
    GAME = 1
    PAUSE = 2
    QUIT = 3


class Event:
    MOVE_UP = 0
    MOVE_DOWN = 1
    MOVE_LEFT = 2
    MOVE_RIGHT = 3
    PICK = 4
    SELECT = 5


class Direction:
    UP = pygame.K_z
    DOWN = pygame.K_s
    LEFT = pygame.K_q
    RIGHT = pygame.K_d
