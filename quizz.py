# Quizz
# Uma pergunta com várias opções onde normalmente apenas 1 é verdadeira
# -- O que pode ser melhorado?
# Inserir Perguntas
# Validação
# Perguntas  / Respostas aleatórias (Dicionario)
# Pontuação / score
# Nome utilizador, data
# Menu Principal Jogo
# Separar em mais funcoes

# Tipo Text: 	    str
# Tipo Numerico: 	int, float, complex
# Tipo Sequencial: 	list, tuple, range
# Tipo Mapa: 	    dict
# Tipo Conjunto: 	set, frozenset
# Tipo Boleano: 	bool
# Tipo Binario: 	bytes, bytearray, memoryview

# lista = ["Ola",2, None] # lista com ordem indexada 1, 2, 3...
# dicionario = { "chave":"valor", 1:"valor", 2: None } # dicionario com "keys" (chave)
# tuplo = (1,2,3,"ada") # tuplo ordenado/indexado e não se pode alterar o valor

import sys
import time

pergunta1 = ["Qual das palavras não pertence à família da Arvore?", ["Computador", "Folha", "Tronco", "Ramos", "Raiz"], 0 ]
pergunta2 = ["Em que anos se deu a união dinástica?", ["1780-1820", "1580-1640", "1290-1311", "1555-1580", "1467-1509"], 1 ]

perguntas = [pergunta1,pergunta2]

def fazerPergunta (pergunta):
    print(pergunta[0])
    # loop 1
    # 3 plicas comenta em bloco
    ''' 
    x = 1
    for i in pergunta[1]:
        print(str(x) + ". " + i)
        x += 1

    '''
    # loop 2
    opcoes = pergunta[1]

    for i in range(len(pergunta[1])):
        opcao = pergunta[1][i]
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

    if int(resposta)-1 == pergunta[2]:
        print("Correcta")
    else:
        print("Errada")

for pergunta in perguntas:
    fazerPergunta(pergunta)
    print("\n")
    time.sleep(1) # delay de 1 seg.

print("Quizz concluido")