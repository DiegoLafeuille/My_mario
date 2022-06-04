from os import walk
import pygame as pg

def import_folder(path):
    surf_list = []
    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pg.image.load(full_path).convert_alpha()
            surf_list.append(image_surf)
    return surf_list