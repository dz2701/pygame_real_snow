import sys
import pygame
from cloud import Cloud
from snowflakes import Snowflake
from snowmen import Snowman

def check_events(set,scr,cloud,snowflakes):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()
        elif event.type == pygame.KEYDOWN: check_keydown_events(event,set,scr,cloud,snowflakes)
        elif event.type == pygame.KEYUP: check_keyup_events(event,set,scr,cloud)

def update_screen(set, screen, cloud, snowflake, man):
    screen.fill(set.bg_color)
    cloud.blitme()
    cloud.update()
    for snow in snowflake.sprites():
        snow.draw_snowflake()
    man.blitme()
    pygame.display.flip()


def update_flakes(flakes,set,scr):
    flakes.update()
    for snow in flakes.copy():
        if snow.rect.bottom > set.screen_h:
            flakes.remove(snow)

def check_keydown_events(event,set,scr,cloud,snowflakes):
    if event.key == pygame.K_RIGHT: cloud.moving_right = True
    elif event.key == pygame.K_LEFT: cloud.moving_left = True
    elif event.key == pygame.K_UP: cloud.moving_up = True
    elif event.key == pygame.K_DOWN: cloud.moving_down = True
    elif event.key == pygame.K_SPACE:
        new_s =Snowflake(set,scr,cloud)
        snowflakes.add(new_s)

def  check_keyup_events(event,set,scr,cloud):
    if event.key == pygame.K_RIGHT: cloud.moving_right = False
    elif event.key == pygame.K_LEFT: cloud.moving_left = False
    elif event.key == pygame.K_UP: cloud.moving_up = False
    elif event.key == pygame.K_DOWN: cloud.moving_down = False

'''
def create_row(set,scr,cloud,snowflakes,snowmen):
    man = Snowman(set,scr,cloud,snowflakes)
    snowmen.add(man)
    man.blitme()
    print("blitted!")
'''
