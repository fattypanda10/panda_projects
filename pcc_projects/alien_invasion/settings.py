class Settings:
    def __init__(self):
        # screen settings
        self.alien_points = None
        self.alien_speed = None
        self.bullet_speed = None
        self.ship_speed = None
        self.fleet_direction = None
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_limit = 3

        # bullet settings
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # alien settings
        self.fleet_drop_speed = 10

        # speed scaling
        self.speedup_scale = 1.1

        # score scaling with increasing levels
        self.score_scale = 1.5

        # dynamic settings
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5  # in pixels
        self.bullet_speed = 1.5
        self.alien_speed = 1.0
        self.fleet_direction = 1
        # alien hit points
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
