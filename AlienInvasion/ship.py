import pygame

class Ship:
    def __init__(self, ai_game):
        """Initialize the ship and set the starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.screen_rect = self.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the ship at its current locations."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed