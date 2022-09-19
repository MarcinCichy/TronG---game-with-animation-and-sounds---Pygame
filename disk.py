import spritesheet
from board import Board
from constants import *


class Disk:
	def __init__(self):
		self.speed_x = DISK_SPEED_X
		self.speed_y = DISK_SPEED_Y
		self.disk_appears_img = pygame.image.load_extended('pics/Disk_appeared.png').convert_alpha()
		self.sprite_sheet = spritesheet.SpriteSheet(self.disk_appears_img)
		self.disk_ingame_img = pygame.image.load_extended('pics/Tron_Disk.png').convert_alpha()
		self.disk_ingame_pos = self.disk_ingame_img.get_rect()  # image size is 32x32
		self.bounced_disk_img = pygame.image.load_extended('pics/Bounced_Tron_Disk.png').convert_alpha()
		self.bounced_disk = self.bounced_disk_img.get_rect()
		self.static_background = Board()
		self.disk_ingame_pos.center = (SCREEN_HALF_WIDTH, SCREEN_HALF_HIGHT)
		
	def disk_start(self):
		self.disk_ingame_pos.center = (SCREEN_HALF_WIDTH, SCREEN_HALF_HIGHT)
		self.disk_appears_anim()
		screen.blit(self.disk_ingame_img, self.disk_ingame_pos)
		pygame.time.delay(250)
		
	def disk_appears_anim(self):
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
		
	def disk_move(self):
		self.disk_ingame_pos.x += self.speed_x
		self.disk_ingame_pos.y += self.speed_y
		self.static_background.board_static()
		screen.blit(self.disk_ingame_img, self.disk_ingame_pos)
		pygame.time.delay(3)

	def disk_after_bounce(self):
		screen.blit(self.bounced_disk_img, self.disk_ingame_pos)
		pygame.display.update()
		pygame.time.delay(20)
	

	



	

