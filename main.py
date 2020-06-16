import pygame


YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
SPEED = 0.1
RAIO = 30

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, )
x = 30
y = 30
spd_x = SPEED
spd_y = SPEED

while True:
    # Calcula as regras
    x = x + spd_x
    y = y + spd_y

    if x + RAIO > 640:
        spd_x = -SPEED
    elif x - RAIO < 0:
        spd_x = SPEED
    elif y + RAIO > 480:
        spd_y = -SPEED
    elif y - RAIO < 0:
        spd_y = SPEED


    # Pinta
    screen.fill((BLACK))
    pygame.draw.circle(screen, YELLOW, (int(x), int(y)), RAIO, 0)
    pygame.display.update()

    #Eventos

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
