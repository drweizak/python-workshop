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