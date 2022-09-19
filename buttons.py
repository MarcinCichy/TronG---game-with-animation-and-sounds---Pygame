from constants import *


class Button():
	def __init__(self, image, x_pos, y_pos, text_input):
		self.button_img = image
		self.clicked_button_img = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.font = button_font
		self.hovering_color = "blue"
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, BUTTON_FONT_COLOR)
		self.button_pos = self.button_img.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input_pos = self.text .get_rect(center=(self.x_pos, self.y_pos))
		
	def show_button(self):
		screen.blit(self.button_img, self.button_pos)
		screen.blit(self.text, self.text_input_pos)
		
	def show_clicked_button(self):
		screen.blit(self.clicked_button_img, self.button_pos)
		screen.blit(self.text, self.text_input_pos)
