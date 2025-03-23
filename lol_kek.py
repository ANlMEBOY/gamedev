import pygame, controls
from gun import Gun
from pygame.sprite import Group

def run():
    pygame.init() #инициализируем модуль пайгейм
    screen = pygame.display.set_mode((700, 500)) #обозначили разрешение экрана
    pygame.display.set_caption("Космические защитники") #название окна игры
    bg_color = (0, 0, 0) #цвет экрана
    gun = Gun(screen)#добавили пушку
    bullet

    while True:
        controls.events(gun)
        gun.update_gun()
        controls.update(bg_color, screen, gun)
run()
