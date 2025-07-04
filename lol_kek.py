import pygame, controls
from gun import Gun
from pygame.sprite import Group

def run():
    pygame.init() #инициализируем модуль пайгейм
    screen = pygame.display.set_mode((1200, 600)) #обозначили разрешение экрана
    pygame.display.set_caption("Космические защитники") #название окна игры
    bg_color = (0, 0, 0) #цвет экрана
    gun = Gun(screen)#добавили пушку
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)

    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        bullets.update()
        controls.update(bg_color, screen, gun, inos, bullets)
        controls.update_bullets(bullets)

run()