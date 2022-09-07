import spritesheet
from Board import Board
from Constants import *


class Disk():
	def __init__(self, speed_x=DISK_SPEED_X, speed_y=DISK_SPEED_Y):
		self.speed_x = speed_x
		self.speed_y = speed_y
		self.disk_appears_img = pygame.image.load_extended('pics/Disk_appeared.png').convert_alpha()
		self.sprite_sheet = spritesheet.SpriteSheet(self.disk_appears_img)
		self.disk_ingame_img = pygame.image.load_extended('pics/Tron_Disk.png').convert_alpha()
		self.disk_ingame_pos = self.disk_ingame_img.get_rect()  # image size is 32x32
		self.bounced_disk_img = pygame.image.load_extended('pics/Bounced_Tron_Disk.png').convert_alpha()
		self.bounced_disk = self.bounced_disk_img.get_rect()
		self.static_background = Board()
		self.disk_ingame_pos.center = (SCREEN_HALF_WIDTH, SCREEN_HALF_HIGHT)
		# self.disk_vector = pygame.Vector2()
		# self.bounce_counter = 0
		#
		# self.vector_top = pygame.Vector2()
		# self.vector_bottom = pygame.Vector2()
		# self.vector_left = pygame.Vector2()
		# self.vector_right = pygame.Vector2()
		#
		# self.vector_top.xy = 400, 0
		# self.vector_bottom.xy = 400, 600
		# self.vector_left.xy = 0, 300
		# self.vector_right.xy = 800, 300
		
	def disk_start(self):
		pygame.time.delay(50)
		self.disk_ingame_pos.center = (SCREEN_HALF_WIDTH, SCREEN_HALF_HIGHT)
		print(self.disk_ingame_pos)
		self.disk_appears_anim()
		screen.blit(self.disk_ingame_img, self.disk_ingame_pos)
		#pygame.display.update()
		
	def disk_appears_anim(self):
		# if point < 1:
		animation_list = []
		animation_steps = 12
		
		for x in range(animation_steps):
			animation_list.append(self.sprite_sheet.get_image(x, 32, 32, 1, 'black'))
		
		for frame in range(len(animation_list)):
			if frame != 5:
				# to check if all images are in animation_list, change x position of screen.blit to "frame*50 for example"
				screen.blit(animation_list[frame], (SCREEN_HALF_WIDTH-16, SCREEN_HALF_HIGHT-16))
			else:
				self.static_background.board_static()
			pygame.display.update()
			pygame.time.delay(80)
		self.static_background.board_static()

		#pygame.time.delay(200)
		
		# print(self.frame)
		# while self.frame == (len(animation_list)):
		#
		# 	if self.frame != 5:
		# 		# to check if all images are in animation_list, change x position of screen.blit to "frame*50 for example"
		# 		screen.blit(animation_list[self.frame], (SCREEN_HALF_WIDTH-16, SCREEN_HALF_HIGHT-16))
		# 	else:
		# 		self.static_background.board_static()
		#
		# 	pygame.display.update()
		# 	pygame.time.delay(80)
		# 	self.static_background.board_static()
		# self.frame += 1
		
	def disk_move(self):
		self.disk_ingame_pos.x += self.speed_x
		self.disk_ingame_pos.y += self.speed_y
		self.static_background.board_static()
		screen.blit(self.disk_ingame_img, self.disk_ingame_pos)
		pygame.time.delay(3)

	def disk_after_bounc(self):
		screen.blit(self.bounced_disk_img, self.disk_ingame_pos)
		pygame.display.update()
		pygame.time.delay(20)
	
	# def disk_acceleration(self):
	# 	self.disk_vector.xy = self.disk_ingame.x, self.disk_ingame.y
	# 	# print(f'Vector = {self.vector}')
	# 	# print(f'Vector lenght after bounce  = {self.vector.length()}')
	# 	# print(f'Vector distance = {self.vector.distance_to(self.vector_top)}')
	# 	# if self.vector.length() < self.vector.length() / 2:
	# 	# 	self.speed_x -= 30
	# 	# return self.speed_x
	# 	return self.disk_vector.distance_to(self.vector_top)
	



	

