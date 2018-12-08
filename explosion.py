#explo

import pygame
import time

class Expl(pygame.sprite.Sprite):

    def __init__ (self, x_p, y_p):
        pygame.sprite.Sprite.__init__(self)

        self.x = x_p
        self.y = y_p

        self.images = []
        self.frame = 0
        self.life = True

        self.images.append('assets/1.png')
        self.images.append('assets/2.png')
        self.images.append('assets/3.png')
        self.images.append('assets/4.png')
        self.images.append('assets/5.png')
        self.images.append('assets/6.png')
        self.images.append('assets/7.png')
        self.images.append('assets/8.png')
        self.images.append('assets/9.png')
        self.images.append('assets/10.png')
        self.images.append('assets/11.png')
        self.images.append('assets/12.png')
        self.images.append('assets/13.png')

        self.image = pygame.image.load(self.images[self.frame])

        self.rect = self.image.get_rect(center = (self.x, self.y))

        self.cr_time = int(round(time.time() * 1000))

    def update(self):

        if ((int(round(time.time() * 1000)) - self.cr_time) > 40):
            if self.frame < 12:
                self.cr_time = (int(round(time.time() * 1000)))
                self.frame += 1
                self.image = pygame.image.load(self.images[self.frame])
                self.rect = self.image.get_rect(center = (self.x, self.y))
            if (self.frame == 12):
                self.kill ()
