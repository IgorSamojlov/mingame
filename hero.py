import pygame
import bull
from math import atan2, degrees

class My_hero(pygame.sprite.Sprite):
    def __init__(self, width, height):

        self.w = width
        self.h = height
        self.x = 500
        self.y = 320
        self.speed = 5
        self.bull_speed = 10

        self.image = pygame.image.load('assets/s_sheep.png')
        self.rect = self.image.get_rect(center =(self.x, self.y))


        print ("Cretate Hero")

    def move_hero(self, key):

        if key[pygame.K_a] and (self.x > 0):
            self.x -= self.speed

        if key[pygame.K_s] and (self.y < self.h):
            self.y += self.speed

        if key[pygame.K_d] and (self.x < self.w):
            self.x += self.speed

        if key[pygame.K_w] and (self.y > 0):
            self.y -= self.speed

    def draw_hero(self, scr, pos):

        new_rec = self.rotate_hero(pos)
        scr.blit(new_rec[0], new_rec[1])

    def get_x_hero(self):
        return self.x

    def get_y_pos(self):
        return self.y

    def hero_shoot (self, bulll, pos):

        b = bull.Bullet (1200, 640,
        self.bull_speed, (self.rect.center[0]), (self.rect.center[1]),
        0, 'Hero', pos[0], pos[1])
        bulll.append(b)

    def rotate_hero (self, pos):

        x = pos[0] - self.x
        y = pos[1] - self.y

        a = degrees(atan2((x), (y)))
        a += 180

        rot_img = pygame.transform.rotate(self.image, a)
        self.rect = rot_img.get_rect(center = (self.x, self.y))
        return (rot_img, self.rect)
