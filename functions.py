from Board import *
from Disk import Disk
from Paddles import Paddle
from Constants import *
import pygame

#
def disk_moving():
	disk_moving_in_game = Disk()
	right_paddle_in_game = Paddle("left")
	left_paddle_in_game = Paddle("right")
	background_in_game = Board()
	fill_board_in_game = FillBoard()

	print (disk_moving_in_game.disk_ingame_pos)
	if disk_moving_in_game.disk_ingame_pos.colliderect(right_paddle_in_game.paddle_right_pos) or disk_moving_in_game.disk_ingame_pos.colliderect(left_paddle_in_game.paddle_left_pos):
		disk_moving_in_game.speed_x *= -1
		disk_moving_in_game.disk_after_bounc()

	# check collision with top and bottom of board

	if disk_moving_in_game.disk_ingame_pos.bottom >= SCREEN_HIGHT or disk_moving_in_game.disk_ingame_pos.top <= 0:
		disk_moving_in_game.speed_y *= -1
		disk_moving_in_game.disk_after_bounc()

	if disk_moving_in_game.disk_ingame_pos.right >= SCREEN_WIDTH:
		fill_board_in_game.fill_board("board_right")
		background_in_game.board_static()  # -> check it
		pygame.time.delay(650)
		disk_moving_in_game.disk_ingame_pos.center = (SCREEN_HALF_WIDTH, SCREEN_HALF_HIGHT)
		start_game()

	if disk_moving_in_game.disk_ingame_pos.left <= 0:
		fill_board_in_game.fill_board("board_left")
		background_in_game.board_static()  # -> check it
		pygame.time.delay(650)
		disk_moving_in_game.disk_ingame_pos.center = (SCREEN_HALF_WIDTH, SCREEN_HALF_HIGHT)
		start_game()
	
		
def start_game():
	start_game_board = Board()
	start_game_board.board_appearance()
	new_disk = Disk()
	new_disk.disk_start()
	
# #
# def read_keys_events():
# 	for event in pygame.event.get():
# 		if event.type == pygame.KEYDOWN:
# 			if event.key == pygame.K_DOWN:
# 				PADDLE_SPEED_RIGHT += 10
# 			if event.key == pygame.K_UP:
# 				PADDLE_SPEED_RIGHT -= 10
# 		if event.type == pygame.KEYUP:
# 			if event.key == pygame.K_DOWN:
# 				PADDLE_SPEED_RIGHT -= 10
# 			if event.key == pygame.K_UP:
# 				PADDLE_SPEED_RIGHT += 10
#
# 		if event.type == pygame.KEYDOWN:
# 			if event.key == pygame.K_z:
# 				PADDLE_SPEED_LEFT += 10
# 			if event.key == pygame.K_a:
# 				PADDLE_SPEED_LEFT -= 10
# 		if event.type == pygame.KEYUP:
# 			if event.key == pygame.K_z:
# 				PADDLE_SPEED_LEFT -= 10
# 			if event.key == pygame.K_a:
# 				PADDLE_SPEED_LEFT += 10
	