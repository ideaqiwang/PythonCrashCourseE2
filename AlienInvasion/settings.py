class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        # Screen settings
        self.screen_width = 600
        self.screen_height = 650
        self.bg_color = (230, 230, 230)
        
        # Ship settings
        self.ship_speed = 5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 20

        # Alien settings
        self.alien_speed = 10.0
        self.fleet_drop_speed = 30

        # 1 -> right, -1 -> left
        self.fleet_direction = 1