import sys
import pygame as pg
from settings import Settings
from pygame.sprite import Group
from cloud import Cloud
import gamefunctions as gf
from snowflakes import Snowflake
from snowmen import Snowman
def run_game():
    pg.init()
    pg.display.set_caption("Let it Snow!")
    set = Settings() #setting value
    scr = pg.display.set_mode((set.screen_w,set.screen_h))
    maincloud = Cloud(set,scr)
    snowflakes = Group()
    snowmen = Group()
    #gf.create_row(set,scr,maincloud,snowflakes,snowmen)
    man = Snowman(set,scr,maincloud,snowflakes)
    snowmen.add(man)
    while(True):
        gf.check_events(set,scr,maincloud,snowflakes)
        gf.update_flakes(snowflakes,set,scr)
        gf.update_screen(set,scr,maincloud, snowflakes,man)


run_game()
