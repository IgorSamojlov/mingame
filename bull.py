#Bullets Class

import pygame
import time
import math

class Bullet():

    color = (225, 200, 50)

    def __init__(self, w, h, b_speed, x_pos, y_pos, b_power, who_is, n_x, n_y):

        self.w = w
        self.h = h

        self.who = who_is
        self.speed = 0
        self.put = 3
        self.x = 0
        self.y = 0
        self.nx = n_x
        self.ny = n_y
        self.dx = x_pos
        self.dy = y_pos
        self.koof = self.get_koof()
        self.power = b_power
        self.life = True

    def get_koof (self):
        print(((self.dy - self.ny)/(self.dx - self.nx)))
        return((self.dy - self.ny)/(self.dx - self.nx))

    def get_power(self):
        return self.power

    def draw_bullet(self, screen):
        a = self.move_bullet ()
        pygame.draw.circle(screen, self.color, (a[0], a[1]), 2, 2)


    def move_bullet (self):

        self.speed += self.put

        self.x = (math.sqrt((self.speed**2)/(1+(self.koof**2))))

        self.y = (self.koof*self.x)

        if (self.nx < self.dx):
            self.x *= -1
        if (self.nx < self.dx) and (self.ny > self.dy):
            self.y *= -1
        if(self.nx < self.dx) and (self.ny < self.dy):
            self.y *=-1

        if (round(self.x + self.dx)) > self.w or (round(self.x + self.dx)) < 0:
            self.life = False
        if (round(self.y + self.dy)) > self.h or (round(self.y + self.dy)) < 0:
            self.life = False

        return (round(self.x + self.dx), round(self.y + self.dy))
