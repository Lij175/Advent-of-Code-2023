class game:
    def __init__(self, game):
        self.game_num = int(game[5])
        self.draws = game[8].split('; ')

    def getGameNum(self):
        return self.game_num
    
    def getDraws(self):
        return self.draws
    
    def __str__(self):
        return f'Game {1}: {"; ".join(self.draws)}'
