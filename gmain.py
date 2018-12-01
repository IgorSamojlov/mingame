import sys
import pygame
import time
import bull
import hero
import nlo

RED = (225, 0, 7)
BAL = (0, 0, 50)
clock = pygame.time.Clock()

def bull_dr(bul, scr):
    if bul:
            for b in range(0, len(bul)):
                bul[b].draw_bullet (scr)
            if not bul[b].life:
                del bul[b]
                print ("Kill")


def main():

    millis = int(round(time.time() * 1000))
    clo = pygame.time.Clock()
    keyd = 0

    myhero = hero.My_hero(1200, 640)

    nl = []
    bullets = []

    n = nlo.My_nlo (100, 100, 2)
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

                myhero.hero_shoot(bullets, p)

            if event.type == pygame.MOUSEBUTTONUP:
                m_keyd = 0

        kd = pygame.key.get_pressed()
        if kd:
            myhero.move_hero(kd)

        myhero.draw_hero(screen, (pygame.mouse.get_pos()))

        bull_dr (bullets, screen)
        nl[0].draw_nlo (screen, (pygame.mouse.get_pos()))
        nl[0].nlo_shoot (bullets, (pygame.mouse.get_pos()))

        pygame.display.update ()
        clock.tick(60)

main ()
