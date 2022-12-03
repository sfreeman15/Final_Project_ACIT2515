import pygame
from screens import BaseScreen
from components import TextBox, Rock, Paper, Scissors
# from components .rock import Rock
# from components .paper import Paper
# from components .scissors import Scissors



class WelcomeScreen(BaseScreen):
    def __init__(self,window,state):
        """Screen for main menu of Rock Paper Scissors Game"""
        super().__init__(window,state)
        self.title = TextBox((300,80), "Rock Paper Scissors", bgcolor=(250,235,215))
        self.play = TextBox((200,80), "Play", bgcolor=(250,235,215))
        self.rock = Rock()
        self.paper = Paper()
        self.scissors = Scissors()
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.rock)
        self.sprites.add(self.paper)
        self.sprites.add(self.scissors)

      
    def draw(self):
        """Displays text and images to the window"""
        self.window.fill((0,0,0))
        self.window.blit(self.title.image,(150,50))
        self.window.blit(self.play.image, (200, 190))
        self.window.blit(self.rock.image, self.rock.rect)
        self.window.blit(self.paper.image, self.paper.rect)
        self.window.blit(self.scissors.image, self.scissors.rect)

    def update(self):
        """Calls the update functions of each sprite class"""
        self.sprites.update()

    def manage_event(self, event):
        """
        Changes the screen if the player clicks on the play button textbox.

        Args:
            event (_type_): MOUSEBUTTONDOWN event in pygame
        """
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if 200 < event.pos[0] < 400 and 190 < event.pos[1] < 270:
                self.next_screen ="game_mode"
                self.running = False

