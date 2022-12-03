import pygame
import json
from screens import BaseScreen
from components import TextBox



#for player 1?
class GameScreenPVP(BaseScreen):
    def __init__(self,window,state):
        """Screen for the player vs. player rock paper scissors mode"""
        super().__init__(window,state)
        """
        Constructs the necessary attributes for the GameScreenPVP class
        Inherits window and state from BaseScreen
        """
        self.timer = pygame.time.get_ticks()
        self.countdown = TextBox((150,80), "Choose your move!", bgcolor=(250,235,215))
        self.json_file = "data/pvp_results.json"
        self.move_p1 = ""
        self.move_p2 = ""
        self.player_info = [{"p1_move": "", "p1_win": "no", "draw": "no"},
        {"p2_move": "", "p2_win": "no", "draw": "no"}]
        self.title = TextBox((300,80), "Choose your move!", bgcolor=(250,235,215))
        self.p1 = TextBox((150,50), "Player One", bgcolor=(250,235,215))
        self.rock_input_p1 = TextBox((150,50), "q = rock", bgcolor=(250,235,215))
        self.paper_input_p1 = TextBox((150,50), "w = paper", bgcolor=(250,235,215))
        self.scissors_input_p1 = TextBox((150,50), "e = scissors", bgcolor=(250,235,215))
        self.p2 = TextBox((150,50), "Player Two", bgcolor=(250,235,215))
        self.rock_input_p2 = TextBox((150,50), "i = rock", bgcolor=(250,235,215))
        self.paper_input_p2 = TextBox((150,50), "o = paper", bgcolor=(250,235,215))
        self.scissors_input_p2 = TextBox((150,50), "p = scissors", bgcolor=(250,235,215))

    
    def draw(self):
        """Displays text and images to the window"""
        self.window.fill((0,0,0))
        self.window.blit(self.title.image,(150,50))
        self.window.blit(self.p1.image,(50,250))
        self.window.blit(self.rock_input_p1.image,(50,300))
        self.window.blit(self.paper_input_p1.image,(50,350))
        self.window.blit(self.scissors_input_p1.image,(50,400))    
        self.window.blit(self.p2.image,(400,250))
        self.window.blit(self.rock_input_p2.image,(400,300))
        self.window.blit(self.paper_input_p2.image,(400,350))
        self.window.blit(self.scissors_input_p2.image,(400,400))
    


        
        
    def update(self):
        pass
            
    def write_to_json(self):
        """Stores the player's moves, and results of the game in the pvp_results.json for the pvp_results screen"""
        with open(self.json_file, "w") as f:
            json.dump(self.player_info, f)

    def game_logic(self):
        """Determines the winner of the game based on rock paper scissors rules. Uses the write_to_json method to append the moves and winner/loser to the pvp_results.json. Once the results have been determined, moves to the pvp_results screen"""
        if self.move_p1 == "rock" and self.move_p2 == "scissors":        
            self.player_info[0]["p1_win"] = "yes"   
            self.write_to_json()   
            self.next_screen = "results_pvp"
            self.running = False
        elif self.move_p1 == "paper" and self.move_p2 == "rock":   
            self.player_info[0]["p1_win"] = "yes"
            self.write_to_json()    
            self.next_screen = "results_pvp"
            self.running = False
        elif self.move_p1 == "scissors" and self.move_p2 == "paper": 
            self.player_info[0]["p1_win"] = "yes"
            self.write_to_json()  
            self.next_screen = "results_pvp"
            self.running = False
        elif self.move_p2 == "rock" and self.move_p1 == "scissors":
            self.player_info[1]["p2_win"] = "yes"
            self.write_to_json()
            self.next_screen = "results_pvp"
            self.running = False
        elif self.move_p2 == "paper" and self.move_p1 == "rock":
            self.player_info[1]["p2_win"] = "yes"
            self.write_to_json()
            self.next_screen = "results_pvp"
            self.running = False
        elif self.move_p2 == "scissors" and self.move_p1 == "paper":
            self.player_info[1]["p2_win"] = "yes"
            self.write_to_json()
            self.next_screen = "results_pvp"
            self.running = False
        elif self.move_p1 == self.move_p2:
            self.write_to_json()
            for category in self.player_info:
                category["draw"] = "yes"
            self.write_to_json()
            self.next_screen = "results_pvp"
            self.running = False




    
    def manage_event(self, event):
        """
        Determines what moves the players use depending on what key presses they use, and adds them to the player_info dictionary. Once the player has chosen a move, the game_logic method is called to determine who won, and writes the information to the pvp_results.json.

        Args:
            event (_type_): _description_
        """
        if event.type == pygame.KEYDOWN:   
            if pygame.key.name(event.key) == "q":
                self.move_p1 = "rock"
                self.player_info[0]["p1_move"] = self.move_p1
                self.game_logic()
            if pygame.key.name(event.key) == "w":
                self.move_p1 = "paper"
                self.player_info[0]["p1_move"] = self.move_p1
                self.game_logic()
            if pygame.key.name(event.key) == "e":
                self.move_p1 = "scissors"
                self.player_info[0]["p1_move"] = self.move_p1
                self.game_logic()
            if pygame.key.name(event.key) == "i":
                self.move_p2 = "rock"
                self.player_info[1]["p2_move"] = self.move_p2
                self.game_logic()
            if pygame.key.name(event.key) == "o":
                self.move_p2 = "paper"
                self.player_info[1]["p2_move"] = self.move_p2
                self.game_logic()
            if pygame.key.name(event.key) == "p":
                self.move_p2 = "scissors"
                self.player_info[1]["p2_move"] = self.move_p2
                self.game_logic()
            



            
            
            

