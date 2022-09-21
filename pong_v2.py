""" Exam at mentoring program "Za rączkę"
			Game "PONG"
"""

from main_game import *

pygame.init()

pygame.display.set_caption('TronG')
# clock = pygame.time.Clock()

screen.fill(BKG_COLOR)  # ?????


x = menu.show_menu()
main_game(x)

pygame.quit()
exit()



	