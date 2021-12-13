import time
import random
import json
from datetime import datetime

def gerarPerguntas(total_perguntas):
    # Ler Json
    with open("perguntas.json", "r") as ficheiro:
        perguntas = json.loads(ficheiro.read())

    random.shuffle(perguntas)

    return perguntas[:total_perguntas]

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