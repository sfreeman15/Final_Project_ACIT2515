import pygame
import random
from .base_screen import BaseScreen
from components .text_box import TextBox
from components .text import render_text,center_text


#for player 1?
class GameScreenCPU(BaseScreen):
    def __init__(self,window):
        super().__init__(window)
        self.cpu_choice = ""
        self.move_player = ""
        self.player_score = 0
        self.move = TextBox((300,80), "Choose your move!", bgcolor=(250,235,215))
        self.total_score = TextBox((300,80), f"{self.player_score}", bgcolor=(250,235,215))
        
        self.time_limit=pygame.time.get_ticks()

    def draw(self):
        self.window.fill((69,139,0))
        # self.window.blit(self.play_outer.image, (200, 300))
        # center_text(self.title, (200, 50))
        self.window.blit(self.move.image,(150,50))
        self.window.blit(self.total_score.image,(150,200))

        
    def draw_score(self):
        pass

      
        
    def cpu(self):
        moves = ["rock", "paper", "scissors"]
        self.cpu_choice = random.choice(moves)
        

    def update(self):
        pass

    def game_logic(self):
        if self.move_player == "rock" and  self.cpu_choice == "scissors":
            self.player_score = self.player_score + 1
        elif self.move_player == "paper" and self.cpu_choice == "rock":
            self.player_score = self.player_score + 1
        elif self.move_player == "scissors" and self.cpu_choice == "paper":
            self.player_score = self.player_score + 1
        # elif self.self.cpu_choice == "rock" and self.move_p1 == "scissors":
        #         self.next_screen = "winner_p2"
        #         self.running = False
        # elif self.self.cpu_choice == "paper" and self.move_p1 == "rock":
        #     self.next_screen = "winner_p2"
        #     self.running = False
        # elif self.self.cpu_choice== "scissors" and self.move_p1 == "paper":
        #     self.next_screen = "winner_p2"
        #     self.running = False
        # elif self.move_p1 == self.move_p2:
        #     self.next_screen = "draw"
        #     self.running = False


    def manage_event(self, event):
        if event.type == pygame.KEYDOWN:   
            GameScreenCPU.cpu(self)
            print(self.cpu_choice)
            if pygame.key.name(event.key) == "q":
                self.move_player = "rock"
                print(self.move_player)
                GameScreenCPU.game_logic(self)
                print(self.player_score)
                # self.next_screen ="game_p2"
            if pygame.key.name(event.key) == "w":
                self.move_player = "paper"
                print(self.move_player)
                GameScreenCPU.game_logic(self)
                print(self.player_score)
                # self.next_screen ="game_p2"
                # self.running = False
            if pygame.key.name(event.key) == "e":
                self.move_player = "scissors"
                print(self.move_player)
                GameScreenCPU.game_logic(self)
                print(self.player_score)
            # if self.move_player == "rock" and self.cpu_choice == "scissors":
            #     self.player_score += 1
            #     GameScreenCPU.update(self)
            #     print(self.player_score)
            # elif self.move_player == "paper" and self.cpu_choice == "rock":
            #     self.player_score += 1
            #     GameScreenCPU.update(self)
            #     print(self.player_score)
            # elif self.move_player == "scissors" and self.cpu_choice == "paper":
            #     self.player_score += 1
            #     GameScreenCPU.update(self)
            #     print(self.player_score)
           

