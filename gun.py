import pygame.image


class Gun():
    def __init__(self, screen):
        """инициализация пушки"""
        self.screen = screen
        self.image = pygame.image.load('pic/e1988d7c30075cfbdf631be1fd70e11f.jpg')
        self.rect = self.image.get_rect() #получили нашу картинку и
        # представили ее в виде прямоугольника через get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        """рисование пушки"""
        self.screen.blit(self.image, self.rect)#метод blit отрисовывает пушку

    def update_gun(self):
        """Обновление позиции пушки"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        if self.mleft and self.rect.left > 0:
            self.center -= 1.5

        self.rect.centerx = self.center