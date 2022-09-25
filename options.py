import pygame.image
import functions
from board import Board
from buttons import *
import constants

# # below are default values of some game parameters
# disk_speed_list = [6]
# computer_speed_list = [8]
# max_points_list = [5]
# chosen_list = [disk_speed_list, computer_speed_list, max_points_list]

# Buttons in Options menu
button_set_img = pygame.image.load('pics/empty_button_1.png').convert_alpha()
button_set = Button(button_set_img, 420, 455, "SET")

set_disk_speed_txt = TextButton(220, 280, "SET DISK SPEED")
set_computer_speed_txt = TextButton(220, 340, "SET COMPUTER SPEED")
set_max_points_txt = TextButton(220, 400, "SET MAX POINT LIMIT")

# options values for disk speed
disk_speed_txt_value4 = TextButton(480, 280, "4")
disk_speed_txt_value5 = TextButton(520, 280, "5")
disk_speed_txt_value6 = TextButton(560, 280, "6")

# options values for computer speed
computer_speed_txt_value6 = TextButton(480, 340, "7")
computer_speed_txt_value7 = TextButton(520, 340, "8")
computer_speed_txt_value8 = TextButton(560, 340, "9")

# options values for max points
max_points_txt_value3 = TextButton(480, 400, "3")
max_points_txt_value5 = TextButton(520, 400, "5")
max_points_txt_value10 = TextButton(560, 400, "10")

list_of_values = [disk_speed_txt_value4, disk_speed_txt_value5, disk_speed_txt_value6,
				  computer_speed_txt_value6, computer_speed_txt_value7, computer_speed_txt_value8,
				  max_points_txt_value3, max_points_txt_value5, max_points_txt_value10]


