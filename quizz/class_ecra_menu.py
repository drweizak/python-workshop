import pygame
import pygame_widgets
from pygame_widgets.button import Button
from .class_cores import Cores as cor


class Menu():
    jogo = None
    butaoGerarPerguntas = None
    butaoJogar = None
    butaoPontuacoes = None
    butaoTerminarSessao = None

    def __init__(self, jogo):
        self.jogo = jogo

        # Obter Centro do ecra
        self.centro_ecra = self.jogo.ecra.get_rect().center

        self.butaoJogar = Button(
            self.jogo.ecra,
            self.centro_ecra[0] - (240 / 2),
            300,
            240,
            75,
            text="Jogar",
            fontSize=40,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=cor().cinzento_cueca,  # Colour of button when not being interacted with
            # Colour of button when being hovered over
            hoverColour=cor().azul_escuro_cueca,
            pressedColour=cor().azul_escuro_cueca,  # Colour of button when being clicked
            onClick=self.navegarJogar  # Function to call when clicked on
        )
        self.butaoGerarPerguntas = Button(
            self.jogo.ecra,
            self.centro_ecra[0] - (240 / 2),
            400,
            240,
            75,
            text="Gerar Perguntas",
            fontSize=40,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=cor().cinzento_cueca,  # Colour of button when not being interacted with
            # Colour of button when being hovered over
            hoverColour=cor().azul_escuro_cueca,
            pressedColour=cor().azul_escuro_cueca,  # Colour of button when being clicked
            onClick=self.navegarPerguntas  # Function to call when clicked on
        )
        self.butaoPontuacoes = Button(
            self.jogo.ecra,
            self.centro_ecra[0] - (240 / 2),
            500,
            240,
            75,
            text="Pontuações",
            fontSize=40,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=cor().cinzento_cueca,  # Colour of button when not being interacted with
            hoverColour=cor().azul_escuro_cueca, # Colour of button when being hovered over
            pressedColour=cor().azul_escuro_cueca,  # Colour of button when being clicked
            onClick=self.navegarPontuacoes  # Function to call when clicked on
        )
        self.butaoTerminarSessao = Button(
            self.jogo.ecra,
            self.centro_ecra[0] - (240 / 2),
            600,
            240,
            75,
            text="Terminar Sessão",
            fontSize=40,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=cor().cinzento_cueca,  # Colour of button when not being interacted with
            hoverColour=cor().azul_escuro_cueca, # Colour of button when being hovered over
            pressedColour=cor().azul_escuro_cueca,  # Colour of button when being clicked
            onClick=self.terminarSessao  # Function to call when clicked on
        )

    def construir(self, jogo):
        self.jogo = jogo

        titulo_fonte = pygame.font.SysFont(
            "arial", 80, bold=True, italic=False)
        menu_fonte = pygame.font.SysFont("arial", 40, bold=True, italic=False)


        # Definir cor de fundo
        self.jogo.ecra.fill(cor().azul_cueca)

        # Definir texto
        textoTitulo = titulo_fonte.render(
            self.jogo.titulo, True, cor().vermelho_cueca)
        textoNomeUtilizador = menu_fonte.render(
            self.jogo.nome_utilizador, True, cor().verde_cueca)


        # Inserir text
        self.jogo.ecra.blit(
            textoTitulo, (textoTitulo.get_rect(center=self.centro_ecra)[0], 150))
        self.jogo.ecra.blit(
            textoNomeUtilizador, (20, 15))

        pygame_widgets.update(self.jogo.eventos)

    def removerWidget(self):
        pygame_widgets.WidgetHandler().getWidgets().remove(self.butaoGerarPerguntas)
        pygame_widgets.WidgetHandler().getWidgets().remove(self.butaoJogar)
        pygame_widgets.WidgetHandler().getWidgets().remove(self.butaoPontuacoes)
        pygame_widgets.WidgetHandler().getWidgets().remove(self.butaoTerminarSessao)

    def navegarJogar(self):
        self.removerWidget()
        self.jogo.estado = self.jogo.ecras["jogar"](self.jogo)
        
    def navegarPerguntas(self):
        self.removerWidget()
        self.jogo.estado = self.jogo.ecras["perguntas"](self.jogo)

    def navegarPontuacoes(self):
        self.removerWidget()
        self.jogo.estado = self.jogo.ecras["pontuacoes"](self.jogo)

    def terminarSessao(self):
        self.removerWidget()
        self.jogo.nome_utilizador = None
        self.jogo.estado = self.jogo.ecras["login"](self.jogo)


