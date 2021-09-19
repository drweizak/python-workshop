import pygame

# Definir variaveis
tamanho_ecra = (768, 768)
titulo = "Quizz"
cor_azul_cueca = (153, 204, 255)
cor_vermelho_cueca = (203,66,84)

# Criar um ecra
ecra = pygame.display.set_mode(tamanho_ecra)

# Definir um titulo da janela
pygame.display.set_caption(titulo)

# Criar um relogio
relogio = pygame.time.Clock()

# Definir Fontes
pygame.font.init()
titulo_fonte = pygame.font.SysFont("arial", 80, bold=True, italic=False)

# Iniciar ciclo
while True:

    # Definir cor de fundo
    ecra.fill(cor_azul_cueca)

    # Definir texto
    textoTitulo = titulo_fonte.render(titulo, True, cor_vermelho_cueca)

    # Obter Centro do ecra
    centro_ecra = ecra.get_rect().center

    # Inserir text
    ecra.blit(textoTitulo, (textoTitulo.get_rect(center = centro_ecra)[0], 150))
    
    # Ler todos os evento
    for evento in pygame.event.get():

        # Se evento for do tipo QUIT
        if evento.type == pygame.QUIT:

            # Fechar janela e sai do jogo
            pygame.quit()
            exit()

    # Atualizar o ecra 60 vezes a cada segundo
    pygame.display.update()
    relogio.tick(60)