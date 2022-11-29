import pygame

class Scissors(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image = pygame.image.load("images/scissors.png")
        self.image = pygame.transform.scale(image,(175,175))
        self.rect = self.image.get_rect()
        

    def update(self):
        self.rect.bottom = 580
        self.rect.x = 420
