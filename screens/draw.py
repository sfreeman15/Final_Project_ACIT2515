import pygame
from screens import BaseScreen
from components import TextBox




#for player 2?
class Draw(BaseScreen):
    """Screen for when both players choose the same move, resulting in a draw"""
    def __init__(self,window,state):
        super().__init__(window,state)
        """
        Constructs the necessary attributes for the Draw class
        Inherits window size from BaseScreen
        """
        print("Draw")
        self.tie = TextBox((300,80), "It's a draw!", bgcolor=(250,235,215))
        self.play_again = TextBox((300,80), "Try again?", bgcolor=(250,235,215))
        self.menu = TextBox((300,80), "Go back to menu?", bgcolor=(250,235,215))

    def draw(self):
        """Displays text and images to the window"""
        self.window.fill((0,0,0))
        self.window.blit(self.tie.image,(150,50))
        self.window.blit(self.play_again.image,  (150, 300))
        self.window.blit(self.menu.image, (150, 410))

    def update(self):
        pass

    def manage_event(self, event):
        """
        Changes the screen if the player clicks on the play again, go back to main menu textboxes.

        Args:
            event (_type_): MOUSEBUTTONDOWN event in pygame
        """
        if event.type == pygame.MOUSEBUTTONDOWN: 
            print(event.pos[0])
            if 100 < event.pos[0] < 450 and 300 < event.pos[1] < 370:
                self.next_screen ="game_pvp"
                self.running = False
            if 100 < event.pos[0] < 450 and 410 < event.pos[1] < 480:
                self.next_screen ="welcome"
                self.running = False