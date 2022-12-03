import pygame

class Rock(pygame.sprite.Sprite):
    """Creates the Rock sprite"""
    def __init__(self):
        super().__init__()
        image = pygame.image.load("images/rock.png")
        self.image = pygame.transform.scale(image,(225,175))
        self.rect = self.image.get_rect()
        

    def update(self):
        """Updates the rock sprite's positioning on the screen"""
        self.rect.bottom = 600
    
    def update_p1(self):
        """Updates the rock sprite's positioning on the screen for the pvp_results if player 1 chooses paper"""
        self.rect.bottom = 320
        self.rect.x = 30

    def update_p2(self):
        """Updates the rock sprite's positioning on the screen for the pvp_results if player 2 chooses paper"""
        self.rect.bottom = 320
        self.rect.x = 370

   