class Options:
	def __init__(self):
		self.options_background_img = pygame.image.load('pics/menu_background.png')
		self.options_background_pos = self.options_background_img.get_rect()
		self.options_img = pygame.image.load('pics/menu.png').convert_alpha()
		self.options_size = self.options_img.get_rect()
		self.options_size.midtop = (400, 240)
		self.options_pos = self.options_size
		self.static_background = Board()
		self.cursor_pos_x = MOVE_CURSOR_X
		self.cursor_pos_y = MOVE_CURSOR_Y
		
	def show_options(self):
		options_on = True
		while options_on:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					options_on = False
			
			screen.blit(self.options_background_img, self.options_background_pos)
			screen.blit(self.options_img, self.options_pos)
			
			# show buttons
			self.show_chosen_value(chosen_list)
			set_disk_speed_txt.show_text_button()
			set_computer_speed_txt.show_text_button()
			set_max_points_txt.show_text_button()
			
			disk_speed_txt_value4.show_text_button()
			disk_speed_txt_value5.show_text_button()
			disk_speed_txt_value6.show_text_button()
			
			computer_speed_txt_value6.show_text_button()
			computer_speed_txt_value7.show_text_button()
			computer_speed_txt_value8.show_text_button()
			
			max_points_txt_value3.show_text_button()
			max_points_txt_value5.show_text_button()
			max_points_txt_value10.show_text_button()
			
			button_set.show_button()
			
			set_cursor_position = self.move_cursor()
			q = self.select_option(set_cursor_position)
			
			if q == "Quit":
				options_on = False
			pygame.display.update()
	
	def move_cursor(self):
		key = None
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					functions.play_sound('audios/mixkit-explainer-video-pops-whoosh-light-pop-3005.wav')
					self.cursor_pos_y += 60
				if event.key == pygame.K_UP:
					functions.play_sound('audios/mixkit-explainer-video-pops-whoosh-light-pop-3005.wav')
					self.cursor_pos_y -= 60
				if event.key == pygame.K_LEFT:
					functions.play_sound('audios/mixkit-explainer-video-pops-whoosh-light-pop-3005.wav')
					self.cursor_pos_x -= 40
				if event.key == pygame.K_RIGHT:
					functions.play_sound('audios/mixkit-explainer-video-pops-whoosh-light-pop-3005.wav')
					self.cursor_pos_x += 40
				if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
					key = "K_RETURN"
					functions.play_sound('audios/mixkit-falling-on-metal-roof-752.wav')
		
		cursor_color = (28, 21, 78)
		cursor = pygame.Rect(self.cursor_pos_x, self.cursor_pos_y, 25, 30)
		
		# if cursor is on the first column and cursor is not on the button and move it to the left,
		# then move cursor to the last column
		if cursor.x < 475 and cursor.y < 455:
			cursor.x = 555
			self.cursor_pos_x = 555
		# if cursor is on the last column and cursor is not on the button and move it to the right,
		# then move cursor to the first column
		elif cursor.x > 555 and cursor.y < 455:
			cursor.x = 475
			self.cursor_pos_x = 475
		
		# if cursor is on the first row	and move it up, then move the cursor on the button
		# set position of the cursor in x and y on the button
		if cursor.y < 275:
			cursor.y = 455
			cursor.x = 400
			self.cursor_pos_x = 400
			self.cursor_pos_y = 455
		
		# if cursor is on the button and move it down, then move the cursor on the first row
		elif cursor.y > 455:
			cursor.y = 275
			self.cursor_pos_x = 475
			self.cursor_pos_y = 275
		
		# if cursor is on the last row and move it down, then set the cursor on button
		elif cursor.y > 395:
			cursor.y = 455
			cursor.x = 400
			self.cursor_pos_x = 400
			self.cursor_pos_y = 455
		
		# don't let move the cursor on the left and the right if it is on the button
		if cursor.x < 475 and cursor.y == 455:
			self.cursor_pos_x = 400
			self.cursor_pos_y = 455
			cursor = pygame.Rect(self.cursor_pos_x - 20, self.cursor_pos_y - 20, 80, 40)  # new size of cursor on button "SET"
		# print(cursor)
		pygame.draw.rect(screen, cursor_color, cursor, 2)
		return cursor, key
	
	def select_option(self, x):
		# x[0] -> position of cursor on menu
		# x[1] -> information about press ENTER/SPACE/ key
		collide_setbtn = pygame.Rect.colliderect(x[0], button_set.button_pos)
		if collide_setbtn and x[1] == "K_RETURN":
			functions.check()
			return "Quit"
		
		for z in range(len(list_of_values)):
			chosen_pos = list_of_values[z].button_text_pos
			chosen_value = list_of_values[z].button_text
			collide = pygame.Rect.colliderect(x[0], chosen_pos)
			if collide and x[1] == "K_RETURN":
				if list_of_values.index(list_of_values[z]) <= 2:
					disk_speed_list[0] = chosen_value
					constants.DISK_SPEED_X = (chosen_list[0][0])
					constants.DISK_SPEED_Y = (chosen_list[0][0])
				elif list_of_values.index(list_of_values[z]) >= 6:
					max_points_list[0] = chosen_value
					constants.END_GAME_POINTS = (chosen_list[2][0])
				else:
					computer_speed_list[0] = chosen_value
					constants.COMPUTER_PADDLE_SPEED = (chosen_list[1][0])

	def show_chosen_value(self, lv):
		selected_cursor_color = (190, 38, 51)
		for z in range(len(list_of_values)):
			if lv[0][0] == list_of_values[z].button_text and list_of_values.index(list_of_values[z]) <= 2:
				selected_cursor_1 = pygame.Rect(list_of_values[z].button_text_pos.x-5, list_of_values[z].button_text_pos.y-5, 25, 30)
				pygame.draw.rect(screen, selected_cursor_color, selected_cursor_1, 2)
			elif lv[2][0] == list_of_values[z].button_text and list_of_values.index(list_of_values[z]) >= 6:
				selected_cursor_2 = pygame.Rect(list_of_values[z].button_text_pos.x-5, list_of_values[z].button_text_pos.y-5, 25, 30)
				pygame.draw.rect(screen, selected_cursor_color, selected_cursor_2, 2)
			elif lv[1][0] == list_of_values[z].button_text and list_of_values.index(list_of_values[z]) >= 3 and list_of_values.index(list_of_values[z]) < 6:
				selected_cursor_3 = pygame.Rect(list_of_values[z].button_text_pos.x-6, list_of_values[z].button_text_pos.y-5, 25, 30)
				pygame.draw.rect(screen, selected_cursor_color, selected_cursor_3, 2)