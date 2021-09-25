import pygame

# Definir variaveis
cor_azul_cueca = (153, 204, 255)
cor_vermelho_cueca = (203,66,84)
preto_cueca = (0, 0, 0)

class Jogo:

    def __init__(self):
        self.titulo = "Quizz"
        self.tamanho_ecra = (768, 768)
        self.ecra = pygame.display.set_mode(self.tamanho_ecra)
        self.relogio = pygame.time.Clock()
        self.estado = self.menu
        self.eventos = None
        pygame.font.init()
        pygame.display.set_caption(self.titulo)
        
        self.construir()
    
    def construir(self):
        # Iniciar ciclo
        while True:
            self.eventos_globais()
            self.estado()
            # Atualizar o ecra 60 vezes a cada segundo
            pygame.display.update()
            self.relogio.tick(60)

    def eventos_globais(self):
        self.eventos = pygame.event.get()
        for evento in self.eventos:                    
            # Se evento for do tipo QUIT
            if evento.type == pygame.QUIT:
                # Fechar janela e sai do jogo
                pygame.quit()
                exit()

    def menu(self):
        titulo_fonte = pygame.font.SysFont("arial", 80, bold=True, italic=False)
        menu_fonte = pygame.font.SysFont("arial", 40, bold=True, italic=False)

        # Definir cor de fundo
        self.ecra.fill(cor_azul_cueca)

        # Definir texto
        textoTitulo = titulo_fonte.render(self.titulo, True, cor_vermelho_cueca)
        textoButaoJogar = menu_fonte.render("Jogar", True, preto_cueca)
        textoButaoPerguntas = menu_fonte.render("Adicionar perguntas", True, preto_cueca)
        textoButaoPontuacoes = menu_fonte.render("Pontuações", True, preto_cueca)

        # Obter Centro do ecra
        centro_ecra = self.ecra.get_rect().center

        # Inserir text
        self.ecra.blit(textoTitulo, (textoTitulo.get_rect(center = centro_ecra)[0], 150))
        self.ecra.blit(textoButaoJogar, (textoButaoJogar.get_rect(center = centro_ecra)[0], 300))
        self.ecra.blit(textoButaoPerguntas, (textoButaoPerguntas.get_rect(center = centro_ecra)[0], 350))
        self.ecra.blit(textoButaoPontuacoes, (textoButaoPontuacoes.get_rect(center = centro_ecra)[0], 400))

        #pygame.draw.rect(display, (255, 0, 0), (100, 100, 100, 100))
        
        # Ler todos os evento
        
        for evento in self.eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                x, y = pygame.mouse.get_pos()
                #var = textoButaoJogar.collidepoint(pygame.mouse.get_pos())
                #print(textoButaoJogar.get_width())

                if x >= centro_ecra[0] - textoButaoJogar.get_width()/2 and x <= centro_ecra[0] + textoButaoJogar.get_width()/2 and y >=300 and y <= 340:
                    self.estado = self.sel_jogar
                
    def sel_jogar(self):
        titulo_fonte = pygame.font.SysFont("arial", 80, bold=True, italic=False)
        menu_fonte = pygame.font.SysFont("arial", 40, bold=True, italic=False)
        
        # Definir cor de fundo
        self.ecra.fill(cor_azul_cueca)

        # Definir texto
        textoTitulo = titulo_fonte.render("Yey!", True, cor_vermelho_cueca)
        textoButaoJogar = menu_fonte.render("Voltar", True, preto_cueca)


        # Obter Centro do ecra
        centro_ecra = self.ecra.get_rect().center

        # Inserir text
        self.ecra.blit(textoTitulo, (textoTitulo.get_rect(center = centro_ecra)[0], 150))
        self.ecra.blit(textoButaoJogar, (textoButaoJogar.get_rect(center = centro_ecra)[0], 300))


        #pygame.draw.rect(display, (255, 0, 0), (100, 100, 100, 100))
        
        # Ler todos os evento
        
        for evento in self.eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                x, y = pygame.mouse.get_pos()
                #var = textoButaoJogar.collidepoint(pygame.mouse.get_pos())
                #print(textoButaoJogar.get_width())

                if x >= centro_ecra[0] - textoButaoJogar.get_width()/2 and x <= centro_ecra[0] + textoButaoJogar.get_width()/2 and y >=300 and y <= 340:
                    self.estado = self.menu


quizz = Jogo()