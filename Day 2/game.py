class game:
    def __init__(self, game_info):
        self.num = int(game_info[5])
        self.draws = game_info[8:].split('; ')

    def get_num(self):
        return self.num
    
    def get_draws(self):
        return self.draws
    
    def __str__(self):
        return f'Game {self.num}: {"; ".join(self.draws)}'