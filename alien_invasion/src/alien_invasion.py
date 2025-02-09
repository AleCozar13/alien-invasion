"""Dependencies"""

import sys
import pygame


class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        # Initialize the clock to control frame rate.
        self.clock = pygame.time.Clock()
        # Set dimensions of game window, (wide, high).
        self.screen = pygame.display.set_mode((1200, 800))
        # Set window name.
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game"""

        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                # Make the most recently drawn screen visible.
                pygame.display.flip()

                # Frame rate, run exactly 60 times per second.
                self.clock.tick(60)


if __name__ == "__main__":

    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
