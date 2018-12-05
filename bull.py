#Bullets Class

import pygame
import time
from math import sqrt

class Bullet(pygame.sprite.Sprite):



    def __init__(self, w, h, b_speed, x_pos, y_pos, b_power, who_is, n_x, n_y):
        pygame.sprite.Sprite.__init__(self)

        self.w = w
        self.h = h

        self.who = who_is
        self.speed = 0
        self.put = b_speed
        self.x = 0
        self.y = 0
        self.nx = n_x
        self.ny = n_y
        self.dx = x_pos
        self.dy = y_pos
        self.koof = self.get_koof()
        self.power = b_power

        self.image = pygame.image.load('assets/1.png')
        self.rect = self.image.get_rect(center = (self.x, self.y))


    def get_koof (self):
        return((self.dy - self.ny)/(self.dx - self.nx))

    def get_power(self):
        return self.power

    def update(self):
        a = self.move_bullet ()
        self.rect.centerx = a[0]
        self.rect.centery = a[1]
        if (a[0] <= 0) or (a[0] >= self.w):
            self.kill()
        if (a[1] <= 0) or (a[1] >= self.h):
            self.kill()

    def move_bullet (self):

        self.speed += self.put

        self.x = (sqrt((self.speed**2)/(1+(self.koof**2))))

        self.y = (self.koof*self.x)

        if (self.nx < self.dx):
            self.x *= -1
        if (self.nx < self.dx) and (self.ny > self.dy):
            self.y *= -1
        if(self.nx < self.dx) and (self.ny < self.dy):
            self.y *= -1

        return (round(self.x + self.dx), round(self.y + self.dy))

    def get_x_y (self):
        return (round(self.x + self.dx), round(self.y + self.dy))
