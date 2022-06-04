import pygame as pg
import sys
from settings import *
from level import Level
from game_data import level_0

# Pygame setup
pg.init()
screen = pg.display.set_mode((screen_width,screen_height))
clock = pg.time.Clock()
level = Level(level_0, screen)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
    screen.fill('black')
    level.run()

    pg.display.update()
    clock.tick(60)

