# Quizz
# Uma pergunta com várias opções onde normalmente apenas 1 é verdadeira
# -- O que pode ser melhorado?
# Várias Perguntas
# Inserir Perguntas
# Listas de respostas
# Funções de verificação
# Validação
# Perguntas  / Respostas aleatórias (Dicionario)
# Pontuação
# Nome utilizador, data, score

import time

pergunta1 = "Qual das palavras não pertence à família da Arvore?"

a="a. computador"
b="b. folha"
c="c. tronco"
d="d. ramos"
e="e. raiz"

print(pergunta1)
print(a)
print(b)
print(c)
print(d)
print(e)

respostaCerta = "a"

resposta = input("Resposta:")

print("A tua resposta está... ")

time.sleep(2) # delay de 2 seg.

if resposta == respostaCerta:
    print("Correcta")
else:
    print("Errada")


#este e outro teste!