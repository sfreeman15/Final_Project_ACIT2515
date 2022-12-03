import pygame
import json
import random
from screens import BaseScreen
from components import TextBox




#for player 1?
class GameScreenCPU(BaseScreen):
    """Screen for the player vs computer game mode"""
    def __init__(self,window,state):
        super().__init__(window,state)
        """
        Constructs the necessary attributes for the GameScreenCPU class
        Inherits window and state from Basescreen. State is used to keep track of the player's name and scores.
        """
        self.json_file = "data/score.json"
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

    def draw(self):
        """Displays text and images to the window"""
        self.window.fill((0,0,0))
        self.window.blit(self.move.image,(150,50))
        self.window.blit(self.q_rock.image,(150,125))
        self.window.blit(self.w_paper.image,(150,200))
        self.window.blit(self.e_scissors.image,(150,275))
        self.window.blit(self.info.image,(50,400))
        
    def cpu(self):
        """Makes the computer choose randomly between rock, paper, or scissors"""
        moves = ["rock", "paper", "scissors"]
        self.cpu_choice = random.choice(moves)
        

    def update(self):
        pass

    def write_to_json(self):
        """
        Loads the score.json file. If self.state is not in score.json's keys, creates a name key for the player. Appends the player's score to the name key as a list. Afterwards, it writes the  player's name and score key-value to the score.json file.
        """
        with open(self.json_file,"r") as f:
            self.data = json.load(f)
        if self.state["name"] not in self.data.keys():
            self.data[self.state["name"]] = []   
        self.data[self.state["name"]].append(self.player_score["score"])
        with open(self.json_file, "w") as f:
            json.dump(self.data, f)
    




    def game_logic(self):
        """
        Creates the game logic for the player vs. computer. Adds a point to the player's score if the player wins. If the computer wins, the player is brought to the game over screen, and the user's name and score are stored in score.json as a key-value pair. If the player and computer choose the same move, it is declared a draw and the player gets to choose another move.
        """
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
        """
        Determines which key presses equate to a move for the player. If player presses q, w, or e, the rock, paper, or scissors move will be chosen, The cpu method will choose a move for the computer, and the game_logic method will determine if the player or computer won.

        Args:
            event (_type_): _description_
        """
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
         
