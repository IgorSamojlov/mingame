import pygame
import bull

class My_hero(pygame.sprite.Sprite):
    def __init__(self):

        self.x = 500
        self.y = 320
        self.speed = 3

        self.image = pygame.image.load('car.png')

        self.bull_speed = 5
        self.rect = self.image.get_rect(center =(self.x, self.y))

        print ("Cretate Hero")

    def move_hero(self, key):

        if key[pygame.K_a]:
            self.x -= self.speed

        if key[pygame.K_s]:
            self.y += self.speed

        if key[pygame.K_d]:
            self.x += self.speed

        if key[pygame.K_w]:
            self.y -= self.speed

    def draw_hero(self, scr):
        self.rect.x = self.x
        self.rect.y = self.y
        scr.blit(self.image, self.rect)

    def get_x_hero(self):
        return self.x

    def get_y_pos(self):
        return self.y

    def hero_shoot (self, bulll, pos):

        b = bull.Bullet (self.bull_speed,
            self.x, self.y, 10, 'Hero', pos[0], pos[1])
        bulll.append(b)

