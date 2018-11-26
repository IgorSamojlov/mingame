#Bullets Class

import pygame
import time

class Bullet():

	color = (225, 200, 50)

	def __init__(self, b_speed, x_pos, y_pos, b_power, who_is, n_x, n_y):

		self.who = who_is
		self.speed = b_speed
		self.x = x_pos
		self.y = y_pos
		self.nx = n_y
		self.ny = n_y
		self.power = b_power


	def get_power(self):
		return self.power

	def draw_bullet(self, screen):

		pygame.draw.circle(screen, self.color, (self.x, self.y), 20, 10)
		self.move_bullet ()

	def move_bullet (self):
		self.x += self.speed
		self.y = (round(self.y/self.x))*self.x
		print (self.y)


