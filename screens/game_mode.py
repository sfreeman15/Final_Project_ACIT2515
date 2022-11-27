import pygame
from .base_screen import BaseScreen
from components .text_box import TextBox
from components .text import render_text,center_text



class GameMode(BaseScreen):
    def __init__(self,window):
        super().__init__(window)
        print("Welcome screen is being called")
        self.mode = TextBox((500,80), "What Game Mode do you want to play?", bgcolor=(250,235,215))
        self.pvp = TextBox((200,80), "Player vs. Player", bgcolor=(250,235,215))
        # self.play_outer= TextBox((200,100),bgcolor=(0,0,0))
        self.AI = TextBox((200,80), "Play vs. A.I", bgcolor=(250,235,215))
        



    def draw(self):
        self.window.fill((69,139,0))
        # self.window.blit(self.play_outer.image, (200, 300))
        # center_text(self.title, (200, 50))
        self.window.blit(self.mode.image,(50,50))
        self.window.blit(self.pvp.image, (200, 190))
        self.window.blit(self.AI.image,  (200, 300))
       
        

    def update(self):
        pass

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN: 
            # if 440 < event.pos[0] < 500 and 0 < event.pos[1] < 60:
            print(event.pos[1])
            if 200 < event.pos[0] < 400 and 190 < event.pos[1] < 270:
                self.next_screen ="game_pvp"
                self.running = False
            if 200 < event.pos[0] < 400 and 300 < event.pos[1] < 380:
                self.next_screen ="cpu"
                self.running = False

 