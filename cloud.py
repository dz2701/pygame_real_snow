import pygame as pg
class Cloud():
     def __init__(self,settings,screen):
         self.screen = screen
         self.set = settings
         self.image = pg.image.load('images/cloud.bmp')
         self.rect = self.image.get_rect()
         self.screen_rect = screen.get_rect()
         self.rect.centerx = self.screen_rect.centerx
         self.rect.bottom = self.screen_rect.bottom
         self.moving_right, self.moving_left, self.moving_up, self.moving_down = False, False, False, False
         self.center = float(self.rect.centerx)
         self.y = self.rect.top


     def blitme(self):
        self.screen.blit(self.image, self.rect)
     def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.set.cloud_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.set.cloud_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.y -= self.set.cloud_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.set.cloud_speed
        self.rect.centerx = int(self.center)
