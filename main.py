import pygame

# Criar um ecra
ecra = pygame.display.set_mode((768, 768))

# Definir um titulo da janela
pygame.display.set_caption("Quizz")

# Criar um relogio
relogio = pygame.time.Clock()

# Definir variaveis

# Iniciar ciclo

while True:

    # Ler todos os eventos
    for evento in pygame.event.get():

        # Se evento for do tipo QUIT
        if evento.type == pygame.QUIT:

            # Fechar janela e sai do jogo
            pygame.quit()
            exit()

    # Atualizar o ecra 60 vezes a cada segundo
    pygame.display.update()
    relogio.tick(60)