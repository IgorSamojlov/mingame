#init
#main

import sys
import pygame
import time
import bull
import hero
import nlo
import explosion
from random import randint

class Game_m ():

    def __init__ (self):

        pygame.init()
        pygame.display.set_caption("My game")

        self.game_paused = 0
        self.timer = [(int(round(time.time() * 100))), 1]

        self.score = 0
        self.hero_name = 'Hero'

        self.rectan = [5, 5, 950, 630]

        self.c_gr = (0, 150, 220)
        self.c_bal = (0, 0, 50)
        self.bl = (100, 0, 50)
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 640))

        self.myhero = hero.My_hero(self.rectan)

        self.bullets_group = pygame.sprite.Group()
        self.bullets_group_nlo = pygame.sprite.Group()

        self.nlo_group = pygame.sprite.Group()

        self.explo = pygame.sprite.Group()

        self.myfont = pygame.font.SysFont('Comic Sans MS', 25)
        self.myfont_name = pygame.font.SysFont('Times new roman', 55)

    def draw_score(self):
        pygame.draw.rect(self.screen, self.c_gr, [5, 5, 950, 630], 3)
        pygame.draw.rect(self.screen, self.c_gr, [953, 5, 245, 630], 3)

        live = self.myfont.render(("Live = " + str(self.myhero.life)), True,
         self.c_gr)
        score = self.myfont.render(("Score = " + str(self.score)), True,
         self.c_gr)
        name = self.myfont_name.render((self.hero_name), True,
         (150, 200, 150))

        x = round((self.myhero.life*40)/100) + 1010
        col = (255, (x - 890), 100)

        pygame.draw.line(self.screen, col, (1010, 180), (x, 180), 20)

        self.screen.blit(live, (1010, 120))
        self.screen.blit(score, (1010, 80))
        self.screen.blit(name, (1020, 20))

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
                if self.myhero.life <= 0:
                    self.game_over()

    def game_add_nlo(self, nlo_group):
        if (int(round(time.time())) * 100 -  self.timer[0]) >= 800:
            self.timer[0] = int(round(time.time())) * 100
            self.timer[1] += 1
            a = self.timer[1]

            while (a != 0):
                nnlo = nlo.My_nlo((randint(-10, 1000)), (randint(-50, 10)), 5)
                nlo_group.add(nnlo)
                a -= 1

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

        self.game_add_nlo(self.nlo_group)

        pygame.display.update ()
        self.clock.tick(60)

    def game_over(self):
        myfont = pygame.font.SysFont('Comic Sans MS', 120)
        myfont_p = pygame.font.SysFont('Times new roman', 40)
        press = myfont_p.render("Press any mouse button i igray zanovo",
         True, (200, 200, 100))
        game = myfont.render("GAME OVER!", True, (200, 200, 100))

        s = str(self.hero_name) + " score " + str(self.score)

        t_score = myfont_p.render(s, True, (200, 200, 100))
        self.screen.blit(game, (150, 150))
        self.screen.blit(press, (220, 350))
        self.screen.blit(t_score, (220, 400))

        self.game_paused = True
        self.score = 0
        self.nlo_group.empty()
        self.bullets_group.empty()
        self.bullets_group_nlo.empty()
        self.timer = [(int(round(time.time() * 100))), 1]
        self.myhero.life = 300
