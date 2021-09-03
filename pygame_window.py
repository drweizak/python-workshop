import pygame

# create the window
game_screen = pygame.display.set_mode((768, 768))

# set the title
pygame.display.set_caption("quizz")

#clock to update frames
clock = pygame.time.Clock()

#fonts
pygame.font.init()
fontTitle = pygame.font.SysFont("arial", 80, bold=True, italic=False)

color1 = 255

while True:
    game_screen.fill((194, 194, 194))

    #title
    textTitle = fontTitle.render("Quizz", True, (color1,color1*.5,.5))
    game_screen.blit(textTitle, (300, 150))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    color1 = (color1 + 1) % 255

    pygame.display.update()
    clock.tick(60)