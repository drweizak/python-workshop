import pygame_widgets
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
import pygame

class Login() :

    cor_cinzento_cueca = (246, 246, 246)
    cor_azul_cueca = (153, 204, 255)
    cor_azul_escuro_cueca = (184, 196, 209)
    cor_vermelho_cueca = (203, 66, 84)
    cor_laranja_cueca = (205, 131, 67)
    preto_cueca = (0, 0, 0)
    branco_cueca = (255, 255, 255)

    jogo = None
    caixaTexto = None
    butao = None
    mensagem_erro = None

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

        self.butao = Button(
            self.jogo.ecra,
            self.centro_ecra[0] - (240 / 2),
            430,
            240,
            75,
            text="Iniciar",
            fontSize=40,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=self.cor_cinzento_cueca,  # Colour of button when not being interacted with
            # Colour of button when being hovered over
            hoverColour=self.cor_azul_escuro_cueca,
            pressedColour=self.cor_azul_escuro_cueca,  # Colour of button when being clicked
            onClick=self.output # Function to call when clicked on)
        )

    def output(self):
        if len(self.caixaTexto.getText())>2:
            self.jogo.nome_utilizador = self.caixaTexto.getText()
            pygame_widgets.WidgetHandler().getWidgets().remove(self.caixaTexto)
            pygame_widgets.WidgetHandler().getWidgets().remove(self.butao)
            self.jogo.estado = self.jogo.ecras["menu"](self.jogo)
        else:
            self.mensagem_erro = "Nome inválido: deve ter mais de 2 caracteres."

    def construir(self, jogo):
        self.jogo = jogo

        self.jogo.ecra.fill(self.cor_azul_cueca)

        titulo_fonte = pygame.font.SysFont("arial", 48, bold=True, italic=False)
        mensagemErro_fonte = pygame.font.SysFont("arial", 30, bold=False, italic=False)

        textoTitulo = titulo_fonte.render("Insira aqui o seu nome", 
            True, self.cor_vermelho_cueca)
        self.jogo.ecra.blit(
            textoTitulo, (textoTitulo.get_rect(center=self.centro_ecra)[0], 180))
            
        if self.mensagem_erro:
            textoMensagemErro = mensagemErro_fonte.render(self.mensagem_erro, 
                True, self.cor_laranja_cueca)
            self.jogo.ecra.blit(
                textoMensagemErro, (textoMensagemErro.get_rect(center=self.centro_ecra)[0], 385))
 
        pygame_widgets.update(self.jogo.eventos)