import pygame
import random

SCREEN_HIGHT = 600
SCREEN_WIDTH = 800
SCREEN_HALF_HIGHT = int(SCREEN_HIGHT/2)
SCREEN_HALF_WIDTH = int(SCREEN_WIDTH/2)
# --------------------------------------------------
# DISK_SPEED_X = 3 * random.choice((1, -1))
# DISK_SPEED_Y = 3 * random.choice((1, -1))
DISK_SPEED_X = 3
DISK_SPEED_Y = 3
# --------------------------------------------------
PADDLE_SPEED_RIGHT = 0
PADDLE_SPEED_LEFT = 0
# --------------------------------------------------
ANIMATION_LIST = []
ANIMATION_STEPS = 12
# --------------------------------------------------
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
MIDDLE_LINE_COLOR = (0, 0, 0)
BKG_COLOR = pygame.Color(50, 50, 50)