import pygame
import json
import random
from .base_screen import BaseScreen
from components .text_box import TextBox
from components .text import render_text,center_text


#for player 1?
class Username(BaseScreen):
    def __init__(self,window):
        super().__init__(window)
        self.json_file = "data/score.json"
        self.username = ""
        self.move = TextBox((300,80), "Choose your move!", bgcolor=(250,235,215))
        
        self.time_limit=pygame.time.get_ticks()

    def draw(self):
        self.window.fill((0,0,0))
        # self.window.blit(self.play_outer.image, (200, 300))
        # center_text(self.title, (200, 50))
        self.window.blit(self.move.image,(150,50))

        
    def draw_score(self):
        pass

      
        
    def cpu(self):
        moves = ["rock", "paper", "scissors"]
        self.cpu_choice = random.choice(moves)
        

    def update(self):
        pass

        
    def write_to_json(self):
        with open(self.json_file, "w") as f:
            json.dump(self.username, f)


    def manage_event(self, event):
        if event.type == pygame.KEYDOWN:  
            if event.key in range(pygame.K_a, pygame.K_z + 1):
                self.username += event.unicode
                print(self.username)
