import pygame as pg
from pygame.sprite import Sprite

class Snowman(Sprite):
    def __init__(self,set,scr,cloud,snowflakes):
        super().__init__()
        self.scr = scr
        self.set = set
        self.image1 = pg.image.load('images/snowman_1.bmp')
        self.image2 = pg.image.load('images/snowman_2.bmp')
        self.image3 = pg.image.load('images/snowman_3.bmp')
        self.rect = self.image1.get_rect()

        self.rect.centerx = 200
        self.rect.centery = set.screen_h -50

        #coordination of location
    def blitme(self):
        self.scr.blit(self.image1,self.rect)
