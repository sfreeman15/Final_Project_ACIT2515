import pygame
from .base_screen import BaseScreen
from components .text_box import TextBox
from components .text import render_text,center_text


#for player 1?
class GameScreenPVP(BaseScreen):
    def __init__(self,window):
        super().__init__(window)
        self.move_p1 = ""
        self.move_p2 = ""
        print("GameScreen is being called")
        self.title = TextBox((300,80), "Choose your move!", bgcolor=(250,235,215))
        self.player2_turn = TextBox((300,80), "Player 2's turn!", bgcolor=(250,235,215))
     
        self.time_limit=pygame.time.get_ticks()

    def draw(self):
        self.window.fill((69,139,0))
        # self.window.blit(self.play_outer.image, (200, 300))
        # center_text(self.title, (200, 50))
        self.window.blit(self.title.image,(150,50))
        
        
    def update(self):
        pass

    def game_logic(self):
        if self.move_p1 == "rock" and self.move_p2 == "scissors":
                self.next_screen = "winner_p1"
                self.running = False
        elif self.move_p1 == "paper" and self.move_p2 == "rock":
            self.next_screen = "winner_p1"
            self.running = False
        elif self.move_p1 == "scissors" and self.move_p2 == "paper":
            self.next_screen = "winner_p1"
            self.running = False
        elif self.move_p2 == "rock" and self.move_p1 == "scissors":
                self.next_screen = "winner_p2"
                self.running = False
        elif self.move_p2 == "paper" and self.move_p1 == "rock":
            self.next_screen = "winner_p2"
            self.running = False
        elif self.move_p2 == "scissors" and self.move_p1 == "paper":
            self.next_screen = "winner_p2"
            self.running = False
        elif self.move_p1 == self.move_p2:
            self.next_screen = "draw"
            self.running = False




    
    def manage_event(self, event):
        if event.type == pygame.KEYDOWN:   
            if pygame.key.name(event.key) == "q":
                self.move_p1 = "rock"
                print(self.move_p1)
                GameScreenPVP.game_logic(self)
                # self.next_screen ="game_p2"
            if pygame.key.name(event.key) == "w":
                self.move_p1 = "paper"
                print(self.move_p1)
                GameScreenPVP.game_logic(self)
                # self.next_screen ="game_p2"
                # self.running = False
            if pygame.key.name(event.key) == "e":
                self.move_p1 = "scissors"
                print(self.move_p1)
                GameScreenPVP.game_logic(self)
            if pygame.key.name(event.key) == "i":
                self.move_p2 = "rock"
                print(self.move_p2)
                GameScreenPVP.game_logic(self)
            if pygame.key.name(event.key) == "o":
                self.move_p2 = "paper"
                print(self.move_p2)
                GameScreenPVP.game_logic(self)
            if pygame.key.name(event.key) == "p":
                self.move_p2 = "scissors"
                print(self.move_p2)
                GameScreenPVP.game_logic(self)

            



            # if event.key == pygame.K_s:
            #     self.move_pl = "paper"   
            #     print(self.move_p1)
            # if event.key == pygame.K_a:
            #     self.move_p1 = "rock"
            #     print(self.move_p1)
            # if event.key == pygame.K_d:
            #     self.move_pl = "scissors"
            #     print(self.move_p1)
                
            
            

    #need update,
    #manage_events? maybe?


# def main():
#     """Main program"""

#     # Initialize pygame
#     pygame.init()
#     pygame.font.init()
 
#     # Create a window and fill it with a solid color
#     window = pygame.display.set_mode((500, 500))
#     window.fill((100, 0, 100))

#     # Create a Pygame surface, and fill it a solid color
  
#     outer_rectangle1 = pygame.Surface((200, 80)) #creating rectangle
#     outer_rectangle1.fill((0, 0, 0))
#     inner_rectangle1 = pygame.Surface((180, 60))
#     inner_rectangle1.fill((255,255,255))
#     outer_rectangle2 = pygame.Surface((200, 80)) #creating rectangle
#     outer_rectangle2.fill((0, 0, 0))
#     inner_rectangle2 = pygame.Surface((180, 60))
#     inner_rectangle2.fill((255,255,255))
#     outer_rectangle3 = pygame.Surface((200, 80))
#     outer_rectangle3.fill((0, 0, 0))
#     inner_rectangle3 = pygame.Surface((180, 60))
#     inner_rectangle3.fill((255,255,255))
    
#     # Draw a circle in the surface
  
#     # Display the surface in the window
#     window.blit(outer_rectangle1, (150, 300)) #moving my shape
#     window.blit(inner_rectangle1, (160, 310))
#     window.blit(outer_rectangle2, (150, 200)) #moving the mouth of my shape
#     window.blit(inner_rectangle2, (160, 210))
#     window.blit(outer_rectangle2, (150, 400)) #moving the mouth of my shape
#     window.blit(inner_rectangle2, (160, 410))
#     font_play = pygame.font.SysFont('Comic Sans MS', 35)
#     text_play = font_play.render('Play', True, (0, 0, 0))
#     window.blit(text_play, (215,210))
#     font_commands = pygame.font.SysFont('Comic Sans MS', 35)
#     text_commands = font_play.render('Commands', True, (0, 0, 0))
#     window.blit(text_commands, (165,310))
#     font_rules = pygame.font.SysFont('Comic Sans MS', 35)
#     text_rules = font_play.render('Rules', True, (0, 0, 0))
#     window.blit(text_rules, (210,410))

#     # window.blit(surf2, (200, 50))

    


#     # Update the display
#     pygame.display.update()

#     # Event loop
#     running = True
#     while running:
#         clock = pygame.time.Clock()
#         clock.tick(60)
       
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False


# if __name__ == "__main__":
#     main()
