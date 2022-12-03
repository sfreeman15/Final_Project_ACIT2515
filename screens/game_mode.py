import pygame
from screens import BaseScreen
from components import TextBox




class GameMode(BaseScreen):
    def __init__(self,window,state):
        """Screen for players to choose between player vs. another player or playing against a computer"""
        super().__init__(window,state)
        """
        Constructs the necessary attributes for the GameMode class
        Inherits window from BaseScreen
        """
        self.mode = TextBox((500,80), "What Game Mode do you want to play?", bgcolor=(250,235,215))
        self.pvp = TextBox((200,80), "Player vs. Player", bgcolor=(250,235,215))
        self.AI = TextBox((200,80), "Play vs. A.I", bgcolor=(250,235,215))
        



    def draw(self):
        """Displays text and images to the window"""
        self.window.fill((0,0,0))
        self.window.blit(self.mode.image,(50,50))
        self.window.blit(self.pvp.image, (200, 190))
        self.window.blit(self.AI.image,  (200, 300))
       
        

    def update(self):
        pass

    def manage_event(self, event):
        """
        Changes the screen if the player clicks on the player vs. player or player vs. A.I textboxes.

        Args:
            event (_type_): MOUSEBUTTONDOWN event in pygame
        """
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if 200 < event.pos[0] < 400 and 190 < event.pos[1] < 270:
                self.next_screen ="game_pvp"
                self.running = False
            if 200 < event.pos[0] < 400 and 300 < event.pos[1] < 380:
                self.next_screen ="username"
                self.running = False
    
 
 