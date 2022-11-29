import pygame

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image = pygame.image.load("images/rock.png")
        self.image = pygame.transform.scale(image,(225,175))
        self.rect = self.image.get_rect()
        

    def update(self):
        self.rect.bottom = 600

   
