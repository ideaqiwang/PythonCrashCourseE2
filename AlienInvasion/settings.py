class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        # Screen settings
        self.screen_width = 600
        self.screen_height = 650
        self.bg_color = (230, 230, 230)
        
        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 20

        # Alien settings
        self.fleet_drop_speed = 30
        self.speedup_scale = 1.2

        self.init_dynamic_settings()
       

    def init_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 5
        self.bullet_speed = 5
        self.alien_speed = 5

         # 1 -> right, -1 -> left
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale