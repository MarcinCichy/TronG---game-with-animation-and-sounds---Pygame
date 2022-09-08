from Constants import *


class Board:
	def __init__(self):
		self.bg_img_left = pygame.image.load('pics/bkg_left_wo_fill.png').convert()
		self.bg_img_right = pygame.image.load('pics/bkg_right_wo_fill.png').convert()
	
	def board_appearance(self):
		pygame.draw.line(screen, MIDDLE_LINE_COLOR, (SCREEN_HALF_WIDTH, 0), (SCREEN_HALF_WIDTH, SCREEN_HIGHT), width=3)  # middle line
		half_background_size = pygame.Rect(0, 0, SCREEN_HALF_WIDTH, SCREEN_HIGHT)  # image size is 400x600
		self.board_move(half_background_size)

	def board_move(self, background_size):
		positions = []
		for p in range(-SCREEN_HALF_HIGHT, SCREEN_HALF_HIGHT):
			if p <= 0:
				left_image_position = background_size.move(p, 0)
				positions.append(left_image_position)
			p *= -1  # to revers position value
			if p >= 0:
				right_image_position = background_size.move(p, 0)
				positions.append(right_image_position)
		
		for background_position in positions:
			if background_position[0] <= 0:
				screen.blit(self.bg_img_left, background_position)  # left half of background move by left top corner
			else:
				screen.blit(self.bg_img_right, background_position.topright)  # right half of background move by right top corner
			pygame.display.update()  # update display every frame
			pygame.time.delay(2)  # but not so fast
	
	def board_static(self):
		pygame.draw.line(screen, MIDDLE_LINE_COLOR, (SCREEN_HALF_WIDTH, 0), (SCREEN_HALF_WIDTH, SCREEN_HIGHT), width=3)  # middle line
		screen.blit(self.bg_img_left, (0, 0))
		screen.blit(self.bg_img_right, (401, 0))
	
	
class FillBoard:
	def __init__(self):
		self.bg_img_left_fill = pygame.image.load('pics/bkg_left_fill_alpha.png').convert_alpha()
		self.bg_img_right_fill = pygame.image.load('pics/bkg_right_fill_alpha.png').convert_alpha()
		
	def fill_board(self, side):
		if side == "board_left":
			screen.blit(self.bg_img_left_fill, (0, 0))  # left half of background move by left top corner
		else:
			screen.blit(self.bg_img_right_fill, (400, 0))  # right half of background move by right top corner
		pygame.display.update()  # update display every frame
