import pygame

class TelaInicial:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load('imagem_de_fundo.png').convert()
        self.font = pygame.font.SysFont(None, 50)
        self.text = self.font.render('Pressione qualquer tecla para iniciar', True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=self.screen.get_rect().center)

    def mostrar(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.text, self.text_rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Meu jogo")

    tela_inicial = TelaInicial(screen)

    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            elif event.type == pygame.KEYDOWN:
                rodando = False

        tela_inicial.mostrar()
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
