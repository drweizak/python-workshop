# Exercicio 5 - Pontuacao e Avaliacao

# Requisitos passo a passo:

# Criar uma variavel do tipo dicionario com uma estrutura composta por:
    # titulo - Pergunta a fazer ao utilizador. ex: "Quais destas respostas esta correta?"
    # respostas - Lista com cinco posicoes do tipo texto com as possiveis resposta. ex: "2 + 2 e igual a 6"
    # resposta_correta - variavel do tipo texto igual ao valor do elemento correto na lista de respostas

# Criar mais cinco variaveis do tipo dicionario identicas ao dicionario mencionado acima, mas com pergunta e repostas diferentes.

# Criar uma lista com cinco posicoes, onde cada posicao representa uma pergunta. ex: perguntas = [pergunta1, pergunta2, pergunta3]

# Randomizar com shuffle a lista de perguntas

# Criar uma variavel para contabilizar o total de perguntas a apresentar

# Criar uma variavel para contabilizar o total de respostas corretas

# Criar uma variavel para contabilizar os pontos que o utilizador obtem em cada resposta correta

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

            # Incrementar um valor as respostas corretas

            # Incrementar um valor a pontuacao

        # Imprimir "Errada.", se a condicao for falsa

# Criar uma variavel para guardar o nome do utilizador

# Criar um ciclo que corra todas as posicoes da lista de perguntas
    
    # Chamar a funcao declarada para fazer a pergunta acompanhado do dicionario da pergunta

    # Aguardar 1 segundo antes de apresentar a nova pergunta

# Imprimir "Acertaste em 'respostas_corretas' perguntas num total de 'total_perguntas'."

# Obter uma percentagem atraves do calculo entre pontuacao e total de perguntas

    # Se percentagem for inferior a 20% "nome_utilizador, Oh meu Deus!"

    # Se percentagem for inferior a 50% "nome_utilizador, Tenta mais uma vez e talvez consigas atingir um patamar aceitavel!"

    # Se percentagem for inferior a 75% "nome_utilizador, Nao e mau! Mas consegues melhor."

    # Se percentagem for inferior a 90% "E pah! Temos genio, mas sera que consegues aquele bocadinho "assim"?"

    # Se percentagem for superior ou igual a 100% "nome_utilizador, Brutal, acertaste em tudo. Se es assim tao bom nisto, porque nao nos ajudas a programar este Quiz?"

# Imprimir "Quizz Concluido!"
