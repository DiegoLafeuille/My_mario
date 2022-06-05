from random import randint, choice
import pygame as pg
from settings import vertical_tile_number, tile_size, screen_width
from tiles import AnimatedTile, StaticTile
from support import import_folder

class Sky:
    def __init__(self, horizon):
        self.top = pg.image.load('../graphics/decoration/sky/sky_top.png').convert()
        self.bottom = pg.image.load('../graphics/decoration/sky/sky_bottom.png').convert()
        self.middle = pg.image.load('../graphics/decoration/sky/sky_middle.png').convert()
        self.horizon = horizon

        # Strecth
        self.top = pg.transform.scale(self.top, (screen_width, tile_size))
        self.bottom = pg.transform.scale(self.bottom, (screen_width, tile_size))
        self.middle = pg.transform.scale(self.middle, (screen_width, tile_size))

    def draw(self,surface):
        for row in range(vertical_tile_number):
            y = row * tile_size
            if row < self.horizon:
                surface.blit(self.top, (0,y))
            elif row == self.horizon:
                surface.blit(self.middle, (0,y))
            else:
                surface.blit(self.bottom, (0,y))

class Water:
    def __init__(self,top,level_width):
        water_start = -screen_width
        water_tile_width = 192
        tile_x_amount = int((level_width + 2*screen_width) / water_tile_width)
        self.water_sprites = pg.sprite.Group()

        for tile in range (tile_x_amount):
            x = water_start + tile * water_tile_width
            y = top
            sprite = AnimatedTile(water_tile_width, x, y, '../graphics/decoration/water')
            self.water_sprites.add(sprite)
    
    def draw(self,surface,shift):
        self.water_sprites.update(shift)
        self.water_sprites.draw(surface)

class Clouds:
    def __init__(self, horizon, level_width, cloud_number):
        cloud_surf_list = import_folder('../graphics/decoration/clouds')
        min_x = - screen_width
        max_x = level_width + screen_width
        min_y = 0
        max_y = horizon
        self.cloud_sprites = pg.sprite.Group()

        for cloud in range(cloud_number):
            cloud = choice(cloud_surf_list)
            x = randint(min_x, max_x)
            y = randint(min_y, max_y)
            sprite = StaticTile(0, x, y, cloud)
            self.cloud_sprites.add(sprite)

    def draw(self, surface, shift):
        self.cloud_sprites.update(shift)
        self.cloud_sprites.draw(surface)