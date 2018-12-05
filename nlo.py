#Nlo Class
import bull
import time
import pygame
from math import sqrt

class My_nlo(pygame.sprite.Sprite):
    def __init__ (self, nlo_x, nlo_y, nlo_power):

        pygame.sprite.Sprite.__init__(self)

        self.life = 100
        self.speed = 1
        self.x = nlo_x
        self.y = nlo_y
        self.power = nlo_power
        self.put = 1
        self.koof = 0
        self.image = pygame.image.load('assets/nlo.png')
        self.rect = self.image.get_rect(center =(self.x, self.y))

        self.time_m = int(round(time.time() * 1000))
        self.time_sh = int(round(time.time() * 1000))


    def nlo_shoot(self, pos, b_group):
        #print ((int(round(time.time())* 1000 - self.cr_time)))
        if (int(round(time.time())* 1000 - self.time_sh) > 100):
            self.time_sh = (int(round(time.time())* 1000))

            bullet = bull.Bullet (1200, 640,
            10, (self.x), (self.y),
            0, 'Hero', pos[0], pos[1])
            b_group.add(bullet)

    def nlo_get_pos (self):
        return (self.x, self.y)

    def nlo_move(self, pos, b_group):
        if (int(round(time.time())* 1000 - self.time_m) > 20):
            self.time_m = int(round(time.time() * 1000))
            self.koof = self.get_koof(pos)

            a = abs(sqrt((self.speed**2)/(1+(self.koof**2))))

            if (self.x < pos[0]):
                self.x += a

            if (self.x > pos[0]):
                self.x -= abs(a)

            if (self.y < pos[1]):
                self.y += abs(a*self.koof)

            if (self.y > pos[1]):
                self.y -= abs(a*self.koof)

            self.rect.centerx = self.x
            self.rect.centery = self.y
            self.nlo_shoot(pos, b_group)

    def get_koof (self, pos):
        return(abs((self.y - pos[1])/(self.x - pos[0])))

    def update(self, pos, b):
        self.nlo_move(pos, b)
        self.check_life()

    def check_life(self):
        if self.life <= 0:
            self.kill()



