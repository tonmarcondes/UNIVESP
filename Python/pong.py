import pygame

pygame.init()

janela = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

clock.tick(30)