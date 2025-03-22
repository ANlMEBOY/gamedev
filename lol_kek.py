import pygame, controls
from gun import Gun

def run():
    pygame.init() #инициализируем модуль пайгейм
    screen = pygame.display.set_mode((700, 800)) #обозначили разрешение экрана
    pygame.display.set_caption("Космические защитники") #название окна игры
    bg_color = (0, 0, 0) #цвет экрана
    gun = Gun(screen)#добавили пушку

    while True:
        controls.events(gun)
        screen.fill(bg_color) # заполняет экран указанным цветом
        gun.output()
        pygame.display.flip()
run()
