import pygame
import pygame_widgets
from pygame_widgets.button import Button


class Menu():

    jogo = None

    def __init__(self, jogo):
        self.jogo = jogo

        self.construir()

    def construir(self):
        # Definir variaveis
        cor_cinzento_cueca = (246, 246, 246)
        cor_azul_cueca = (153, 204, 255)
        cor_azul_escuro_cueca = (184, 196, 209)
        cor_vermelho_cueca = (203, 66, 84)
        preto_cueca = (0, 0, 0)

        titulo_fonte = pygame.font.SysFont(
            "arial", 80, bold=True, italic=False)
        menu_fonte = pygame.font.SysFont("arial", 40, bold=True, italic=False)

        # Definir cor de fundo
        self.jogo.ecra.fill(cor_azul_cueca)

        # Definir texto
        textoTitulo = titulo_fonte.render(
            self.jogo.titulo, True, cor_vermelho_cueca)
        textoButaoJogar = menu_fonte.render("Jogar", True, preto_cueca)
        textoButaoPerguntas = menu_fonte.render(
            "Adicionar perguntas", True, preto_cueca)
        textoButaoPontuacoes = menu_fonte.render(
            "Pontuações", True, preto_cueca)

        # Obter Centro do ecra
        centro_ecra = self.jogo.ecra.get_rect().center

        # Inserir text
        self.jogo.ecra.blit(
            textoTitulo, (textoTitulo.get_rect(center=centro_ecra)[0], 150))
        
        Button(
            self.jogo.ecra,
            centro_ecra[0] - (240 / 2),
            300,
            240,
            75,
            text="Jogar",
            fontSize=40,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=cor_cinzento_cueca,  # Colour of button when not being interacted with
            # Colour of button when being hovered over
            hoverColour=cor_azul_escuro_cueca,
            pressedColour=cor_azul_escuro_cueca,  # Colour of button when being clicked
            onClick=self.navegarJogar  # Function to call when clicked on)
        )
        Button(
            self.jogo.ecra,
            centro_ecra[0] - (240 / 2),
            400,
            240,
            75,
            text="Gerar Perguntas",
            fontSize=40,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=cor_cinzento_cueca,  # Colour of button when not being interacted with
            # Colour of button when being hovered over
            hoverColour=cor_azul_escuro_cueca,
            pressedColour=cor_azul_escuro_cueca,  # Colour of button when being clicked
            onClick=self.navegarPerguntas  # Function to call when clicked on)
        )
        Button(
            self.jogo.ecra,
            centro_ecra[0] - (240 / 2),
            500,
            240,
            75,
            text="Pontuações",
            fontSize=40,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=cor_cinzento_cueca,  # Colour of button when not being interacted with
            hoverColour=cor_azul_escuro_cueca, # Colour of button when being hovered over
            pressedColour=cor_azul_escuro_cueca,  # Colour of button when being clicked
            onClick=self.navegarPontuacoes  # Function to call when clicked on)
        )
        pygame_widgets.update(self.jogo.eventos)

    def navegarJogar(self):
        self.jogo.estado = self.jogo.ecras["jogar"]

    def navegarPerguntas(self):
        self.jogo.estado = self.jogo.ecras["perguntas"]

    def navegarPontuacoes(self):
        self.jogo.estado = self.jogo.ecras["pontuacoes"]


