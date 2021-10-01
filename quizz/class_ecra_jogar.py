import pygame


class Jogar():

    jogo = None

    def __init__(self, jogo):
        self.jogo = jogo

        self.construir()

    def construir(self):
        # Definir variaveis
        cor_azul_cueca = (153, 204, 255)
        cor_vermelho_cueca = (203, 66, 84)
        preto_cueca = (0, 0, 0)

        titulo_fonte = pygame.font.SysFont(
            "arial", 80, bold=True, italic=False)
        menu_fonte = pygame.font.SysFont("arial", 40, bold=True, italic=False)

        # Definir cor de fundo
        self.jogo.ecra.fill(cor_azul_cueca)

        # Definir texto
        textoTitulo = titulo_fonte.render("Yey!", True, cor_vermelho_cueca)
        textoButaoJogar = menu_fonte.render("Voltar", True, preto_cueca)

        # Obter Centro do ecra
        centro_ecra = self.jogo.ecra.get_rect().center

        # Inserir text
        self.jogo.ecra.blit(
            textoTitulo, (textoTitulo.get_rect(center=centro_ecra)[0], 150))
        self.jogo.ecra.blit(textoButaoJogar,
                            (textoButaoJogar.get_rect(center=centro_ecra)[0], 300))

        # pygame.draw.rect(display, (255, 0, 0), (100, 100, 100, 100))

        # Ler todos os evento

        for evento in self.jogo.eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                x, y = pygame.mouse.get_pos()
                # var = textoButaoJogar.collidepoint(pygame.mouse.get_pos())
                # print(textoButaoJogar.get_width())

                if x >= centro_ecra[0] - textoButaoJogar.get_width()/2 and x <= centro_ecra[0] + textoButaoJogar.get_width()/2 and y >= 300 and y <= 340:
                    self.jogo.estado = self.jogo.ecras["menu"]
