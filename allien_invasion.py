import sys
import pygame
from settings import settings
from ship import Ship
from allien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scorebord

def run_game():
    #inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) #cria a janela do pygame em pixels
    pygame.display.set_caption("Allien Invasion")

    # Cria o botao  play
    play_button = Button(ai_settings, screen, "Play")

    #Cria uma instancia para armazenar dados estatisticos do jogo e cria painel de pontuacao
    stats = GameStats(ai_settings)
    sb = Scorebord(ai_settings, screen, stats)

    #cria uma espaconave, um grupo de projeteis e um grupo de alienigenaas
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    #inicia o laço principal do jogo e vai ficar rodando aqui em loop infinito ate evento que pare
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)



run_game()




