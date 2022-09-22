""" Exam at mentoring program "Za rączkę"
			Game "PONG"
"""

from main_game import *
from board import Board


title_screen = Board()
pygame.init()

pygame.display.set_caption('TronG')

title_screen.show_title_screen()
pygame.time.delay(5000)
num_of_players = menu.show_menu()
menu.close_menu_window()
main_game(num_of_players)

