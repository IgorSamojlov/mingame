import sys
import pygame
import time
import bull
import hero

RED = (225, 0, 50)
BAL = (0, 0, 200)


def main():

	millis = int(round(time.time() * 1000))
	clo = pygame.time.Clock()
	keyd = 0
	m_keyd = 0

	a = 0

	myhero = hero.My_hero()


	nlo = []

	bullets = []

	for i in range(1, 5):
		n = bull.My_nlo (i + 20, 2, 2)
		nlo.append (n)

	pygame.init()
	screen = pygame.display.set_mode((1200, 640))
	pygame.display.set_caption("My game")



	while True:

		screen.fill(BAL)

		for event in pygame.event.get ():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				m_keyd = 1
				p =pygame.mouse.get_pos()
				b = bull.Bullet (1, myhero.x, myhero.y, 0, 'Hero', p[0], p[1])
				bullets.append(b)


			if event.type == pygame.MOUSEBUTTONUP:
				m_keyd = 0

			if event.type == pygame.KEYDOWN:
				keyd = 1

			if event.type == pygame.KEYUP:
				keyd = 0

		if keyd == 1:
			kd = pygame.key.get_pressed()
			myhero.move_hero (kd)

		myhero.draw_hero (screen)
		if len(bullets) > 0:
			bullets[0].draw_bullet (screen)

		pygame.display.update ()

main ()
