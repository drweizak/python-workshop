# Exercicio 4 - Ciclo While, Random Shuffle

# Ciclo While
# https://www.w3schools.com/python/python_while_loops.asp

# Random Shuffle
# https://www.w3schools.com/python/ref_random_shuffle.asp


# Requisitos passo a passo:

# Criar uma variavel do tipo dicionario com uma estrutura composta por:
    # titulo - Pergunta a fazer ao utilizador. ex: "Quais destas respostas esta correta?"
    # respostas - Lista com cinco posicoes do tipo texto com as possiveis resposta. ex: "2 + 2 e igual a 6"
    # resposta_correta - variavel do tipo texto igual ao valor do elemento correto na lista de respostas

# Criar mais cinco variaveis do tipo dicionario identicas ao dicionario mencionado acima, mas com pergunta e repostas diferentes.

# Criar uma lista com cinco posicoes, onde cada posicao representa uma pergunta. ex: perguntas = [pergunta1, pergunta2, pergunta3]

# Randomizar com shuffle a lista de perguntas

# Declarar uma funcao, que deve de conter um parametro do tipo dicionario, a funcao e responsavel em:
    # Imprimir titulo do dicionario pergunta

    # Randomizar com shuffle a lista de respostas

    # Criar um ciclo que corra todas as posicoes da lista de respostas do dicionario pergunta.

        # Imprimir numeracao atras de cada resposta para ser mais facil identificar a resposta 

    # Criar um ciclo while que verifique se a resposta introduzida e valida
        
        # Ler um valor introduzido pelo utilizador e guarda-lo numa variavel

        # Verificar se o valor introduzido pelo utilizador e:
            # Um numero
            # E > zero e <= que o tamanho da lista de respostas do dicionario pergunta

            # Quebrar o ciclo while se a reposta for verdadeira
            
            # Imprimir "Resposta invalida, tente outra vez!", se a condicao for falsa            

    # Imprimir "A tua resposta esta..."

    # Aguardar 2 segundos antes de apresentar o resultado

    # Obter o valor da lista de respostas do dicionario pergunta atraves do numero introduzido pelo utilizador e guardar numa varivel
    
    # Comparar se essa variavel recentemente guardada e igual a resposta_correta do dicionario pergunta.

        # Imprimir "Correta.", se a condicao for verdadeira

        # Imprimir "Errada.", se a condicao for falsa

# Criar um ciclo que corra todas as posicoes da lista de perguntas
    
    # Chamar a funcao declarada para fazer a pergunta acompanhado do dicionario da pergunta

    # Aguardar 1 segundo antes de apresentar a nova pergunta

# Imprimir "Quizz Concluido!"
