from Constants import *
from Board import Board


class Menu:
	def __init__(self):
		self.menu_background_img = pygame.image.load('pics/menu_background.png')
		self.menu_background_pos = self.menu_background_img.get_rect()
		self.menu_img = pygame.image.load('pics/menu.png').convert_alpha()
		self.menu_size = self.menu_img.get_rect()
		self.menu_size.midtop = (400, 240)
		self.menu_pos = self.menu_size
		self.static_background = Board()
	
	def show_menu(self):
		screen.blit(self.menu_background_img, self.menu_background_pos)
		screen.blit(self.menu_img, self.menu_pos)
		pygame.display.update()
		pygame.time.delay(3000)
		

	