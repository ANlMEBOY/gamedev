import pygame, sys
from bullet import  Bullet
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

def update(bg_color, screen, gun, bullets):
    """Обновление экрана"""
    screen.fill(bg_color)  # заполняет экран указанным цветом
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    pygame.display.flip()

def update_bullets(bullets):
    """обновлять позиции пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))