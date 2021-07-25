# Quizz
# Uma pergunta com várias opções onde normalmente apenas 1 é verdadeira
# -- O que pode ser melhorado?
# Inserir Perguntas
# Validação
# Pontuação / score
# Avaliação / Pauta com Nome utilizador
# Menu Principal Jogo / GUI
# Separar em mais funcoes

# Notas de rodapé: Em Dinamarquês e Alemão "Moi" = Olá (em suomi perkele, carago!)

import sys
import time
import random

class questao:
    def __init__(self, titulo, respostas, verifica):
        self.titulo = titulo
        self.respostas = respostas
        self.verifica = verifica

pergunta1 = questao("Qual das palavras não pertence à família da Arvore?", ["Computador", "Folha", "Tronco", "Ramos", "Raiz"], "Computador")
pergunta2 = questao("Em que anos se deu a união dinástica ibérica?", ["1780-1820", "1580-1640", "1290-1311", "1555-1580", "1467-1509"], "1580-1640")
pergunta3 = questao("Em que ano sucedeu o atentado terrorista de 11 de Setembro?", ["2021", "1876", "2002", "3001", "2001"], "2001")
pergunta4 = questao("Quando é que o tiranossauro Rex extinguiu-se?", ["1990", "66,000,000 AC", "2021", "20,000,000 AC", "10,000 AC"], "66,000,000 AC")

# Faz random às perguntas :)

perguntas = [pergunta1,pergunta2,pergunta3,pergunta4]
random.shuffle(perguntas)
# print(perguntas[0].titulo, perguntas[1].titulo, perguntas[2].titulo)
# sys.exit()

def fazerPergunta (pergunta):
    print(pergunta.titulo)
    random.shuffle(pergunta.respostas)

    for i in range(len(pergunta.respostas)):
        opcao = pergunta.respostas[i]
        print(str(i+1) + ". " + opcao)
        
    
    resposta = input("Resposta: ")
    print("A tua resposta está")
    
    # suspense
    time.sleep(0.5) # delay de 2 seg.
    print(".")
    time.sleep(0.5) # delay de 2 seg.
    print(".")
    time.sleep(0.5) # delay de 2 seg.
    print(".")
    time.sleep(0.5) # delay de 2 seg.

    posicaoIndex = int(resposta)-1
    texto = pergunta.respostas[posicaoIndex]   

    if texto == pergunta.verifica:
        print("Correcta")
    else:
        print("Errada")

for pergunta in perguntas:
    fazerPergunta(pergunta)
    print("\n")
    time.sleep(1) # delay de 1 seg.

print("Quizz concluido")