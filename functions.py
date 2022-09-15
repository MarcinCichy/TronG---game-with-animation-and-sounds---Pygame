from Board import *
from Disk import Disk
from Paddles import Paddle
from Constants import *
import pygame


left_points = LEFT_POINTS
right_points = RIGHT_POINTS


# set a new disk
def new_disk():
	start_game_board = Board()
	start_game_board.board_appearance()
	renew_disk = Disk()
	renew_disk.disk_start()
	
	
# check collision with paddles and check if disk is stick to the paddle
def collisons(disk, right_paddle, left_paddle, right_paddle_speed, left_paddle_speed, right_paddle_stick, left_paddle_stick):
	if disk.disk_ingame_pos.colliderect(right_paddle.paddle_right_pos) or disk.disk_ingame_pos.colliderect(left_paddle.paddle_left_pos):
		if right_paddle_stick == 1 and disk.disk_ingame_pos.colliderect(right_paddle.paddle_right_pos):
			disk.speed_x = 0
			disk.speed_y = right_paddle_speed
		elif left_paddle_stick == 1 and disk.disk_ingame_pos.colliderect(left_paddle.paddle_left_pos):
			disk.speed_x = 0
			disk.speed_y = left_paddle_speed
		elif right_paddle_stick == -1 and disk.disk_ingame_pos.colliderect(right_paddle.paddle_right_pos) and right_paddle_speed != 0:
			disk.speed_x -= DISK_SPEED_X
			disk.speed_y = right_paddle_speed
		elif left_paddle_stick == -1 and disk.disk_ingame_pos.colliderect(left_paddle.paddle_left_pos) and left_paddle_speed != 0:
			disk.speed_x += DISK_SPEED_X
			disk.speed_y = left_paddle_speed
		# check that below
		elif right_paddle_stick == -1 and disk.disk_ingame_pos.colliderect(right_paddle.paddle_right_pos) and right_paddle_speed == 0:
			disk.speed_x = 0
			disk.speed_y = right_paddle_speed
		elif left_paddle_stick == -1 and disk.disk_ingame_pos.colliderect(left_paddle.paddle_left_pos) and left_paddle_speed == 0:
			disk.speed_x = 0
			disk.speed_y = left_paddle_speed
			
		# check collision with paddles and change the direction of the disc
		# depending on the direction of the paddle
		elif right_paddle_stick == 0 or left_paddle_stick == 0:
			# The disk acceleration after bounce by paddle
			if abs(disk.speed_x) == DISK_SPEED_X and abs(disk.speed_y) == DISK_SPEED_Y:
				disk.speed_x *= ACCELERATION
				disk.speed_y *= ACCELERATION
			if (right_paddle_speed == 10 and disk.speed_y > 0) or (left_paddle_speed == 10 and disk.speed_y > 0):
				disk.speed_x *= -1
			elif (right_paddle_speed == 10 and disk.speed_y < 0) or (left_paddle_speed == 10 and disk.speed_y < 0):
				disk.speed_x *= -1
				disk.speed_y *= -1
			elif (right_paddle_speed == -10 and disk.speed_y < 0) or (left_paddle_speed == -10 and disk.speed_y < 0):
				disk.speed_x *= -1
			elif (right_paddle_speed == -10 and disk.speed_y > 0) or (left_paddle_speed == -10 and disk.speed_y > 0):
				disk.speed_x *= -1
				disk.speed_y *= -1
			elif (right_paddle_speed == 0) or (left_paddle_speed == 0):
				disk.speed_x *= -1
		disk.disk_after_bounc()
		
	# Check collision with top and bottom of board
	if disk.disk_ingame_pos.bottom >= SCREEN_HIGHT or disk.disk_ingame_pos.top <= 0:
		disk.speed_y *= -1
		disk.disk_after_bounc()

		
# Check if the disk has reached its target
# and show by filling in half of the board where the player lost a point
def lost_point(disk, background):
	global left_points, right_points
	end_game(left_points, right_points, background)
	show_points(left_points, right_points)
	if disk.disk_ingame_pos.right >= SCREEN_WIDTH or disk.disk_ingame_pos.left <= 0:
		if disk.disk_ingame_pos.right >= SCREEN_WIDTH:
			left_points += 1
			background.fill_board("board_right")
			# Paddle.paddle_lost_point("right_paddle")
		elif disk.disk_ingame_pos.left <= 0:
			right_points += 1
			background.fill_board("board_left")
			
		# background.board_static()  # -> check it if is needed
		pygame.time.delay(650)
		disk.disk_ingame_pos.center = (SCREEN_HALF_WIDTH, SCREEN_HALF_HIGHT)
		# after lost point, set disk speed at start values
		disk.speed_x = DISK_SPEED_X
		disk.speed_y = DISK_SPEED_Y
		new_disk()


def show_points(l_points, r_points):
	left_points_text = game_font.render(f"{l_points}", False, FONT_COLOR)
	screen.blit(left_points_text, (200, 50))
	right_points_text = game_font.render(f"{r_points}", False, FONT_COLOR)
	screen.blit(right_points_text, (600, 50))


def end_game(l_points, r_points, background):
	if l_points == END_GAME_POINTS or r_points == END_GAME_POINTS:
		background.board_static()
		end_game_text = game_font.render("GAME OVER", False, FONT_COLOR)
		screen.blit(end_game_text, (170, 300))
		pygame.time.delay(3000)
		# menu()
		# left_points = LEFT_POINTS
		# right_points = RIGHT_POINTS
		# disk.speed_x = DISK_SPEED_X
		# disk.speed_y = DISK_SPEED_Y
		# new_disk()