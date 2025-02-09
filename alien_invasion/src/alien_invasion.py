"""Dependencies"""

import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        # Initialize the clock to control frame rate.
        self.clock = pygame.time.Clock()

        # Call settings
        self.settings = Settings()

        # Set dimensions of game window, (wide, high).
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        # Set window name.
        pygame.display.set_caption("Alien Invasion")

        # Call ship class
        self.ship = Ship(self)

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)

        # Draw the ship in the screen
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def run_game(self):
        """Start the main loop for the game"""

        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            # Redraw the screen during each pass through the loop.
            self._update_screen()
            # Frame rate, run exactly 60 times per second.
            self.clock.tick(60)


if __name__ == "__main__":

    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
