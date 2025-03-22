import pygame
import sys

def run():
    pygame.init() #инициализируем модуль пайгейм
    screen = pygame.display.set_mode((1200, 800)) #обозначили разрешение экрана
    pygame.display.set_caption("Космические защитники") #название окна игры
    bg_color = (0, 0, 0) #цвет экрана

    while True:
        for event in pygame.event.get(): #цикл который постоянно мониторит
                                        # события пользователя
            if event.type == pygame.QUIT: #если нажимаем на крестик
                sys.exit()

        screen.fill(bg_color) # заполняет экран указанным цветом
        pygame.display.flip()
run()
