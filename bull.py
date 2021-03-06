#Bullets Class

import pygame
import time
from math import sqrt, atan2, degrees

class Bullet(pygame.sprite.Sprite):

    def __init__(self, w, h, b_speed, x_pos, y_pos, b_power, n_x, n_y):
        pygame.sprite.Sprite.__init__(self)

        self.w = w
        self.h = h
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

        self.image = pygame.image.load('assets/rock.png')
        self.rect = self.image.get_rect(center = (self.x, self.y))

        self.rotate_bul()

    def get_koof (self):
        if (self.dx - self.nx) != 0:
            return((self.dy - self.ny)/(self.dx - self.nx))
        else:
            return(0.0001)

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

    def rotate_bul(self):
        x = self.dx - self.nx
        y = self.dy - self.ny

        a = degrees(atan2((x), (y)))
        a += 180

        rot_img = pygame.transform.rotate(self.image, a)
        self.image = rot_img
        self.rect = rot_img.get_rect(center = (self.x, self.y))
