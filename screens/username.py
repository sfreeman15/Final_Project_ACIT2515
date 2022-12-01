import pygame
import json
import random
from .base_screen import BaseScreen
from components .text_box import TextBox
from components .text import render_text,center_text


#for player 1?
class Username(BaseScreen):
    def __init__(self,window,state):
        super().__init__(window,state)
        self.json_file = "data/initial_user.json"
        # self.username = ""
        self.type = TextBox((300,80), "Type your username", bgcolor=(250,235,215))
        self.luck = TextBox((600,80), "Test your luck against the computer!",color=(255,255,255) ,bgcolor=(0,0,0))
        self.upload = TextBox((600,80), "Your score will be uploaded to the leaderboard",color=(255,255,255) ,bgcolor=(0,0,0))
        self.max_characters = TextBox((300,80), "8 letters max", bgcolor=(250,235,215))
        self.state["name"] = ""
        self.state["score"] = 0
        self.time_limit=pygame.time.get_ticks()

    def draw(self):
        self.window.fill((0,0,0))
        # self.window.blit(self.play_outer.image, (200, 300))
        # center_text(self.title, (200, 50))
        self.window.blit(self.type.image,(150,50))
        self.window.blit(self.max_characters.image,(150,130))
        self.window.blit(self.user_input.image,(150,500))
        self.window.blit(self.luck.image,(0, 275))
        self.window.blit(self.upload.image,(0,350))

        
    def draw_score(self):
        pass

    
        
    def cpu(self):
        moves = ["rock", "paper", "scissors"]
        self.cpu_choice = random.choice(moves)
        

    def update(self):
        self.user_input = TextBox((300,80), f"{self.state['name']}", bgcolor=(250,235,215))

        
    def write_to_json(self):
        with open(self.json_file, "w") as f:
            json.dump(self.state, f)


    def manage_event(self, event):
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_BACKSPACE:
                self.state["name"] = self.state["name"][:-1]
                print(str(self.state["name"]))
            else:
                if event.key in range(pygame.K_a, pygame.K_z + 1):
                    self.state["name"] += str(event.unicode)
                    print(str(self.state["name"]))
            if len(self.state["name"]) >= 1:
                if len(self.state["name"]) >= 8 or event.key == pygame.K_RETURN:
                    # self.state[self.username] = []
                    print(self.state["name"])
                    # self.write_to_json()
                    self.next_screen = "cpu"
                    self.running = False
       
