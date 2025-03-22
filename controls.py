import pygame, sys

def events(gun):
    """Обработка событий"""
    for event in pygame.event.get():  # цикл который постоянно мониторит
        # события пользователя
        if event.type == pygame.QUIT:  # если нажимаем на крестик
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.rect.centerx += 1
