class settings():
    #esta e uma classe para atmazenar todas as conficurações da invasão alienigena

    def __init__(self):
        #inicializa as configurações do jogo)

        # Configurações da tela
        self.screen_width =900
        self.screen_height=600
        self.bg_color = (230,230,230)

        #configurações da espaçponave

        #self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #configuracoes dos projeteis
        #self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        #configurações dos alienigenas
        #   self.alien_speed_factor = 1
        self.fleet_drop_speed = 10

        #fleet direction = 1 representa a direita e = -1 representa a esquerda
        #self.fleet_direction = 1

        # A taxa com que a velocidade do jogo aumenta
        self.speedup_scale = 1.1

        # A taxa com que os pontos para cada alienigena aumentam
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Inicaliza as configuraçaões que mudam no decorrer do jogo"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        #Pontuação
        self.alien_points = 50

        # fleet direction = 1 representa a direita e = -1 representa a esquerda
        self.fleet_direction = 1

    def increase_speed(self):
        """ Aumenta as configurações de velocidade"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)