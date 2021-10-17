import pygame
from .quizz import gerarPerguntas

class Jogar():

    jogo = None
    total_perguntas = 5
    respostas_corretas = 0
    pontuacao = 0
    perguntas = []
    posicao_pergunta = 0
    initial_render = True

    def __init__(self, jogo):
        self.jogo = jogo
        
        # Definir cores
        self.cor_cinzento_cueca = (246, 246, 246)
        self.cor_azul_cueca = (153, 204, 255)
        self.cor_azul_escuro_cueca = (184, 196, 209)
        self.cor_vermelho_cueca = (203, 66, 84)
        self.cor_verde_cueca = (69, 132, 69)
        self.preto_cueca = (0, 0, 0)
        

    def construir(self, jogo):
        self.jogo = jogo

        if self.initial_render:
            self.perguntas = gerarPerguntas(self.total_perguntas)
            self.initial_render = False
            print(self.perguntas)
            #Mudar para True quando volta ao menu!!!!
        
        self.fazerPergunta(self.perguntas[self.posicao_pergunta])
        self.jogo.ecra.fill(self.cor_azul_cueca)
    
    def fazerPergunta(self, pergunta):
        pass 
