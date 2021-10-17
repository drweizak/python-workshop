import pygame
import pygame_widgets
from quizz.class_ecra_menu import Menu
from quizz.class_ecra_jogar import Jogar
from quizz.class_ecra_login import Login

class Jogo:
    titulo = "Quizz"
    tamanho_ecra = (768, 768)
    estado = None
    eventos = None
    ecra = None
    relogio = None
    ecras = {
        "login": Login,
        "menu": Menu,
        "jogar": Jogar,
        "perguntas": Menu,
        "pontuacoes": Menu,
        "nivelJogo": Menu,
    }
    nome_utilizador = None

    def __init__(self):
        pygame.font.init()
        pygame.display.set_caption(self.titulo)
        self.relogio = pygame.time.Clock()
        self.ecra = pygame.display.set_mode(self.tamanho_ecra)
        self.estado = self.ecras["login"](self)

        self.construir()

    def construir(self):
        # Iniciar ciclo
        while True:
            self.eventos_globais()
            self.estado.construir(self)
            # Atualizar o ecra 60 vezes a cada segundo
            pygame.display.update()
            self.relogio.tick(60)

    def eventos_globais(self):
        self.eventos = pygame.event.get()
        for evento in self.eventos:
            # Se evento for do tipo QUIT
            if evento.type == pygame.QUIT:
                # Fechar janela e sai do jogo
                pygame.quit()
                exit()
                