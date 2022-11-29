import pygame
from .base_screen import BaseScreen
from components .text_box import TextBox
from components .rock import Rock
from components .paper import Paper
from components .scissors import Scissors



class WelcomeScreen(BaseScreen):
    def __init__(self,window):
        super().__init__(window)
        self.title = TextBox((300,80), "Rock Paper Scissors", bgcolor=(250,235,215))
        self.play = TextBox((200,80), "Play", bgcolor=(250,235,215))
        self.rock = Rock()
        self.paper = Paper()
        self.scissors = Scissors()
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.rock)
        self.sprites.add(self.paper)
        self.sprites.add(self.scissors)

        # self.play_outer= TextBox((200,100),bgcolor=(0,0,0))
        # self.rules = TextBox((200,80), "Rules", bgcolor=(250,235,215))
        # self.commands = TextBox((200,80), "Commands", bgcolor=(250,235,215))
    def draw(self):
        self.window.fill((0,0,0))
        # self.window.blit(self.play_outer.image, (200, 300))
        # center_text(self.title, (200, 50))
        self.window.blit(self.title.image,(150,50))
        self.window.blit(self.play.image, (200, 190))
        # self.window.blit(self.rules.image,  (200, 300))
        # self.window.blit(self.commands.image, (200, 410))
        self.window.blit(self.rock.image, self.rock.rect)
        self.window.blit(self.paper.image, self.paper.rect)
        self.window.blit(self.scissors.image, self.scissors.rect)

    def update(self):
        self.sprites.update()

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN: 
            print(event.pos[0])
            # if 440 < event.pos[0] < 500 and 0 < event.pos[1] < 60:
            if 200 < event.pos[0] < 400 and 190 < event.pos[1] < 270:
                self.next_screen ="game_mode"
                self.running = False

