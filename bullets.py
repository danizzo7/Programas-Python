import pygame
#from pygame.sprite import Sprite
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Uma classe que administra projeteis disparados pela espaconave"""
    def __init__(self, ai_settings, screen, ship):
        """cria um obejeto par o projetil a posicao atual da espaconave"""
        super(Bullet, self).__init__()
        self.screen = screen

        ##cria um retangulo para o projetil em (0,0) e em seguida define a posicao correta
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
                                  ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #armazena a posicao do projetil como um valor decimal
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move o projetil para cima na tela"""

        #atualiza a posicao decimal do projetil
        self.y -= self.speed_factor

        #atualiza a posicao do rect
        self.rect.y = self.y

    def draw_bullet(self):
        """Desenha o projetil na tela"""
        pygame.draw.rect(self.screen, self.color, self.rect)




