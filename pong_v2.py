""" Exam at mentoring program "Za rączkę"
			Game "PONG"
										"""
import random
import time

import pygame
import spritesheet
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
left_paddle = Paddle("lewa")
right_paddle = Paddle("prawa")
filldboard = FillBoard()


def start_game():
	background.board_appearance()  # it should be run only once at start and every time when point is hit
	#disk.disk_appears_anim()
	disk.disk_start()

start_game()


while True:
	
	if disk.disk_ingame_pos.colliderect(right_paddle.paddle_right_pos) or disk.disk_ingame_pos.colliderect(
			left_paddle.paddle_left_pos):
		disk.speed_x *= -1
		disk.disk_after_bounc()
	
	if disk.disk_ingame_pos.bottom >= SCREEN_HIGHT or disk.disk_ingame_pos.top <= 0:
		disk.speed_y *= -1
		disk.disk_after_bounc()
	
	if disk.disk_ingame_pos.right >= SCREEN_WIDTH:
		filldboard.fill_board("right")
		disk.disk_start()
		pygame.time.delay(50)
		
	if disk.disk_ingame_pos.left <= 0:
		filldboard.fill_board("left")
		disk.disk_start()
		pygame.time.delay(50)
	
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

	disk.disk_move()
	left_paddle.show_paddles()
	right_paddle.show_paddles()
	right_paddle.paddle_move(PADDLE_SPEED_RIGHT)
	left_paddle.paddle_move(PADDLE_SPEED_LEFT)

	pygame.display.update()
	clock.tick(60)

	
	