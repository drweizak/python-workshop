import pygame

# Definir variaveis
tamanho_ecra = (768, 768)
titulo = "Quizz"
cor_azul_cueca = (153, 204, 255)
cor_vermelho_cueca = (203,66,84)
preto_cueca = (0, 0, 0)

# Criar um ecra
ecra = pygame.display.set_mode(tamanho_ecra)

# Definir um titulo da janela
pygame.display.set_caption(titulo)

# Criar um relogio
relogio = pygame.time.Clock()

# Definir Fontes
pygame.font.init()
titulo_fonte = pygame.font.SysFont("arial", 80, bold=True, italic=False)
menu_fonte = pygame.font.SysFont("arial", 40, bold=True, italic=False)

# Iniciar ciclo
while True:

    # Definir cor de fundo
    ecra.fill(cor_azul_cueca)

    # Definir texto
    textoTitulo = titulo_fonte.render(titulo, True, cor_vermelho_cueca)
    textoButaoJogar = menu_fonte.render("Jogar", True, preto_cueca)
    textoButaoPerguntas = menu_fonte.render("Adicionar perguntas", True, preto_cueca)
    textoButaoPontuacoes = menu_fonte.render("Pontuações", True, preto_cueca)

    # Obter Centro do ecra
    centro_ecra = ecra.get_rect().center

    # Inserir text
    ecra.blit(textoTitulo, (textoTitulo.get_rect(center = centro_ecra)[0], 150))
    ecra.blit(textoButaoJogar, (textoButaoJogar.get_rect(center = centro_ecra)[0], 300))
    ecra.blit(textoButaoPerguntas, (textoButaoPerguntas.get_rect(center = centro_ecra)[0], 350))
    ecra.blit(textoButaoPontuacoes, (textoButaoPontuacoes.get_rect(center = centro_ecra)[0], 400))

    #pygame.draw.rect(display, (255, 0, 0), (100, 100, 100, 100))
    
    # Ler todos os evento
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            x, y = pygame.mouse.get_pos()
            #var = textoButaoJogar.collidepoint(pygame.mouse.get_pos())
            #print(textoButaoJogar.get_width())


            if x >= centro_ecra[0] - textoButaoJogar.get_width()/2 and x <= centro_ecra[0] + textoButaoJogar.get_width()/2 and y >=300 and y <= 340:
                print("Jogar")
                
        # Se evento for do tipo QUIT
        if evento.type == pygame.QUIT:

            # Fechar janela e sai do jogo
            pygame.quit()
            exit()

        #if evento.type == pygame.MOUSEMOTION:
        #    mouse_position = pygame.mouse.get_pos()
        #    a_block.set_position(mouse_position[0],mouse_position[1])

    # Atualizar o ecra 60 vezes a cada segundo
    pygame.display.update()
    relogio.tick(60)