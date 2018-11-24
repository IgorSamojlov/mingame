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

		self.move_bullet ()

		pygame.draw.circle(screen, self.color, (self.x, self.y), 20, 10)

	def move_bullet (self):
		self.x += self.speed
		self.y = (round(self.y/self.x))*self.x


class My_nlo():
	def __init__ (self, nlo_x, nlo_y, nlo_power):
		self.speed = 3
		self.x = nlo_x
		self.y = nlo_y
		self.power = nlo_power
		self.cr_time = int(round(time.time() * 1000))


	def draw_nlo (self, scr):
			pygame.draw.circle(scr, (100, 100, 100), (self.x, self.y), 20, 10)

	def nlo_shoot(self):
			print ("Shooot")
			b = Bullet (5, 100, 100, 0, 10, 10, 10)
			return (b)

	def nlo_get_pos (self):
		return (self.x, self.y)

	def nlo_move(self, x, y):
		if ( int(round(time.time())* 1000 - self.cr_time) > 200):
			self.x =+ self.speed


