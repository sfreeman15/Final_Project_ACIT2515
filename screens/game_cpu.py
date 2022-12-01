import pygame
import json
import random
from .base_screen import BaseScreen
from components .text_box import TextBox
from components .text import render_text,center_text




#for player 1?
class GameScreenCPU(BaseScreen):
    def __init__(self,window,state):
        super().__init__(window,state)
        self.json_file = "data/score.json"
        self.user_file = "data/initial_user.json"
        self.cpu_choice = ""
        self.move_player = ""
        self.player_score = {
            "score": 0
        }

        self.move = TextBox((300,80), "Choose your move!", bgcolor=(250,235,215))
        self.q_rock = TextBox((300,80), "q: rock", bgcolor=(250,235,215))
        self.w_paper = TextBox((300,80), "w: paper", bgcolor=(250,235,215))
        self.e_scissors = TextBox((300,80), "e: scissors", bgcolor=(250,235,215))
        self.info = TextBox((500,80), "The moves will display in the terminal", color=(255,255,255),bgcolor=(0,0,0))

        
        self.time_limit = pygame.time.get_ticks()

    def draw(self):
        self.window.fill((0,0,0))
        # self.window.blit(self.play_outer.image, (200, 300))
        # center_text(self.title, (200, 50))
        self.window.blit(self.move.image,(150,50))
        self.window.blit(self.q_rock.image,(150,125))
        self.window.blit(self.w_paper.image,(150,200))
        self.window.blit(self.e_scissors.image,(150,275))
        self.window.blit(self.info.image,(50,400))
    
    def draw_score(self):
        pass

      
        
    def cpu(self):
        moves = ["rock", "paper", "scissors"]
        self.cpu_choice = random.choice(moves)
        

    def update(self):
        pass

    # def load_from_json(self):
    #     with open(self.user_file ,"r") as f:
    #         self.data = json.load(f)
    #         # for name in data:
    #         if self.state["name"] not in self.data.keys():
    #             self.data[self.state["name"]] = []
            
    #         self.data[self.state["name"]].append(self.player_score["score"])            
                

    def write_to_json(self):
        print(self.state)
        with open(self.json_file,"r") as f:
            self.data = json.load(f)
        if self.state["name"] not in self.data.keys():
            self.data[self.state["name"]] = []   
        self.data[self.state["name"]].append(self.player_score["score"])
        with open(self.json_file, "w") as f:
            json.dump(self.data, f)
    




    def game_logic(self):
        if self.move_player == "rock" and  self.cpu_choice == "scissors":
            self.player_score["score"] += 1
            self.state["score"] += 1
        elif self.move_player == "paper" and self.cpu_choice == "rock":
           self.player_score["score"] += 1 
           self.state["score"] += 1
        elif self.move_player == "scissors" and self.cpu_choice == "paper":
            self.player_score["score"] += 1
            self.state["score"] += 1
        elif self.cpu_choice == "rock" and self.move_player == "scissors":
            # self.load_from_json()
            self.write_to_json()
            self.next_screen = "game_over"
            self.running = False
        elif self.cpu_choice == "paper" and self.move_player == "rock":
            # self.load_from_json()
            self.write_to_json()
            self.next_screen = "game_over"
            self.running = False
        elif self.cpu_choice== "scissors" and self.move_player == "paper":
            # self.load_from_json()
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
         
