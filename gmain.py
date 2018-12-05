import sys
import pygame
import time
import bull
import hero
import nlo
import explosion

RED = (225, 0, 7)
BAL = (0, 0, 50)
clock = pygame.time.Clock()


def get_collide(bul_gr, nlo_gr):

    for a in pygame.sprite.groupcollide(nlo_gr, bul_gr, False, False):
        for b in pygame.sprite.groupcollide(bul_gr, nlo_gr, True, False):
            a.life -= b.power
            print (b.power)
            print ("a.lifi = " + str(a.life))



def main():

    keyd = 0

    explo = pygame.sprite.Group()

    myhero = hero.My_hero(1200, 640)

    nlo_group = pygame.sprite.Group()
    m_nlo = nlo.My_nlo (300, 200, 2)
    nlo_group.add(m_nlo)

    bullets_group = pygame.sprite.Group()
    bullets_group_nlo = pygame.sprite.Group()

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

                myhero.hero_shoot(bullets_group, p)

            if event.type == pygame.MOUSEBUTTONUP:
                m_keyd = 0

        kd = pygame.key.get_pressed()
        if kd:
            myhero.move_hero(kd)

        myhero.draw_hero(screen, (pygame.mouse.get_pos()))


        explo.update()
        explo.draw(screen)

        nlo_group.update(pygame.mouse.get_pos(), bullets_group_nlo)
        nlo_group.draw(screen)

        bullets_group.update()
        bullets_group.draw(screen)

        bullets_group_nlo.update()
        bullets_group_nlo.draw(screen)

        get_collide(bullets_group, nlo_group)

        pygame.display.update ()
        clock.tick(60)

main ()
