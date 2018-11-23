import pygame

class Bullet():

	color = (225, 200, 50)
	
	def __init__(self, b_speed, x_pos, y_pos, b_power):

		self.speed = b_speed
		self.x = x_pos
		self.y = y_pos
		self.power = b_power

	def get_power(self):
		return self.power

	def draw_bullet(self, screen):
		
		self.move_bullet ()

		pygame.draw.circle(screen, self.color, (self.x, self.y), 20, 10)

	def move_bullet (self):
		self.x += self.speed


class My_nlo():
	def __init__ (self, nlo_x, nlo_y, nlo_power):
		self.x = nlo_x
		self.y = nlo_y
		self.power = nlo_power


	def draw_nlo (self, scr):
			pygame.draw.circle(scr, (100, 100, 100), (self.x, self.y), 20, 10)

	def nlo_shoot(self):
			b = Bullet (5, 100, 100, 0)
			return (b)



