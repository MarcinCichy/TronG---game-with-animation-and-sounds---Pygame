from constants import *


class Paddle:
	def __init__(self, name):
		self.name = name
		self.paddle_left_img = pygame.image.load_extended('pics/Left_Paddle_Alpha.png').convert_alpha()
		self.paddle_left_pos = self.paddle_left_img.get_rect()
		self.paddle_left_pos.center = (SCREEN_WIDTH-SCREEN_WIDTH+15, SCREEN_HALF_HIGHT)
		self.paddle_right_img = pygame.image.load_extended('pics/Right_Paddle_Alpha.png').convert_alpha()
		self.paddle_right_pos = self.paddle_right_img.get_rect()
		self.paddle_right_pos.center = (SCREEN_WIDTH-15, SCREEN_HALF_HIGHT)
		self.paddle_left_pos.center = (SCREEN_WIDTH - SCREEN_WIDTH + 15, SCREEN_HALF_HIGHT)
		self.paddle_right_pos.center = (SCREEN_WIDTH - 15, SCREEN_HALF_HIGHT)
		# self.right_paddle_lost_disk_img = pygame.image.load_extended('pics/Right_Paddle_Alpha_Lost_Disk_Anim.png').convert_alpha()
		# self.right_sprite_sheet = spritesheet.SpriteSheet(self.right_paddle_lost_disk_img)
		# self.left_paddle_lost_disk_img = pygame.image.load_extended('pics/Left_Paddle_Alpha_Lost_Disk_Anim.png').convert_alpha()
		# self.left_sprite_sheet = spritesheet.SpriteSheet(self.left_paddle_lost_disk_img)
	
	def show_paddles(self):
		if self.name == "left":
			screen.blit(self.paddle_left_img, self.paddle_left_pos)
		elif self.name == "right":
			screen.blit(self.paddle_right_img, self.paddle_right_pos)

	def paddle_move(self, speed):
		self.paddle_right_pos.y += speed
		if self.paddle_right_pos.top <= 0:
			self.paddle_right_pos.top = 0
		if self.paddle_right_pos.bottom >= SCREEN_HIGHT:
			self.paddle_right_pos.bottom = SCREEN_HIGHT
		
		self.paddle_left_pos.y += speed
		if self.paddle_left_pos.top <= 0:
			self.paddle_left_pos.top = 0
		if self.paddle_left_pos.bottom >= SCREEN_HIGHT:
			self.paddle_left_pos.bottom = SCREEN_HIGHT
	
	def computer_paddle_move(self, disk, comp_speed):
		#self.paddle_left_pos.y += comp_speed
		if self.paddle_left_pos.top < disk.disk_ingame_pos.y:
			self.paddle_left_pos.top += comp_speed
		if self.paddle_left_pos.bottom > disk.disk_ingame_pos.y:
			self.paddle_left_pos.bottom -= comp_speed
		if self.paddle_left_pos.top <= 0:
			self.paddle_left_pos.top = 0
		if self.paddle_left_pos.bottom >= SCREEN_HIGHT:
			self.paddle_left_pos.bottom = SCREEN_HIGHT
		
		
		
		# if computer.top < ball.y:
		# 	computer.top += COMPUTER_SPEED
		# if computer.bottom > ball.y:
		# 	computer.bottom -= COMPUTER_SPEED
		# if computer.top <= 0:
		# 	computer.top = 0
		# if computer.bottom >= HIGHT:
		# 	computer.bottom = HIGHT
			
	# def paddle_lost_point(self):
	# 	spritesheet.sprite_animation(4, 20, 120, 1, 'black', 100, 200)
