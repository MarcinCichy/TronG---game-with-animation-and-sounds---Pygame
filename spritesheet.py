# from https://github.com/russs123/pygame_tutorials/blob/main/sprite_tutorial/spritesheet.py
from Constants import *


class SpriteSheet:
	def __init__(self, image):
		self.sheet = image
	
	def get_image(self, frame, width, height, scale, colour):
		image = pygame.Surface((width, height)).convert_alpha()
		image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
		image = pygame.transform.scale(image, (width * scale, height * scale))
		image.set_colorkey(colour)
		return image
	
# def sprite_animation(animation_steps, x_frame_size, y_frame_size, scale, alpha_colour, anim_pos_x, anim_pos_y):
# 	# animation_steps = frames in spritesheet
# 	animation_list = []
#
# 	for x in range(animation_steps):
# 		animation_list.append(right_sprite_sheet.get_image(x, x_frame_size, y_frame_size, scale, alpha_colour))
#
# 	for frame in range(len(animation_list)):
# 		# to check if all images are in animation_list, change x position of screen.blit to "frame*50 for example"
# 		screen.blit(animation_list[frame], (anim_pos_x, anim_pos_y))
# 		pygame.display.update()
# 		pygame.time.delay(80)