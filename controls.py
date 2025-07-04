import pygame, sys
from bullet import  Bullet
from ino import Ino

def events(screen, gun, bullets):
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
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False

def update(bg_color, screen, gun, inos, bullets):
    """Обновление экрана"""
    screen.fill(bg_color)  # заполняет экран указанным цветом
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()

def update_bullets(bullets):
    """обновлять позиции пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def create_army(screen, inos):
    """создание армии пришельцев"""
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((1200 - 2 * ino_width) / ino_width)

    for ino_number in range(number_ino_x):
        ino = Ino(screen)
        ino.x = ino_width + ino_width * ino_number
        ino.rect.x = ino.x
        inos.add(ino)