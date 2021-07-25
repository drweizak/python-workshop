# Quizz
# Uma pergunta com várias opções onde normalmente apenas 1 é verdadeira
# -- O que pode ser melhorado:
# Inserir Perguntas
# Menu Principal Jogo / GUI
# Separar em mais funcoes
# criar base de dados
# Modos de jogo (Single Player, Multi-jogador)

import time
import random

class questao:
    def __init__(self, titulo, respostas, verifica):
        self.titulo = titulo
        self.respostas = respostas
        self.verifica = verifica

def imprimirRespostas(respostas):
    random.shuffle(respostas)

    for i in range(len(respostas)):
        opcao = respostas[i]
        print(str(i+1) + ". " + opcao)

def lerResposta():
    resposta = ''
    respostaValida = False
    
    while respostaValida == False:
        resposta = input("Introduz a tua resposta: ")
        
        range_1 = ["1", "2", "3", "4", "5"] 
        if resposta in range_1 :
            respostaValida = True
        else :
            print(resposta, ' Resposta invalida, tente outra vez!')
            print("\n")

    return resposta

def validarResposta(pergunta, resposta):
    global pontuacao, respostas_corretas
    
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
        pontuacao += 1
        respostas_corretas += 1

        print("Correcta")
    else:
        print("Errada")

def fazerPergunta (pergunta):
    print(pergunta.titulo)
    print("\n")

    imprimirRespostas(pergunta.respostas)
    print("\n")

    resposta = lerResposta()
    print("\n")

    validarResposta(pergunta, resposta)

def gerarPerguntas():
    pergunta1 = questao("Qual das palavras não pertence à família da Arvore?", ["Computador", "Folha", "Tronco", "Ramos", "Raiz"], "Computador")
    pergunta2 = questao("Em que anos se deu a união dinástica ibérica?", ["1780-1820", "1580-1640", "1290-1311", "1555-1580", "1467-1509"], "1580-1640")
    pergunta3 = questao("Em que ano sucedeu o atentado terrorista de 11 de Setembro?", ["2021", "1876", "2002", "3001", "2001"], "2001")
    pergunta4 = questao("Quando é que o tiranossauro Rex extinguiu-se?", ["1990", "66,000,000 AC", "2021", "20,000,000 AC", "10,000 AC"], "66,000,000 AC")
    pergunta5 = questao("Qual é a escala que mede a intensidade de um sismo?",["Richter", "Mercalli Modificada", "Magnitude local", "Magnitude de momento", "Terramoto"], "Mercalli Modificada")
    pergunta6 = questao("Qual é o nome que se dá ao ponto de não retorno de um buraco-negro?",["Disco de Acreção", "Horizonte de Eventos", "Infinito", "Heliosfera", "Galáxia"], "Horizonte de Eventos")
    pergunta7 = questao("Qual o livro mais vendido no mundo a seguir à Bíblia?", ["Senhor dos Anéis", "Dom Quixote", "O Pequeno Príncipe", "Ela a Feiticeira", "Um conto de duas cidades"], "Dom Quixote")
    pergunta8 = questao("Qual destes países não é na Europa?",["Portugal","Finlandia","Alemanha","Burkina Faso", "Suiça"], "Burkina Faso")
    pergunta9 = questao("Qual foi o primeiro jogo publicado pela Titan Forged Games", ["League of Legends", "Slinki", "SMITE", "Out of Line", "Ugo Volt"], "Slinki") 
    pergunta10 = questao("Qual é o código do multibanco da Verónica?", ["6743", "0000", "5643", "2021", "XXXX"], "XXXX")
    pergunta11 = questao("Qual é unidade de temperatura de acordo com o SI (Sistema Internacional)?", ["Kelvin", "Celsius", "Centigrados", "Fahrenheit", "Kevin"], "Kelvin")

    perguntas = [pergunta1,pergunta2,pergunta3,pergunta4,pergunta5,pergunta6,pergunta7,pergunta8,pergunta9,pergunta10, pergunta11]

    random.shuffle(perguntas)

    return perguntas[:total_perguntas]

def avaliarPontuacao():
    percentagem = (pontuacao / total_perguntas) * 100

    if(percentagem < 20):
        print(nome_utilizador, ', Oh meu Deus!')
    elif(percentagem < 50):
        print(nome_utilizador, ', Tenta mais uma vez e talvez consigas atingir um patamar aceitavel!')
    elif(percentagem < 75):
        print(nome_utilizador, ', Nao e mau! Mas consegues melhor.')
    elif(percentagem < 90):
        print(nome_utilizador, ', E pah! Temos genio, mas sera que consegues aquele bocadinho "assim"?')
    else:
        print(nome_utilizador, ', Brutal, acertaste em tudo. Se es assim tao bom nisto, porque nao nos ajudas a programar este Quiz?')

def iniciarQuiz():
    global nome_utilizador
    nome_utilizador = input("Introduza o seu nome: ")
    print("\n")

    for pergunta in perguntas:
        fazerPergunta(pergunta)

        print("\n")
        time.sleep(1)

    print('Acertaste em ' + str(respostas_corretas) + ' perguntas num total de ' + str(total_perguntas) + '.')
    print("\n")

    avaliarPontuacao()
    print("\n")

    print("Quizz concluido!")

total_perguntas = 4
respostas_corretas = 0
pontuacao = 0
perguntas = gerarPerguntas()
nome_utilizador = ''

iniciarQuiz()