import pygame as pg
from pygame.sprite import Sprite
class Snowflake(Sprite):
    def __init__(self,set,scr,cloud):
        super().__init__()
        self.scr = scr
        self.image = pg.image.load('images/snowflake.bmp')
        self.rect = pg.Rect(0,0,set.snowflake_width, set.snowflake_height)
        self.rect.top = cloud.rect.bottom
        self.rect.centerx = cloud.rect.centerx
        self.y = float(self.rect.y)

        self.speed_factor = set.snowflake_speed_factor
        self.factor = True

    def update(self):
        if self.factor:
            self.y -= self.speed_factor
            self.rect.y = self.y


    def draw_snowflake(self):
        self.scr.blit(self.image,self.rect)
