import pygame
import bull
from math import atan2, degrees

class My_hero(pygame.sprite.Sprite):
    def __init__(self, rectan):

        self.h_rectan = rectan
        self.x = 500
        self.y = 320
        self.life = 300
        self.speed = 5
        self.bull_speed = 20

        self.image = pygame.image.load('assets/s_sheep.png')
        self.rect = self.image.get_rect(center =(self.x, self.y))

        print ("Cretate Hero")

    def move_hero(self, key):

        if key[pygame.K_a] and (self.x > self.h_rectan[0]):
            self.x -= self.speed

        if key[pygame.K_s] and (self.y < self.h_rectan[3]):
            self.y += self.speed

        if key[pygame.K_d] and (self.x < self.h_rectan[2]):
            self.x += self.speed

        if key[pygame.K_w] and (self.y > self.h_rectan[1]):
            self.y -= self.speed

    def draw_hero(self, scr, pos):

        new_rec = self.rotate_hero(pos)
        scr.blit(new_rec[0], new_rec[1])

    def get_hero_pos(self):
        return (self.x, self.y)

    def hero_shoot (self, b_group, pos):

        bullet = bull.Bullet (1200, 640,
        self.bull_speed, (self.rect.center[0]), (self.rect.center[1]),
        30, pos[0], pos[1])
        b_group.add(bullet)

    def rotate_hero (self, pos):

        x = pos[0] - self.x
        y = pos[1] - self.y

        a = degrees(atan2((x), (y)))
        a += 180

        rot_img = pygame.transform.rotate(self.image, a)
        self.rect = rot_img.get_rect(center = (self.x, self.y))
        return (rot_img, self.rect)
