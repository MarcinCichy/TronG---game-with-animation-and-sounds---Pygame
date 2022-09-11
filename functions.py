from Board import *
from Disk import Disk
from Paddles import Paddle
from Constants import *
import pygame

#
# def disk_moving():
# 	disk_moving_in_game = Disk()
# 	right_paddle_in_game = Paddle("left")
# 	left_paddle_in_game = Paddle("right")
# 	background_in_game = Board()
# 	fill_board_in_game = FillBoard()
#
# 	print (disk_moving_in_game.disk_ingame_pos)
# 	if disk_moving_in_game.disk_ingame_pos.colliderect(right_paddle_in_game.paddle_right_pos) or disk_moving_in_game.disk_ingame_pos.colliderect(left_paddle_in_game.paddle_left_pos):
# 		disk_moving_in_game.speed_x *= -1
# 		disk_moving_in_game.disk_after_bounc()
#
# 	# check collision with top and bottom of board
#
# 	if disk_moving_in_game.disk_ingame_pos.bottom >= SCREEN_HIGHT or disk_moving_in_game.disk_ingame_pos.top <= 0:
# 		disk_moving_in_game.speed_y *= -1
# 		disk_moving_in_game.disk_after_bounc()
#
# 	if disk_moving_in_game.disk_ingame_pos.right >= SCREEN_WIDTH:
# 		fill_board_in_game.fill_board("board_right")
# 		background_in_game.board_static()  # -> check it
# 		pygame.time.delay(650)
# 		disk_moving_in_game.disk_ingame_pos.center = (SCREEN_HALF_WIDTH, SCREEN_HALF_HIGHT)
# 		start_game()
#
# 	if disk_moving_in_game.disk_ingame_pos.left <= 0:
# 		fill_board_in_game.fill_board("board_left")
# 		background_in_game.board_static()  # -> check it
# 		pygame.time.delay(650)
# 		disk_moving_in_game.disk_ingame_pos.center = (SCREEN_HALF_WIDTH, SCREEN_HALF_HIGHT)
# 		start_game()
	
		
def start_game():
	start_game_board = Board()
	start_game_board.board_appearance()
	new_disk = Disk()
	new_disk.disk_start()
	
def collisons(disk, right_paddle, left_paddle):
	print(f'Start disk_speed={disk.speed_x}')
	# if disk.speed_x > DISK_SPEED_X or disk.speed_y > DISK_SPEED_Y:
	# 	disk.speed_x -= ACCELERATION
	# 	disk.speed_y -= ACCELERATION
	if disk.disk_ingame_pos.colliderect(right_paddle.paddle_right_pos) or disk.disk_ingame_pos.colliderect(
			left_paddle.paddle_left_pos):
		# disk.speed_x += ACCELERATION
		# disk.speed_y += ACCELERATION
		if (PADDLE_SPEED_RIGHT == 10 and disk.speed_y > 0) or (PADDLE_SPEED_LEFT == 10 and disk.speed_y > 0):
			disk.speed_x *= -1
		elif (PADDLE_SPEED_RIGHT == 10 and disk.speed_y < 0) or (PADDLE_SPEED_LEFT == 10 and disk.speed_y < 0):
			disk.speed_x *= -1
			disk.speed_y *= -1
		elif (PADDLE_SPEED_RIGHT == -10 and disk.speed_y < 0) or (PADDLE_SPEED_LEFT == -10 and disk.speed_y < 0):
			disk.speed_x *= -1
		elif (PADDLE_SPEED_RIGHT == -10 and disk.speed_y > 0) or (PADDLE_SPEED_LEFT == -10 and disk.speed_y > 0):
			disk.speed_x *= -1
			disk.speed_y *= -1
		elif (PADDLE_SPEED_RIGHT == 0) or (PADDLE_SPEED_LEFT == 0):
			disk.speed_x *= -1
		disk.disk_after_bounc()
		print(f'End disk_speed={disk.speed_x}')
	# Check collision with top and bottom of board
	if disk.disk_ingame_pos.bottom >= SCREEN_HIGHT or disk.disk_ingame_pos.top <= 0:
		disk.speed_y *= -1
	
		disk.disk_after_bounc()