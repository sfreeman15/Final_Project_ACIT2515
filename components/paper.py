import pygame

class Paper(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image = pygame.image.load("images/paper.png")
        self.image = pygame.transform.scale(image,(200,150))
        self.rect = self.image.get_rect()
        

    def update(self):
        self.rect.bottom = 580
        self.rect.x = 200

    def update_p1(self):
        self.rect.bottom = 320
        self.rect.x = 30

    def update_p2(self):
        self.rect.bottom = 320
        self.rect.x = 355

    

   
