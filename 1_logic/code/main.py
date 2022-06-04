import pygame as pg, sys
from settings import * 
from tiles import Tile
from level import Level

# Pygame setup
pg.init()
screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()
level = Level(level_map, screen)

while True:

    # Event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill('black')
    level.run()

    pg.display.update()
    clock.tick(60)