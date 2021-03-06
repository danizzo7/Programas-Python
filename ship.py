import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        """inicializa a espçonave e define a posicao iniial"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #carrega a imagem da espacçonave e obtem o seu rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #inicia cada nova espaconave em sua posicao atual
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom  = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Atualiza a posicao da espaconave de acordo com a flag de movimento"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            #self.rect.centerx += self.ai_set.tings.ship_speed_factor
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
             #self.rect.centerx -= self.ai_settings.ship_speed_factor
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """Desenha a espaconave em sua posicao atual"""
        self.screen.blit (self.image,self.rect)

    def center_ship(self):
        """     Centrazia a espaçonave na tela"""
        self.center = self.screen_rect.centerx