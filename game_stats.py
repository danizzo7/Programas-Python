class GameStats():
    """Armaena dados estatísticos da Invasão Alienigena"""

    def __init__(self, ai_settings):
        """Inicializa os dados estatísticos"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

        # A pontuação máxima jamais deverá ser reiniciada

        self.high_score = 0

    def reset_stats(self):
#       """Inicialia os dados estatisticos que podem mudar durante o jogo"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
