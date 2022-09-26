import copy

import pygame

# # below are default values of some game parameters
disk_speed_list = [6]
computer_speed_list = [8]
max_points_list = [5]
chosen_list = [disk_speed_list, computer_speed_list, max_points_list]

pygame.font.init()
clock = pygame.time.Clock()

SCREEN_HIGHT = 600
SCREEN_WIDTH = 800
SCREEN_HALF_HIGHT = int(SCREEN_HIGHT/2)
SCREEN_HALF_WIDTH = int(SCREEN_WIDTH/2)
# --------------------------------------------------
DISK_SPEED_X = 6
DISK_SPEED_Y = 6
ACCELERATION = 2
RIGHT_PADDLE_STICK_DISK = 0
LEFT_PADDLE_STICK_DISK = 0
# --------------------------------------------------
PADDLE_SPEED_RIGHT = 0
PADDLE_SPEED_LEFT = 0
COMPUTER_PADDLE_SPEED = 8
LEFT_POINTS = 0
RIGHT_POINTS = 0
END_GAME_POINTS = 5
# --------------------------------------------------
ANIMATION_LIST = []
ANIMATION_STEPS = 12
# --------------------------------------------------
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
MIDDLE_LINE_COLOR = (0, 0, 0)
BKG_COLOR = pygame.Color(50, 50, 50)
FONT_COLOR = pygame.Color(153, 217, 234)
BUTTON_FONT_COLOR = pygame.Color(112, 178, 225)
# --------------------------------------------------
game_font = pygame.font.Font("fonts/tr2n/Tr2n.ttf", 80)
button_font = pygame.font.Font("fonts/tr2n/Tr2n.ttf", 25)
option_font = pygame.font.Font("fonts/tr2n/Tr2n.ttf", 20)

MOVE_POINTER = 270
MOVE_CURSOR_X = 475
MOVE_CURSOR_Y = 275
