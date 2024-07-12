class Settings:
    # A class to store all setting for game

    def __init__(self):
        # Initialize the game's Setting.

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
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        
        #fleet_direction of 1 repesent right; -1 represent left.
        self.fleet_direction = 1