import pygame
from screens import BaseScreen
from components import TextBox
# from components .text import render_text,center_text


#for player 1?
class Username(BaseScreen):
    def __init__(self,window,state):
        """Screen for when the player chooses a username for the vs. computer game mode"""
        super().__init__(window,state)
        self.json_file = "data/initial_user.json"
        self.type = TextBox((300,80), "Type your username", bgcolor=(250,235,215))
        self.luck = TextBox((600,80), "Test your luck against the computer!",color=(255,255,255) ,bgcolor=(0,0,0))
        self.upload = TextBox((600,80), "Your score will be uploaded to the leaderboard",color=(255,255,255) ,bgcolor=(0,0,0))
        self.max_characters = TextBox((300,80), "8 letters max", bgcolor=(250,235,215))
        self.state["name"] = ""
        self.state["score"] = 0
        self.time_limit=pygame.time.get_ticks()

    def draw(self):
        """Displays text and images to the window"""
        self.window.fill((0,0,0))
        self.window.blit(self.type.image,(150,50))
        self.window.blit(self.max_characters.image,(150,130))
        self.window.blit(self.user_input.image,(150,500))
        self.window.blit(self.luck.image,(0, 275))
        self.window.blit(self.upload.image,(0,350))
        

    def update(self):
        """Writes the user's name as they type it onto the screen"""
        self.user_input = TextBox((300,80), f"{self.state['name']}", bgcolor=(250,235,215))


    def manage_event(self, event):
        """
        Appends the user's keyboard input to the state attribute. Only takes lowercase and uppercase letters in the alphabet. If a user presses backspace, removes the last letter the user typed. If the user types 8 characters, or presses the return button, the screen moves game_cpu.

        Args:
            event (_type_): KEYDOWN event pygame
        """
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_BACKSPACE:
                self.state["name"] = self.state["name"][:-1]
            else:
                if event.key in range(pygame.K_a, pygame.K_z + 1):
                    self.state["name"] += str(event.unicode)
            if len(self.state["name"]) >= 1:
                if len(self.state["name"]) >= 8 or event.key == pygame.K_RETURN:
                    self.next_screen = "cpu"
                    self.running = False
       
