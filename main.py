import pygame
import sys
pygame.init()

FPS = 60
running = True

def update():
    pygame.display.update()

def main():
    clock = pygame.Clock()
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.EXIT:
                running = False
            if event.type == pygame.KEYDOWN:
                pass
    pygame.quit()