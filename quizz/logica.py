# Quizz
# Uma pergunta com várias opções onde normalmente apenas 1 é verdadeira
# -- O que pode ser melhorado:
# Menu Principal Jogo / GUI
# Modos de jogo (Single Player, Multi-jogador)
# estatisticas e graficos de pontuaçao
# Inserir opção de confirmar/editar na funcao inserirPergunta
# Inserir funcao inserirPergunta nos menus de jogo

import time
import random
import json
from datetime import datetime

def login():
    global nome_utilizador 
    
    print("QUIZZ TIME!!")
    print("Para iniciar o jogo, por favor, ")
    
    nomeValido = False
    
    while nomeValido == False:
        nome_utilizador = input("introduza o seu nome: ")
        
        if len(nome_utilizador) > 1 :
            nomeValido = True
        else :
            print('Este nome ', nome_utilizador, ' é inválido! Deve conter no mínimo dois caracteres!')
            print("\n")


    print("Bem-vind@ ", nome_utilizador, " ao mais fantástico quizz à face da terra e, quiçá, do universo!")
    print("Jogo")
    print("Regras")
    print("Pontuações")
    #input("escreva a opção desejada")

def imprimirOpcoes(respostas):
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
            print(resposta, ' Resposta inválida, tente outra vez!')
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
    texto = pergunta["opcoes"][posicaoIndex]   

    if texto == pergunta["respostaCerta"]:
        pontuacao += 1
        respostas_corretas += 1

        print("Correcta")
    else:
        print("Errada")

def fazerPergunta (pergunta):
    print(pergunta["questao"])
    print("\n")

    imprimirOpcoes(pergunta["opcoes"])
    print("\n")

    resposta = lerResposta()
    print("\n")

    validarResposta(pergunta, resposta)

def gerarPerguntas():
    
    # Ler Json
    with open("perguntas.json", "r") as ficheiro:
        perguntas = json.loads(ficheiro.read())

    random.shuffle(perguntas)

    return perguntas[:total_perguntas]

def avaliarPontuacao():
    percentagem = (pontuacao / total_perguntas) * 100

    if(percentagem < 20):
        print(nome_utilizador, ', oh meu Deus!')
    elif(percentagem < 50):
        print(nome_utilizador, ', tenta mais uma vez e talvez consigas atingir um patamar aceitável!')
    elif(percentagem < 75):
        print(nome_utilizador, ', não é mau! Mas consegues melhor.')
    elif(percentagem < 90):
        print(nome_utilizador, ', é pah! Temos génio, mas será que consegues aquele bocadinho "assim"?')
    else:
        print(nome_utilizador, ', brutal, acertaste em tudo. Se és assim tão bom/boa nisto, porque não nos ajudas a programar este Quiz?')

def guardarRegisto():
    # Ler Json
    with open("utilizadores.json", "r") as ficheiro:
        utilizadores =json.loads(ficheiro.read())
    #if nome_utilizador in utilizadores:
    #try utilizadores[nome_utilizador]:
    novo_registo = {
        'valor': pontuacao,
        'data': str(datetime.utcnow())
    }
    try :
        utilizadores[nome_utilizador].append(novo_registo)
    except:
    #else:
        utilizadores[nome_utilizador] = [novo_registo]
    utilizadores = json.dumps(utilizadores, indent=4)
    with open("utilizadores.json", "w") as ficheiro:
        ficheiro.write(utilizadores)


def iniciarQuiz():
    login()
    print("\n")

    for pergunta in perguntas:
        fazerPergunta(pergunta)

        print("\n")
        time.sleep(1)

    print('Acertaste em ' + str(respostas_corretas) + ' perguntas num total de ' + str(total_perguntas) + '.')
    print("\n")

    avaliarPontuacao()
    print("\n")

    guardarRegisto()

    print("Quizz concluido!")

def inserirPergunta() :
    nova_pergunta=input('Insira a sua pergunta: ')
    resp_corr=input('Insira a resposta correcta: ')
    resp1=input('Insira resposta 1: ')
    resp2=input('Insira resposta 2: ')
    resp3=input('Insira resposta 3: ')
    resp4=input('Insira resposta 4: ')
    lista_resp = [resp_corr, resp1, resp2, resp3, resp4]

    # Ler Json
    with open("perguntas.json", "r") as ficheiro :
        perguntas =json.loads(ficheiro.read())
    #if nome_utilizador in utilizadores:
    #try utilizadores[nome_utilizador]:
    id = perguntas[-1]['id']+1
    
    nova_pergunta = {
        "id": id,
        "questao": nova_pergunta,
        "opcoes": lista_resp,
        "respostaCerta": resp_corr
    }
    perguntas.append(nova_pergunta)
    perguntas = json.dumps(perguntas, indent=4)
    with open("perguntas.json", "w") as ficheiro:
        ficheiro.write(perguntas)

total_perguntas = 5
respostas_corretas = 0
pontuacao = 0
perguntas = gerarPerguntas()
nome_utilizador = ''

# iniciarQuiz()
inserirPergunta()