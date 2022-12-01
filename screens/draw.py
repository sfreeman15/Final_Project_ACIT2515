import pygame
from .base_screen import BaseScreen
from components .text_box import TextBox
from components .text import render_text,center_text




#for player 2?
class Draw(BaseScreen):
    def __init__(self,window,state):
        super().__init__(window,state)
        print("Draw")
        self.tie = TextBox((300,80), "It's a draw!", bgcolor=(250,235,215))
        self.play_again = TextBox((300,80), "Try again?", bgcolor=(250,235,215))
        self.menu = TextBox((300,80), "Go back to menu?", bgcolor=(250,235,215))
    def draw(self):
        self.window.fill((0,0,0))
        self.window.blit(self.tie.image,(150,50))
        self.window.blit(self.play_again.image,  (150, 300))
        self.window.blit(self.menu.image, (150, 410))

    def update(self):
        pass

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN: 
            print(event.pos[0])
            # if 440 < event.pos[0] < 500 and 0 < event.pos[1] < 60:
            if 100 < event.pos[0] < 450 and 300 < event.pos[1] < 370:
                self.next_screen ="game_pvp"
                self.running = False
            if 100 < event.pos[0] < 450 and 410 < event.pos[1] < 480:
                self.next_screen ="welcome"
                self.running = False