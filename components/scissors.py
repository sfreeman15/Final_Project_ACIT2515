import pygame

class Scissors(pygame.sprite.Sprite):
    def __init__(self):
        """Creates the scissors sprite"""
        super().__init__()
        image = pygame.image.load("images/scissors.png")
        self.image = pygame.transform.scale(image,(175,175))
        self.rect = self.image.get_rect()
        

    def update(self):
        """Updates the scissors sprite's positioning on the screen"""
        self.rect.bottom = 580
        self.rect.x = 420

    def update_p1(self):
        """Updates the rock sprite's positioning on the screen for the pvp_results if player 1 chooses paper"""
        self.rect.bottom = 320
        self.rect.x = 30

    def update_p2(self):
        """Updates the rock sprite's positioning on the screen for the pvp_results if player 2 chooses paper"""
        self.rect.bottom = 320
        self.rect.x = 355