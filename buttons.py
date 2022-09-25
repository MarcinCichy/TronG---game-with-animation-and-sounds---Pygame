from constants import *


class Button:
	def __init__(self, image, x_pos, y_pos, text_input):
		self.button_img = image
		self.clicked_button_img = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.font = button_font
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, BUTTON_FONT_COLOR)
		self.button_pos = self.button_img.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input_pos = self.text.get_rect(center=(self.x_pos, self.y_pos))
		
	def show_button(self):
		screen.blit(self.button_img, self.button_pos)
		screen.blit(self.text, self.text_input_pos)
		
		
# bellow code is for options menu -> in future
class TextButton:
	def __init__(self, x_pos, y_pos, button_text):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.font = option_font
		self.button_text = button_text
		self.text = self.font.render(self.button_text, True, FONT_COLOR)
		self.button_text_pos = self.text.get_rect(topleft=(self.x_pos, self.y_pos))

	def show_text_button(self):
		screen.blit(self.text, self.button_text_pos)
