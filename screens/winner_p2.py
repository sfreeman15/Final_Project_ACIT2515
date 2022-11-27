import pygame
from .base_screen import BaseScreen
from components .text_box import TextBox
from components .text import render_text,center_text



#for player 2?
class ResultsP2(BaseScreen):
    def __init__(self,window):
        super().__init__(window)
        print("Winner 2 screen is being called")
        self.winner_p1 = TextBox((300,80), "Player 2 wins!", bgcolor=(250,235,215))
        self.play_again = TextBox((300,80), "Play again?", bgcolor=(250,235,215))
        self.menu = TextBox((300,80), "Go back to menu?", bgcolor=(250,235,215))
    def draw(self):
        self.window.fill((69,139,0))
        self.window.blit(self.winner_p1.image,(150,50))
        self.window.blit(self.play_again.image,  (150, 300))
        self.window.blit(self.menu.image, (150, 410))
     

    def update(self):
        pass

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if 100 < event.pos[0] < 450 and 300 < event.pos[1] < 370:
                self.next_screen ="game_pvp"
                self.running = False
            if 100 < event.pos[0] < 450 and 410 < event.pos[1] < 480:
                self.next_screen ="welcome"
                self.running = False
