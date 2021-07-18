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

# contacto
    # nome
    # telefone
    # idade
    # morada 
        # Rua
        # Porta
        # Codigo Postal
        # Localidade
        # Pais
    # email

import sys
import time

# class contacto:
#     def __init__(self, nome, telefone, idade, morada, email):

#         self.nome = nome 
#         self.telefone = telefone
#         self.idade = idade
#         self.morada = morada
#         self.email = email
    
#     def emaiordeidade(self):
#         if self.idade > 18:
#             return True
#         else:
#             return False

#      # ou
#      self.emaiordeidade = True if self.idade > 18 else False

        
# pessoa1 = contacto("Pedro", 0000, 32, "Rua..", "@gmail.com")
# # pessoa1.nome = "Pedro"

# pessoa2 = contacto("Maria", 9000, 12, "xxx", 'xxx')

# print(pessoa1.nome)
# print(pessoa1.emaiordeidade())
# print(pessoa2.nome)
# print(pessoa2.emaiordeidade())
# print(pessoa2.emaiordeidade())

class questao:
    def __init__(self, titulo, respostas, verifica):
        self.titulo = titulo
        self.respostas = respostas
        self.verifica = verifica

pergunta1 = questao("Qual das palavras não pertence à família da Arvore?", ["Computador", "Folha", "Tronco", "Ramos", "Raiz"], 0)
pergunta2 = questao("Em que anos se deu a união dinástica ibérica?", ["1780-1820", "1580-1640", "1290-1311", "1555-1580", "1467-1509"], 1)
pergunta3 = questao("Em que ano sucedeu o atentado terrorista de 11 de Setembro", ["2021", "1876", "2002", "3001", "2001"], 4)

perguntas = [pergunta1,pergunta2,pergunta3]

def fazerPergunta (pergunta):
    print(pergunta.titulo)

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

    if int(resposta)-1 == pergunta.verifica:
        print("Correcta")
    else:
        print("Errada")

for pergunta in perguntas:
    fazerPergunta(pergunta)
    print("\n")
    time.sleep(1) # delay de 1 seg.

print("Quizz concluido")