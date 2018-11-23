import sys
import pygame
import time 
import bull

RED = (225, 0, 50)
BAL = (0, 0, 0)


def main():
	millis = int(round(time.time() * 1000))

	keyd = 0

	bul = bull.Bullet (10, 10, 10, 0)
	nloo = bull.My_nlo (10, 10, 10)

	pygame.init()
	screen = pygame.display.set_mode((800, 600))
	pygame.display.set_caption("My game")

	while True:
		for event in pygame.event.get ():	
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.MOUSEMOTION:
				print (event.pos)
				print (millis)
			elif event.type == pygame.MOUSEBUTTONDOWN:
			
				keyd = 1
				#print (keyd)

			elif event.type == pygame.MOUSEBUTTONUP:
				keyd = 0
				#print (keyd)
			
			if keyd == 1:

				if int(round(time.time() * 1000)) > millis:
					print ((int(round(time.time() * 1000)) - millis))

				screen.fill(BAL)
				pygame.draw.circle(screen, RED, event.pos, 20)
				bul.draw_bullet (screen)				

			if int((round(time.time() * 1000)) - millis) > 1000:
					print ((int(round(time.time() * 1000)) - millis))
					b = nloo.nlo_shoot()
					nloo.draw_nlo (screen)
					b.draw_bullet (screen)
		
		pygame.display.update ()

	pygame.disply.flip()


main ()