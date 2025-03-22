import pygame.image


class Gun():
    def __init__(self, screen):
        """инициализация пушки"""
        self.screen = screen
        self.image = pygame.image.load(pic/photo_2024-09-24_12-45-43.jpg)
        self.rect = self.image.get_rect() #получили нашу картинку и
        # представили ее в виде прямоугольника через get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def output(self):
        """рисование пушки"""
        self.screen.blit(self.image)