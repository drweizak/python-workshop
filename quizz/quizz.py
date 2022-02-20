import time
import random
import json
from datetime import datetime
from .class_cores import Cores as cor
  
def gerarPerguntas(total_perguntas, categoriasEscolhidas):
   
    # Ler Json
    with open("categorias.json", "r") as ficheiro:
        categorias = json.loads(ficheiro.read())
        
    with open("perguntas.json", "r") as ficheiro:
        perguntas = json.loads(ficheiro.read())

    random.shuffle(perguntas)    
    
    if len(categoriasEscolhidas) > 0:
        # Filtrar perguntas
        perguntas = list(filter(lambda p: filtrarPorCategorias(p, categoriasEscolhidas), perguntas))
    
    return perguntas[:total_perguntas] 

def filtrarPorCategorias(pergunta, categoriasEscolhidas):
    
    for categoria in categoriasEscolhidas:
        if categoria in pergunta['categorias']:
            return True

    return False

def guardarRegisto(nome_utilizador, pontuacao):
    # Ler Json
    with open("utilizadores.json", "r") as ficheiro:
        utilizadores = json.loads(ficheiro.read())
    novo_registo = {
        'valor': pontuacao,
        'data': str(datetime.utcnow())
    }
    try :
        utilizadores[nome_utilizador].append(novo_registo)
    except:
        utilizadores[nome_utilizador] = [novo_registo]
    utilizadores = json.dumps(utilizadores, indent=4)
    with open("utilizadores.json", "w") as ficheiro:
        ficheiro.write(utilizadores)

def avaliarPontuacao(nome_utilizador, pontuacao, total_perguntas):
    percentagem = (pontuacao / total_perguntas) * 100

    if(percentagem < 20):
        mensagem = nome_utilizador + ', oh meu Deus!'
        cor_pontuacao = cor().vermelho_cueca
    elif(percentagem < 50):
        mensagem = nome_utilizador + ', tenta mais uma vez e talvez consigas atingir um patamar aceitável!'
        cor_pontuacao = cor().laranja_cueca
    elif(percentagem < 75):
        mensagem = nome_utilizador + ', não é mau! Mas consegues melhor.'
        cor_pontuacao = cor().amarelo_cueca
    elif(percentagem < 90):
        memensagem = nome_utilizador + ', é pah! Temos génio, mas será que consegues aquele bocadinho "assim"?'
        cor_pontuacao = cor().verde_cueca
    else:
        mensagem = nome_utilizador + ', brutal, acertaste em tudo. Se és assim tão bom/boa nisto, porque não nos ajudas a programar este Quiz?'
        cor_pontuacao = cor().azul_escuro_cueca
        
    return mensagem, cor_pontuacao
