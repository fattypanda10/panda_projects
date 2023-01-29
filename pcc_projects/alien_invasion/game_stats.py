class GameStats:
    def __init__(self, ai_game):
        self.level = None
        self.score = None
        self.ships_left = None
        self.settings = ai_game.settings
        self.game_active = False
        self.high_score = 0
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
