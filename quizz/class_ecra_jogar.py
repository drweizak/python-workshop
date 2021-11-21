import random
import pygame
import pygame_widgets
from pygame_widgets.button import Button
from .quizz import gerarPerguntas
from .class_cores import Cores as cor
from .components.textWrap import wrapline

class Jogar():

    jogo = None
    total_perguntas = 20
    respostas_corretas = 0
    pontuacao = 0
    perguntas = []
    posicao_pergunta = 0
    initial_render = True
    botoes = []
    mensagem = ''
    validar_resposta = False

    def __init__(self, jogo):
        self.jogo = jogo
        
    def construir(self, jogo):
        self.jogo = jogo
        self.jogo.ecra.fill(cor().azul_cueca)
        #gerar texto: tipo Fonte, Cor e Posicao
        menu_fonte = pygame.font.SysFont("arial", 24, bold=True, italic=False)
        textoNomeUtilizador = menu_fonte.render(
            self.jogo.nome_utilizador, True, cor().verde_cueca)
        self.jogo.ecra.blit(
            textoNomeUtilizador, (20, 15))
            
        textoPontuacao = menu_fonte.render(
            str(self.pontuacao), True, cor().laranja_cueca)
        self.jogo.ecra.blit(
            textoPontuacao, (textoNomeUtilizador.get_width() + 80, 15))
        
        if self.initial_render:
            self.perguntas = gerarPerguntas(self.total_perguntas)
            for i in range(len(self.perguntas)):
                random.shuffle(self.perguntas[i]["opcoes"])
            self.initial_render = False
            #Mudar para True quando volta ao menu!!!!

        #contador de perguntas / Progresso
        y_pos = self.fazerPergunta(self.perguntas[self.posicao_pergunta])
        # Render da mensagem
        mensagem_fonte = pygame.font.SysFont("arial", 24, bold=True, italic=False)
        textoMensagem = mensagem_fonte.render(
            self.mensagem, True, cor().verde_cueca)
        self.jogo.ecra.blit(
            textoMensagem, (textoMensagem.get_rect(center=self.jogo.centro_ecra)[0], y_pos))
        
        pygame_widgets.update(self.jogo.eventos)

        if self.validar_resposta == True:
            self.validar_resposta = False
            # Esperar
            pygame.time.delay(2000)
            # Limpar a mensagem
            self.mensagem = ''
            self.posicao_pergunta = self.posicao_pergunta + 1
        
    
    def fazerPergunta(self, pergunta):
        pergunta_fonte = pygame.font.SysFont("arial", 32, bold=True, italic=False)

        questao = wrapline(pergunta["questao"], pergunta_fonte, 600)
        y_pos=130
        
        for linha in questao:
            textoPergunta = pergunta_fonte.render(linha, 
                True, cor().vermelho_cueca)
            self.jogo.ecra.blit(
                textoPergunta, (textoPergunta.get_rect(center=self.jogo.centro_ecra)[0], y_pos))
            y_pos += 38

        y_pos = self.imprimirOpcoes(pergunta["opcoes"], y_pos)
        return y_pos

    def imprimirOpcoes(self, respostas, y_pos):
        
        pergunta_fonte = pygame.font.SysFont("arial", 28, bold=True, italic=False)
        y_pos += 60
        for i in range(len(respostas)):
            opcao = respostas[i]            

            butt = Button(
                    self.jogo.ecra,
                    84,
                    y_pos,
                    100,
                    50,
                    text=chr(i+65),
                    fontSize=40,  # Size of font
                    margin=20,  # Minimum distance between text/image and edge of button
                    inactiveColour=cor().cinzento_cueca,  # Colour of button when not being interacted with
                    # Colour of button when being hovered over
                    hoverColour=cor().azul_escuro_cueca,
                    pressedColour=cor().azul_escuro_cueca,  # Colour of button when being clicked
                    onClickParams=(self.perguntas[self.posicao_pergunta], opcao),
                    onClick=self.validarResposta, # Function to call when clicked on)
                )
            
            self.botoes.append(butt)

            textoOpcao = pergunta_fonte.render(opcao, 
                True, cor().preto_cueca)
            self.jogo.ecra.blit(
                textoOpcao, (84+100+20, y_pos + 11))
            y_pos += 75
        return y_pos
    
    def validarResposta(self, pergunta, resposta):
        for botao in self.botoes:
            pygame_widgets.WidgetHandler().getWidgets().remove(botao)
        self.botoes.clear()

        if resposta == pergunta["respostaCerta"]:
            self.pontuacao += 1
            self.respostas_corretas += 1
            
            # Associar mensagem a uma variavel
            self.mensagem = "Resposta correcta"
        else:
            # Associar mensagem a uma variavel
            self.mensagem = "Resposta errada"
        
        self.validar_resposta = True

        

