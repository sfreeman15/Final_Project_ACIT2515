import pygame

class Paper(pygame.sprite.Sprite):
    """Creates the Paper sprite"""
    def __init__(self):
        super().__init__()
        image = pygame.image.load("images/paper.png")
        self.image = pygame.transform.scale(image,(200,150))
        self.rect = self.image.get_rect()
        

    def update(self):
        """Updates the paper sprite's positioning on the screen"""
        self.rect.bottom = 580
        self.rect.x = 200

    def update_p1(self):
        """Updates the paper sprite's positioning on the screen for the pvp_results if player 1 chooses paper"""
        self.rect.bottom = 320
        self.rect.x = 30

    def update_p2(self):
        """Updates the paper sprite's positioning on the screen for the pvp_results if player 2 chooses paper"""
        self.rect.bottom = 320
        self.rect.x = 355

    

   
