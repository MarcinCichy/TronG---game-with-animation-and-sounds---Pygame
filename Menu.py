from Constants import *
from Board import Board


class Menu:
	def __init__(self):
		self.menu_img = pygame.image.load('pics/menu.png').convert_alpha()
		self.menu_size = self.menu_img.get_rect()
		self.menu_size.midtop = (400, 180)
		self.menu_pos = self.menu_size
		self.static_background = Board()
	
	def show_menu(self):
		self.static_background.board_static()
		screen.blit(self.menu_img, self.menu_pos)
		
