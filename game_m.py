#init
#main

import sys
import pygame
import time
import bull
import hero
import nlo
import explosion

class Game_m ():

    def __init__ (self):

        pygame.init()
        pygame.display.set_caption("My game")

        self.m_keyd = 0

        self.score = 0
        self.hero_name = 'Hero'

        self.rectan = [5, 5, 950, 630]

        self.c_red = (225, 0, 7)
        self.c_bal = (0, 0, 50)
        self.bl = (100, 0, 50)
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 640))

        self.myhero = hero.My_hero(self.rectan)

        self.bullets_group = pygame.sprite.Group()
        self.bullets_group_nlo = pygame.sprite.Group()

        self.nlo_group = pygame.sprite.Group()

        self.nlo = nlo.My_nlo(100, 100, 10)
        self.nlo1 = nlo.My_nlo(600, 200, 10)
        self.nlo_group.add(self.nlo)
        self.nlo_group.add(self.nlo1)

        self.explo = pygame.sprite.Group()

        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.myfont_name = pygame.font.SysFont('Times new roman', 55)

    def draw_score(self):
        pygame.draw.rect(self.screen, self.c_red, [5, 5, 950, 630], 3)
        pygame.draw.rect(self.screen, self.c_red, [953, 5, 245, 630], 3)

        live = self.myfont.render(("Live = " + str(self.myhero.life)), True,
         self.c_red)
        score = self.myfont.render(("Score = " + str(self.score)), True,
         self.c_red)
        name = self.myfont_name.render((self.hero_name), True,
         (150, 200, 150))

        x = round((self.myhero.life*30)/100) + 1010

        pygame.draw.line(self.screen, self.c_red, (1010, 150), (x, 150), 20)

        self.screen.blit(live, (1010, 100))
        self.screen.blit(score, (1010, 70))
        self.screen.blit(name, (1030, 20))

    def get_collide_nlo(self):
        for a in pygame.sprite.groupcollide(self.nlo_group, self.bullets_group,
        False, False):
            for b in pygame.sprite.groupcollide(self.bullets_group,
            self.nlo_group, True, False):
                a.life -= b.power
                if a.life <= 0:
                    self.score += 100

    def get_collide_hero(self):
        a = (pygame.sprite.spritecollideany(self.myhero,
            self.bullets_group_nlo, False))
        if a:
                self.myhero.life -= a.power
                a.kill()

    def draw_game(self):

        self.explo.update()
        self.explo.draw(self.screen)

        self.nlo_group.update(self.myhero.get_hero_pos(),
         self.bullets_group_nlo, self.explo)
        self.nlo_group.draw(self.screen)

        self.bullets_group.update()
        self.bullets_group.draw(self.screen)

        self.bullets_group_nlo.update()
        self.bullets_group_nlo.draw(self.screen)

        self.get_collide_nlo()
        self.get_collide_hero()

        self.draw_score()
        self.myhero.draw_hero(self.screen, (pygame.mouse.get_pos()))

        pygame.display.update ()
        self.clock.tick(60)












