import pygame
import pygame_widgets
from pygame_widgets.button import Button
from .class_cores import Cores as cor

class Menu():
    jogo = None
    botaoGerarPerguntas = None
    botaoJogar = None
    botaoPontuacoes = None
    botaoTerminarSessao = None

    def __init__(self, jogo):
        self.jogo = jogo
        
        # # Starting the mixer
        # pygame.mixer.init()
        
        # # Loading the song
        # pygame.mixer.music.load("quizz/audios/commerical-break.mp3")
        
        # # Setting the volume
        # pygame.mixer.music.set_volume(0.7)
        
        # # Start playing the song
        # pygame.mixer.music.play()

        # # mixer.music.pause() 
        
        self.botaoJogar = Button(
            self.jogo.ecra,
            self.jogo.centro_ecra[0] - (260 / 2),
            250,
            260,
            75,
            text="Jogar",
            fontSize=40,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=cor().cinzento_cueca,  # Colour of button when not being interacted with
            # Colour of button when being hovered over
            hoverColour=cor().cinzento_escuro_cueca,
            pressedColour=cor().cinzento_escuro_cueca,  # Colour of button when being clicked
            onClick=self.navegarJogar  # Function to call when clicked on
        )
        self.botaoGerarPerguntas = Button(
            self.jogo.ecra,
            self.jogo.centro_ecra[0] - (260 / 2),
            350,
            260,
            75,
            text="Gerar Perguntas",
            fontSize=40,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=cor().cinzento_cueca,  # Colour of button when not being interacted with
            # Colour of button when being hovered over
            hoverColour=cor().cinzento_escuro_cueca,
            pressedColour=cor().cinzento_escuro_cueca,  # Colour of button when being clicked
            onClick=self.navegarPerguntas  # Function to call when clicked on
        )
        self.botaoPontuacoes = Button(
            self.jogo.ecra,
            self.jogo.centro_ecra[0] - (260 / 2),
            450,
            260,
            75,
            text="Pontuações",
            fontSize=40,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=cor().cinzento_cueca,  # Colour of button when not being interacted with
            hoverColour=cor().cinzento_escuro_cueca, # Colour of button when being hovered over
            pressedColour=cor().cinzento_escuro_cueca,  # Colour of button when being clicked
            onClick=self.navegarPontuacoes  # Function to call when clicked on
        )
        self.botaoTerminarSessao = Button(
            self.jogo.ecra,
            self.jogo.centro_ecra[0] - (260 / 2),
            550,
            260,
            75,
            text="Mudar Utilizador",
            fontSize=40,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=cor().cinzento_cueca,  # Colour of button when not being interacted with
            hoverColour=cor().cinzento_escuro_cueca, # Colour of button when being hovered over
            pressedColour=cor().cinzento_escuro_cueca,  # Colour of button when being clicked
            onClick=self.terminarSessao  # Function to call when clicked on
        )

        self.botaoTerminarJogo = Button(
            self.jogo.ecra,
            self.jogo.centro_ecra[0] - (260 / 2),
            650,
            260,
            75,
            text="Sair do Jogo",
            fontSize=40,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=cor().cinzento_cueca,  # Colour of button when not being interacted with
            hoverColour=cor().cinzento_escuro_cueca, # Colour of button when being hovered over
            pressedColour=cor().cinzento_escuro_cueca,  # Colour of button when being clicked
            onClick=self.terminarJogo  # Function to call when clicked on
        )
        
    def construir(self, jogo):
        self.jogo = jogo

        titulo_fonte = pygame.font.SysFont(
            "arial", 80, bold=True, italic=False)
        menu_fonte = pygame.font.SysFont("arial", 24, bold=True, italic=False)


        # Definir cor de fundo
        self.jogo.ecra.fill(cor().azul_cueca)

        # Definir texto
        textoTitulo = titulo_fonte.render(
            self.jogo.titulo, True, cor().vermelho_cueca)
        textoNomeUtilizador = menu_fonte.render(
            self.jogo.nome_utilizador, True, cor().verde_cueca)


        # Inserir text
        self.jogo.ecra.blit(
            textoTitulo, (textoTitulo.get_rect(center=self.jogo.centro_ecra)[0], 100))
        self.jogo.ecra.blit(
            textoNomeUtilizador, (20, 15))

        pygame_widgets.update(self.jogo.eventos)

    def removerWidget(self):
        pygame_widgets.WidgetHandler().getWidgets().remove(self.botaoGerarPerguntas)
        pygame_widgets.WidgetHandler().getWidgets().remove(self.botaoJogar)
        pygame_widgets.WidgetHandler().getWidgets().remove(self.botaoPontuacoes)
        pygame_widgets.WidgetHandler().getWidgets().remove(self.botaoTerminarSessao)
        pygame_widgets.WidgetHandler().getWidgets().remove(self.botaoTerminarJogo)

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

    def terminarJogo(self):
        self.removerWidget()
        pygame.quit()
        exit()
