import pygame
import json
from screens import BaseScreen
from components import TextBox, Rock, Paper, Scissors


#for player 2?
class ResultsPVP(BaseScreen):
    def __init__(self,window,state):
        """Screen for showing the results of player vs. player mode"""
        super().__init__(window,state)
        self.clock = pygame.time.Clock()
        self.time_counter = 0
        self.paper = Paper()
        self.rock = Rock()
        self.scissors = Scissors()
        self.json_file = "data/pvp_results.json"
        self.winner_p1 = TextBox((300,80), "Player 1 wins!", bgcolor=(250,235,215))
        self.winner_p2 = TextBox((300,80), "Player 2 wins!", bgcolor=(250,235,215))
        self.tie = TextBox((300,80), "It's a draw!", bgcolor=(250,235,215))
        self.play_again = TextBox((300,80), "Play again?", bgcolor=(250,235,215))
        self.menu = TextBox((300,80), "Go back to menu?", bgcolor=(250,235,215))
        self.start_time = pygame.time.get_ticks()


    def load_from_json(self):
        """Loads the pvp_results.json file"""
        with open(self.json_file, "r") as f:
            return json.load(f)
    
    def draw(self):
        """Displays text and images to the window. Depending on the moves chosen by each player, it will display a different sprite. Example: If player 1 chose rock, will display rock sprite on the left side. If player 2 chose scissors, will display scissor sprite on the right side"""
        self.window.fill((0,0,0))   
        winner = ResultsPVP.load_from_json(self)
        if winner[0]["p1_win"] == "yes" and winner[1]["p2_win"] == "no":
            if winner[0]["p1_move"] == "rock":
                self.window.blit(self.rock.image, self.rock.rect)
                self.rock.update_p1()
            if winner[0]["p1_move"] == "paper":
                self.window.blit(self.paper.image, self.paper.rect)
                self.paper.update_p1()
            if winner[0]["p1_move"] == "scissors":
                self.window.blit(self.scissors.image, self.scissors.rect)
                self.scissors.update_p1()
            if winner[1]["p2_move"] == "rock":
                self.window.blit(self.rock.image, self.rock.rect)
                self.rock.update_p2()
            if winner[1]["p2_move"] == "paper":
                self.window.blit(self.paper.image, self.paper.rect)
                self.paper.update_p2()
            if winner[1]["p2_move"] == "scissors":
                self.window.blit(self.scissors.image, self.scissors.rect)
                self.scissors.update_p2()
            self.window.blit(self.winner_p1.image,(150,50))
        if winner[1]["p2_win"] == "yes" and winner[0]["p1_win"] == "no":
            if winner[0]["p1_move"] == "rock":
                self.window.blit(self.rock.image, self.rock.rect)
                self.rock.update_p1()
            if winner[0]["p1_move"] == "paper":
                self.window.blit(self.paper.image, self.paper.rect)
                self.paper.update_p1()
            if winner[0]["p1_move"] == "scissors":
                self.window.blit(self.scissors.image, self.scissors.rect)
                self.scissors.update_p1()
            if winner[1]["p2_move"] == "rock":
                self.window.blit(self.rock.image, self.rock.rect)
                self.rock.update_p2()
            if winner[1]["p2_move"] == "paper":
                self.window.blit(self.paper.image, self.paper.rect)
                self.paper.update_p2()
            if winner[1]["p2_move"] == "scissors":
                self.window.blit(self.scissors.image, self.scissors.rect)
                self.scissors.update_p2()
            self.window.blit(self.winner_p2.image,(150,50))
        if winner[0]["draw"] == "yes" and winner[1]["draw"] == "yes":
            if winner[0]["p1_move"] == "rock":
                self.window.blit(self.rock.image, self.rock.rect)
                self.rock.update_p1()
            if winner[0]["p1_move"] == "paper":
                self.window.blit(self.paper.image, self.paper.rect)
                self.paper.update_p1()
            if winner[0]["p1_move"] == "scissors":
                self.window.blit(self.scissors.image, self.scissors.rect)
                self.scissors.update_p1()
            if winner[1]["p2_move"] == "rock":
                self.window.blit(self.rock.image, self.rock.rect)
                self.rock.update_p2()
            if winner[1]["p2_move"] == "paper":
                self.window.blit(self.paper.image, self.paper.rect)
                self.paper.update_p2()
            if winner[1]["p2_move"] == "scissors":
                self.window.blit(self.scissors.image, self.scissors.rect)
                self.scissors.update_p2()
            self.window.blit(self.tie.image,(150,50))
        self.window.blit(self.play_again.image,  (150, 400))
        self.window.blit(self.menu.image, (150, 510))
        self.window.blit(self.timer.image, (20,20))
    
    def update(self):
        """
        Updates the timer. Timer counts down from 15. Once timer reaches zero, goes back to the welcome screen.
        """
        now = pygame.time.get_ticks()
        if self.running == True:
            if now - self.start_time > 15000:
                print("Inactive for more than 15 seconds. Returning to main menu.")
                self.next_screen = "welcome"
                self.running = False
        self.timer = TextBox((50,50), str(round(15-(now - self.start_time)/1000,1)),color = (255,255,255), bgcolor=(0,0,0))

 

    def manage_event(self, event):
        """
        Changes the screen if the player clicks on the play again, go back to main menu textboxes.

        Args:
            event (_type_): MOUSEBUTTONDOWN event in pygame
        """
        if event.type == pygame.MOUSEBUTTONDOWN: 
            print(event.pos[0])
            if 100 < event.pos[0] < 450 and 400 < event.pos[1] < 470:
                self.next_screen ="game_pvp"
                self.running = False
            if 100 < event.pos[0] < 450 and 510 < event.pos[1] < 590:
                self.next_screen ="welcome"
                self.running = False
       