import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600), 0, )

YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)


class Pacman:
    def __init__(self):
        self.center_x = 400
        self.center_y = 300
        self.size = 50
        self.raio = self.size // 2

    def paint(self, screen):
        # Desenho do corpo
        pygame.draw.circle(screen, YELLOW, (self.center_x, self.center_y), self.raio, 0)

        # Desenho da boca
        canto_boca = (self.center_x, self.center_y)
        labio_superior = (self.center_x + self.raio, self.center_y - self.raio)
        labio_inferior = (self.center_x + self.raio, self.center_y)
        pontos = [canto_boca, labio_superior, labio_inferior]

        pygame.draw.polygon(screen, BLACK, pontos, 0)

        # Desnho do olho
        olho_x = int(self.center_x + self.raio / 3)
        olho_y = int(self.center_y - self.raio * 0.7)
        olho_raio = int(self.raio / 10)

        pygame.draw.circle(screen, BLACK, (olho_x, olho_y), olho_raio, 0)

if __name__ == "__main__":
    pacman = Pacman()

    while True:
        pacman.paint(screen)
        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()

