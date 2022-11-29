import pygame
import json
import random
from .base_screen import BaseScreen
from components .text_box import TextBox
from components .text import render_text,center_text




#for player 1?
class GameScreenCPU(BaseScreen):
    def __init__(self,window):
        super().__init__(window)
        self.json_file = "data/score.json"
        self.cpu_choice = ""
        self.move_player = ""
        self.player_score = {
            "score": 0
        }
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
            json.dump(self.player_score, f)


    def game_logic(self):
        if self.move_player == "rock" and  self.cpu_choice == "scissors":
            self.player_score["score"] += 1
        elif self.move_player == "paper" and self.cpu_choice == "rock":
           self.player_score["score"] += 1 
        elif self.move_player == "scissors" and self.cpu_choice == "paper":
            self.player_score["score"] += 1
        elif self.cpu_choice == "rock" and self.move_player == "scissors":
            self.write_to_json()
            self.next_screen = "game_over"
            self.running = False
        elif self.cpu_choice == "paper" and self.move_player == "rock":
            self.write_to_json()
            self.next_screen = "game_over"
            self.running = False
        elif self.cpu_choice== "scissors" and self.move_player == "paper":
            self.write_to_json()
            self.next_screen = "game_over"
            self.running = False
        elif self.move_player == self.cpu_choice:
            print("Draw! Choose another move.")
            
          


    def manage_event(self, event):
        if event.type == pygame.KEYDOWN:    
            if pygame.key.name(event.key) == "q":
                self.move_player = "rock"
                print(f"You chose: {self.move_player}")
                self.cpu()
                print(f"Computer chose: {self.cpu_choice}")
                self.game_logic()
                print(f"Your score is {self.player_score['score']}")
            if pygame.key.name(event.key) == "w":
                self.move_player = "paper"
                print(f"You chose: {self.move_player}")
                self.cpu()
                print(f"Computer chose: {self.cpu_choice}")
                self.game_logic()
                print(self.player_score["score"])
                print(f"Your score is {self.player_score['score']}")
            if pygame.key.name(event.key) == "e":
                self.move_player = "scissors"
                self.cpu()
                print(f"You chose: {self.move_player}")
                print(f"Computer chose: {self.cpu_choice}")
                self.game_logic()
                print(self.player_score["score"])
                print(f"Your score is {self.player_score['score']}")
         
