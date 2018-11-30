import sys
import pygame
import time
import bull
import hero
import nlo

RED = (225, 0, 7)
BAL = (0, 0, 50)
clock = pygame.time.Clock()


def main():

    millis = int(round(time.time() * 1000))
    clo = pygame.time.Clock()
    keyd = 0

    myhero = hero.My_hero()

    nl = []
    bullets = []

    for i in range(1, 5):
        n = nlo.My_nlo (i + 20, 2, 2)
        nl.append (n)

    pygame.init()
    screen = pygame.display.set_mode((1200, 640))
    pygame.display.set_caption("My game")

    while True:

        screen.fill(BAL)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                m_keyd = 1
                p = pygame.mouse.get_pos()
                print (p)
                b = bull.Bullet (1200, 640, 10, myhero.x, myhero.y, 0, 'Hero', p[0], p[1])

                bullets.append(b)

            if event.type == pygame.MOUSEBUTTONUP:
                m_keyd = 0

            # if event.type == pygame.KEYDOWN:
            #     keyd = True
        kd = pygame.key.get_pressed()
        if kd:
            myhero.move_hero(kd)

        myhero.draw_hero(screen)
        if bullets:
            for b in range(0, len(bullets)):
                bullets[b].draw_bullet (screen)


        pygame.display.update ()
        clock.tick(60)

main ()
