#Nlo Class
import bull
import time
import pygame
from math import sqrt

class My_nlo(pygame.sprite.Sprite):
    def __init__ (self, nlo_x, nlo_y, nlo_power):

        self.speed = 2
        self.x = nlo_x
        self.y = nlo_y
        self.power = nlo_power
        self.put = 3
        self.koof = 0
        self.image = pygame.image.load('assets/nlo.png')
        self.rect = self.image.get_rect(center =(self.x, self.y))

        self.cr_time = int(round(time.time() * 1000))


    def draw_nlo (self, scr, pos):
        self.nlo_move (pos)
        scr.blit(self.image, self.rect)

    def nlo_shoot(self, b, pos):
        print ((int(round(time.time())* 1000 - self.cr_time)))
        if (int(round(time.time())* 1000 - self.cr_time) > 400):

            print ("Shooot")
            b1 = bull.Bullet (1200, 640,
            10, (self.rect.center[0]), (self.rect.center[1]),
            0, 'Hero', pos[0], pos[1])
            b.append(b1)

    def nlo_get_pos (self):
        return (self.x, self.y)

    def nlo_move(self, pos):

        if (int(round(time.time())* 1000 - self.cr_time) > 100):
            self.cr_time = int(round(time.time() * 1000))
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

    def get_koof (self, pos):
        return(abs((self.y - pos[1])/(self.x - pos[0])))
