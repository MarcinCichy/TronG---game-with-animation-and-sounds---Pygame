""" Exam at mentoring program "Za rączkę"
			Game "PONG"
										"""

import functions
from Paddles import Paddle
from Board import *
from Disk import Disk
from Constants import *
from sys import exit


pygame.init()
pygame.display.set_caption('Tron PONG')
clock = pygame.time.Clock()

screen.fill(BKG_COLOR)

background = Board()
disk = Disk()
left_paddle = Paddle("left")
right_paddle = Paddle("right")
fillboard = FillBoard()

functions.start_game()

while True:
	# ----------------------------- game logic -----------------------------
	# check collision with paddles and
	# change the direction of the disc depending on the direction of the paddle
	if disk.disk_ingame_pos.colliderect(right_paddle.paddle_right_pos) or disk.disk_ingame_pos.colliderect(left_paddle.paddle_left_pos):
		if (PADDLE_SPEED_RIGHT == 10 and disk.speed_y > 0) or (PADDLE_SPEED_LEFT == 10 and disk.speed_y > 0):
			disk.speed_x *= -1
		elif (PADDLE_SPEED_RIGHT == 10 and disk.speed_y < 0) or (PADDLE_SPEED_LEFT == 10 and disk.speed_y < 0):
			disk.speed_x *= -1
			disk.speed_y *= -1
		if (PADDLE_SPEED_RIGHT == -10 and disk.speed_y < 0) or (PADDLE_SPEED_LEFT == -10 and disk.speed_y < 0):
			disk.speed_x *= -1
		elif (PADDLE_SPEED_RIGHT == -10 and disk.speed_y > 0) or (PADDLE_SPEED_LEFT == -10 and disk.speed_y > 0):
			disk.speed_x *= -1
			disk.speed_y *= -1
		disk.disk_after_bounc()
	

	# Check collision with top and bottom of board
	if disk.disk_ingame_pos.bottom >= SCREEN_HIGHT or disk.disk_ingame_pos.top <= 0:
		disk.speed_y *= -1
		disk.disk_after_bounc()
	
	# Check if the disk has reached its target
	# and show by filling in half of the board where the player lost a point
	if disk.disk_ingame_pos.right >= SCREEN_WIDTH or disk.disk_ingame_pos.left <= 0:
		if disk.disk_ingame_pos.right >= SCREEN_WIDTH:
			fillboard.fill_board("board_right")
		elif disk.disk_ingame_pos.left <= 0:
			fillboard.fill_board("board_left")
		background.board_static()  # -> check it
		pygame.time.delay(650)
		disk.disk_ingame_pos.center = (SCREEN_HALF_WIDTH, SCREEN_HALF_HIGHT)
		functions.start_game()

	#functions.disk_moving()

	# ---------- pygame events to control game and paddles  ----------
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				PADDLE_SPEED_RIGHT += 10
			if event.key == pygame.K_UP:
				PADDLE_SPEED_RIGHT -= 10
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_DOWN:
				PADDLE_SPEED_RIGHT -= 10
			if event.key == pygame.K_UP:
				PADDLE_SPEED_RIGHT += 10

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_z:
				PADDLE_SPEED_LEFT += 10
			if event.key == pygame.K_a:
				PADDLE_SPEED_LEFT -= 10
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_z:
				PADDLE_SPEED_LEFT -= 10
			if event.key == pygame.K_a:
				PADDLE_SPEED_LEFT += 10
	print(disk.speed_x, disk.speed_y)
	print("DS:", DISK_SPEED_X, DISK_SPEED_Y)
	disk.disk_move()
	left_paddle.show_paddles()
	right_paddle.show_paddles()
	right_paddle.paddle_move(PADDLE_SPEED_RIGHT)
	left_paddle.paddle_move(PADDLE_SPEED_LEFT)

	pygame.display.update()
	clock.tick(60)

	
	