from cmath import rect
import pygame

class UI:
    def __init__(self, surface):
        
        # Setup
        self.display_surface = surface

        # Health
        self.health_bar = pygame.image.load('../graphics/ui/health_bar.png').convert_alpha()
        self.health_bar_topleft = (54,39)

        # Coins
        self.coin = pygame.image.load('../graphics/ui/coin.png').convert_alpha()
        self.coin_rect = self.coin.get_rect(topleft = (50,61))
        self.font = pygame.font.Font('../graphics/ui/ARCADEPI.ttf', 30)

    def show_health(self,current,full):
        self.display_surface.blit(self.health_bar,(20,10))

    def show_coins(self,amount):
        self.display_surface.blit(self.coin, self.coin_rect)
        coin_amount_surf = self.font.render(str(amount), False, 'black')
        coin_amount_rect = coin_amount_surf.get_rect(midleft = (self.coin_rect.right + 4, self.coin_rect.centery))
        self.display_surface.blit(coin_amount_surf, coin_amount_rect)
       
