import pygame
import webbrowser
import json
from .base_screen import BaseScreen
from components .text_box import TextBox
from components .text import render_text,center_text
from subprocess import Popen



#for player 2?
class GameOver(BaseScreen):
    def __init__(self,window,state,filename = "data/score.json"):
        super().__init__(window,state)
        self.clock = pygame.time.Clock()
        self.time_counter = 0
        self.filename = filename
        self.final_score = self.state.values()
        with open (filename, "r") as f:
            contents = json.load(f)
        self.username = TextBox((300,80), f"{self.state['name']}",color=(255,255,255), bgcolor=(0,0,0))
        self.game_over = TextBox((300,80), "Game Over!", bgcolor=(250,235,215))
        self.play_again = TextBox((300,80), "Play again?", bgcolor=(250,235,215))
        self.final_score = TextBox((300,80), f"Your final score is: {self.state['score']}! ",color=(255,255,255), bgcolor=(0,0,0))
        self.menu = TextBox((300,80), "Go back to menu?", bgcolor=(250,235,215))
        self.start_time = pygame.time.get_ticks()
        self.flask = TextBox((300,80), "High scores on Flask", bgcolor=(250,235,215))
        



    def draw(self):
        self.window.fill((0,0,0))
        self.window.blit(self.game_over.image,(150,50))
        self.window.blit(self.username.image, (150,175))
        self.window.blit(self.final_score.image,(150,250))
        self.window.blit(self.play_again.image,  (150, 400))
        self.window.blit(self.menu.image, (150, 510))
        self.window.blit(self.timer.image, (20,20))
        self.window.blit(self.flask.image,(150,500))
     

    def update(self):
        now = pygame.time.get_ticks()
        # self.time_counter = self.clock.tick()
        if self.running == True:
            if now - self.start_time > 15000:
                print("Inactive for more than 15 seconds. Returning to main menu.")
                self.next_screen = "welcome"
                self.running = False
        self.timer = TextBox((50,50), str(round(15-(now - self.start_time)/1000,1)), color = (255,255,255), bgcolor=(0,0,0))
        
        


    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN: 
            print(event.pos[1])
            if 100 < event.pos[0] < 450 and 400 < event.pos[1] < 470:
                self.next_screen ="cpu"
                self.running = False
                self.state["score"] = 0
            if 100 < event.pos[0] < 450 and 510 < event.pos[1] < 590:
                self.next_screen ="welcome"
                self.running = False
            if 100 < event.pos[0] < 450 and 500 < event.pos[1] < 570:
                # self.next_screen = "welcome"
                # self.running = False
                Popen("python app.py")
                webbrowser.open('http://127.0.0.1:5000')
               
                
            

    