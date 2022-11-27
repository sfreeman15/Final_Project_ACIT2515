import pygame
from .base_screen import BaseScreen
from components .text_box import TextBox
from components .text import render_text,center_text



class WelcomeScreen(BaseScreen):
    def __init__(self,window):
        super().__init__(window)
        print("Welcome screen is being called")
        self.title = TextBox((300,80), "Rock Paper Scissors", bgcolor=(250,235,215))
        self.play = TextBox((200,80), "Play", bgcolor=(250,235,215))
        # self.play_outer= TextBox((200,100),bgcolor=(0,0,0))
        self.rules = TextBox((200,80), "Rules", bgcolor=(250,235,215))
        self.commands = TextBox((200,80), "Commands", bgcolor=(250,235,215))



    def draw(self):
        self.window.fill((69,139,0))
        # self.window.blit(self.play_outer.image, (200, 300))
        # center_text(self.title, (200, 50))
        self.window.blit(self.title.image,(150,50))
        self.window.blit(self.play.image, (200, 190))
        self.window.blit(self.rules.image,  (200, 300))
        self.window.blit(self.commands.image, (200, 410))
    

    def update(self):
        pass

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN: 
            # if 440 < event.pos[0] < 500 and 0 < event.pos[1] < 60:
            if 150 < event.pos[0] < 350 and 190 < event.pos[1] < 270:
                self.next_screen ="game_p1"
                self.running = False

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
