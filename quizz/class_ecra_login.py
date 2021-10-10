import pygame_widgets
from pygame_widgets.textbox import TextBox
import pygame

class Login() :

    cor_cinzento_cueca = (246, 246, 246)
    cor_azul_cueca = (153, 204, 255)
    cor_azul_escuro_cueca = (184, 196, 209)
    cor_vermelho_cueca = (203, 66, 84)
    preto_cueca = (0, 0, 0)
    branco_cueca = (255, 255, 255)

    jogo = None
    caixaTexto = None

    def __init__(self, jogo):
        self.jogo = jogo

        self.centro_ecra = self.jogo.ecra.get_rect().center

        self.caixaTexto = TextBox(
            self.jogo.ecra,
            self.centro_ecra[0] - (550/2),
            300,
            550,
            80, 
            fontSize=50,
            colour=self.branco_cueca,
            borderColour=self.cor_vermelho_cueca,
            textColour=self.preto_cueca,
            onSubmit=self.output,
            radius=10, 
            borderThickness=5,
        )

    def output(self):
        self.jogo.nome_utilizador = self.caixaTexto.getText()
        pygame_widgets.WidgetHandler().getWidgets().remove(self.caixaTexto)
        self.jogo.estado = self.jogo.ecras["menu"](self.jogo)

    def construir(self, jogo):
        self.jogo = jogo

        self.jogo.ecra.fill(self.cor_azul_cueca)

        titulo_fonte = pygame.font.SysFont("arial", 48, bold=True, italic=False)
        textoTitulo = titulo_fonte.render("Insira aqui o seu nome", 
            True, self.cor_vermelho_cueca)

        self.jogo.ecra.blit(
            textoTitulo, (textoTitulo.get_rect(center=self.centro_ecra)[0], 180))
        pygame_widgets.update(self.jogo.eventos)
