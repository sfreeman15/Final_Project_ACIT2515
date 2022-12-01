import pygame
import json
from .base_screen import BaseScreen
from components .text_box import TextBox
from components .text import render_text,center_text



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
        self.game_over = TextBox((300,80), "Game Over!", bgcolor=(250,235,215))
        self.play_again = TextBox((300,80), "Play again?", bgcolor=(250,235,215))
        self.final_score = TextBox((400,80), f"Your final score is: {self.state['score']}! ", bgcolor=(250,235,215))
        self.menu = TextBox((300,80), "Go back to menu?", bgcolor=(250,235,215))
        self.start_time = pygame.time.get_ticks()
        



    def draw(self):
        self.window.fill((0,0,0))
        self.window.blit(self.game_over.image,(150,50))
        self.window.blit(self.final_score.image,(100,175))
        self.window.blit(self.play_again.image,  (150, 400))
        self.window.blit(self.menu.image, (150, 510))
        self.window.blit(self.timer.image, (20,20))
     

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
            if 100 < event.pos[0] < 450 and 510 < event.pos[1] < 590:
                self.next_screen ="welcome"
                self.running = False
    