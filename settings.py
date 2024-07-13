class Settings:
    # A class to store all setting for game

    def __init__(self):
        """Initialize the game's static settings."""

        # Screen Setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #ship setting
        self.ship_speed = 1
        self.ship_limit = 3

        #Bullet Setting
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        #Alien Setting
        self.alien_speed = 1.5
        self.fleet_drop_speed = 10
        
        #fleet_direction of 1 repesent right; -1 represent left.
        self.fleet_direction = 1

        # How quickly the game speeds up.
        self.speedup_scale = 1.1

        # How quickly the alien point values increases.
        self.score_scale = 5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize setting that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction of 1 represent right ; -1 represent left.
        self.fleet_direction = 1

        #Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed setting and alien points values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        