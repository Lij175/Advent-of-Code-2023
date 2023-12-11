def main():
    #only 12 red cubes, 13 green cubes, and 14 blue cubes
    with open('Day 2\short game.txt') as doc:
        doc = doc.readlines()

    bag = {'red': 12, 'green': 13, 'blue': 14}
    
    game_ID = 0
    for line in doc:
        line = line.strip()
        game = game_obj(line)
        for draw in game.get_draws():
            pass



class game_obj:
    def __init__(self, game_info):
        self.num = int(game_info[5])
        self.draws = game_info[8:].split('; ')
        for i in range(len(self.draws)):
            plays = self.draws[i].split(', ')
            self.draws[i] = dict()
            for play in plays:
                self.draws[i][play[2:]] = int(play[0])



    def get_num(self):
        return self.num
    
    def get_draws(self):
        return self.draws

if __name__ == "__main__":
    main()