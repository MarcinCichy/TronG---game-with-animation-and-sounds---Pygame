import pygame.image

import functions
from constants import *
from board import Board
from buttons import Button


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
		menu_on = True
		while menu_on:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					menu_on = False
			# show menu
			screen.blit(self.menu_background_img, self.menu_background_pos)
			screen.blit(self.menu_img, self.menu_pos)
		
			# set buttons
			button_1pl_img = pygame.image.load('pics/emty_button_1.png').convert_alpha()
			button_1pl = Button(button_1pl_img, 420, 280, "1 PLAYER")
			button_2pl_img = pygame.image.load('pics/emty_button_1.png').convert_alpha()
			button_2pl = Button(button_2pl_img, 420, 340, "2 PLAYERS")
			button_opt_img = pygame.image.load('pics/emty_button_1.png').convert_alpha()
			button_opt = Button(button_opt_img, 420, 400, "OPTIONS")
			button_quit_img = pygame.image.load('pics/emty_button_1.png').convert_alpha()
			button_quit = Button(button_quit_img, 420, 460, "QUIT")
			button_1pl.show_button()
			button_2pl.show_button()
			button_opt.show_button()
			button_quit.show_button()
			
			functions.select_from_menu()
			
			pygame.display.update()