import pygame.image
import pygame_gui
from constants import *
from board import Board
from buttons import Button


button_set_img = pygame.image.load('pics/emty_button_1.png').convert_alpha()
button_set = Button(button_set_img, 420, 460, "SET")

manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HIGHT))
text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((320, 280), (15,25)), manager= manager, object_id="#main_text_entry")
pygame.font.init()


class Options:
	def __init__(self):
		self.options_background_img = pygame.image.load('pics/menu_background.png')
		self.options_background_pos = self.options_background_img.get_rect()
		self.options_img = pygame.image.load('pics/menu.png').convert_alpha()
		self.options_size = self.options_img.get_rect()
		self.options_size.midtop = (400, 240)
		self.options_pos = self.options_size
		self.static_background = Board()
	
	def show_options(self):
		options_on = True
		while options_on:
			time_delta = clock.tick(60)/1000
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					options_on = False
					
				manager.process_events(event)
				
			manager.update(time_delta)
			
			# show options menu
			screen.blit(self.options_background_img, self.options_background_pos)
			screen.blit(self.options_img, self.options_pos)
			
			set_disk_speed_txt = option_font.render("SET DISK SPEED", False, FONT_COLOR)
			screen.blit(set_disk_speed_txt, (220, 280))
			set_computer_speed_txt = option_font.render("SET COMPUTER SPEED", False, FONT_COLOR)
			screen.blit(set_computer_speed_txt, (220, 340))
			set_max_points_txt = option_font.render("SET MAX POINT LIMIT", False, FONT_COLOR)
			screen.blit(set_max_points_txt, (220, 400))
			
			button_set.show_button()

			pygame.display.update()

