from sys import exit
import functions
import pygame
from paddles import Paddle
from disk import Disk
import menu
from constants import *
from board import Board



background = Board()
disk = Disk()
left_paddle = Paddle("left")
right_paddle = Paddle("right")
menu = menu.Menu()


def main_game():
	global PADDLE_SPEED_RIGHT, PADDLE_SPEED_LEFT, RIGHT_PADDLE_STICK_DISK, LEFT_PADDLE_STICK_DISK
	game_on = True
	while game_on:
		
		# ---------- pygame events to control game and paddles  ----------
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_on = False
			
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
				if event.key == pygame.K_RALT:
					RIGHT_PADDLE_STICK_DISK = 1
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_RALT:
					RIGHT_PADDLE_STICK_DISK = -1
			
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
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LALT:
					LEFT_PADDLE_STICK_DISK = 1
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LALT:
					LEFT_PADDLE_STICK_DISK = -1
		
		# ----------------------------- game logic -----------------------------
		functions.collisons(disk, right_paddle, left_paddle, PADDLE_SPEED_RIGHT, PADDLE_SPEED_LEFT, RIGHT_PADDLE_STICK_DISK,
							LEFT_PADDLE_STICK_DISK)
		
		disk.disk_move()
		left_paddle.show_paddles()
		right_paddle.show_paddles()
		right_paddle.paddle_move(PADDLE_SPEED_RIGHT)
		left_paddle.paddle_move(PADDLE_SPEED_LEFT)
		
		functions.lost_point(disk, background)
		
		pygame.display.update()
		clock.tick(60)
		