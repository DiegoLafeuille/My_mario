import pygame
from game_data import levels

class Node(pygame.sprite.Sprite):
    def __init__(self, pos, status):
        super().__init__()
        self.image = pygame.Surface((100,80))
        if status == 'available': self.image.fill('red')
        else: self.image.fill('grey')
        self.rect = self.image.get_rect(center = pos)

class PlayerIcon(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((20,20))
        self.image.fill('blue')
        self.rect = self.image.get_rect(center = pos)

class Overworld:
    def __init__(self, start_level, max_level, surface):

        # Setup
        self.display_surface = surface
        self.max_level = max_level
        self.current_level = start_level

        # Sprites
        self.setup_nodes()
        self.setup_icon()
    
    def setup_nodes(self):
        self.nodes = pygame.sprite.Group()
        for index, node_data in enumerate(levels):
            if index <= self.max_level:
                node_sprite = Node(node_data['node_pos'], 'available')
            else:
                node_sprite = Node(node_data['node_pos'], 'locked')
            self.nodes.add(node_sprite)

    def setup_icon(self):
        self.icon = pygame.sprite.GroupSingle()
        icon_sprite = PlayerIcon(levels[self.current_level]['node_pos'])
        self.icon.add(icon_sprite)

    def draw_paths(self):
        points = [node['node_pos'] for index,node in enumerate(levels) if index<=self.max_level]
        pygame.draw.lines(self.display_surface, 'red', False, points, 6)

    def run(self):
        self.draw_paths()
        self.nodes.draw(self.display_surface)
        self.icon.draw(self.display_surface)