import pygame

from screens.welcome_screen import WelcomeScreen
from screens.game_pvp import GameScreenPVP
from screens.winner_p1 import ResultsP1
from screens.winner_p2 import ResultsP2
from screens.game_mode import GameMode
from screens.draw import Draw





class Game:
    """Main class for the application"""

    def __init__(self):
        # Creates the window
        self.window = pygame.display.set_mode((600, 600))
        print("rps screen is being called")
        

    def run(self):
        """Main method, manages interaction between screens"""

        # These are the available screens
        screens = { #dictionary with indicator of screens, with instance of classes from the other files
            "game_pvp": GameScreenPVP,
            "welcome": WelcomeScreen,
            "winner_p1": ResultsP1,
            "winner_p2": ResultsP2,
            "game_mode": GameMode,
            "draw": Draw
           
            # "game_over": GameOverScreen,
        }
        # Start the loop
        center = self.window.get_rect().center
        running = True
        current_screen = "welcome"
        while running:
            
            # Obtain the screen class
            screen_class = screens.get(current_screen)
            if not screen_class:
                raise RuntimeError(f"Screen {current_screen} not found!")

            # Create a new screen object, "connected" to the window
            screen = screen_class(self.window)
            # Run the screen
            screen.run()
            # When the `run` method stops, we should have a `next_screen` setup
            if screen.next_screen is False:
                running = False
            # Switch to the next screen
            current_screen = screen.next_screen


if __name__ == "__main__":
    rps = Game()
    rps.run()
