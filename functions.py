from Paddles import Paddle
from Board import *
from Disk import Disk
from Constants import *


def disk_bounc():
	if Disk.disk_ingame_pos.colliderect(right_paddle.paddle_right_pos) or disk.disk_ingame_pos.colliderect(
			left_paddle.paddle_left_pos):
		Disk.speed_x *= -1
		Disk.disk_after_bounc()
	
	if Disk.disk_ingame_pos.bottom >= SCREEN_HIGHT or Disk.disk_ingame_pos.top <= 0:
		Disk.speed_y *= -1
		Disk.disk_after_bounc()
	
	if Disk.disk_ingame_pos.right >= SCREEN_WIDTH:
		Board.fill_board("right")
	
	if Disk.disk_ingame_pos.left <= 0:
		Board.fill_board("left")