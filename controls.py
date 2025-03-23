import pygame, sys

def events(gun):
    """Обработка событий"""
    for event in pygame.event.get():  # цикл который постоянно мониторит
        # события пользователя
        if event.type == pygame.QUIT:  # если нажимаем на крестик
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            """Обрабатываем нажатия клавиш"""
            if event.key == pygame.K_d: #вправо
                gun.mright = True
            elif event.key == pygame.K_a: #влево
                gun.mleft = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False

def update(bg_color, screen, gun):
    """Обновление экрана"""
    screen.fill(bg_color)  # заполняет экран указанным цветом
    gun.output()
    pygame.display.flip()