import pygame
from config import Init, width, height, running, screen_bg




screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mini Game")

screen.fill(screen_bg)
pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        myfont = pygame.font.SysFont("monospace", 75)
        BLACK = (0, 0, 0)
        label = myfont.render("Tutorial 1", 1, BLACK)
        screen.blit(label, (0, 10))
        pygame.display.update()