def main():
    #only 12 red cubes, 13 green cubes, and 14 blue cubes
    with open('Day 2\\full game.txt') as doc:
        doc = doc.readlines()

    part1(doc)
    part2(doc)
    

def part1(doc):
    bag = {'red': 12, 'green': 13, 'blue': 14}
    
    game_ID = int((len(doc) * (1 + len(doc))) / 2)
    for line in doc:
        line = line.strip()
        game = game_obj(line)
        breaked = False
        for draw in game.get_draws():
            # print(draw)
            for key, value in draw.items():
                if value > bag[key]:
                    # print(game.get_num())
                    game_ID -= game.get_num()
                    breaked = True
                    break
            if breaked:
                break
        # print()
    
    print(game_ID)


def part2(doc):
    power = 0
    for line in doc:
        line = line.strip()
        game = game_obj(line)
        bag = {'red': 0, 'green': 0, 'blue': 0}
        for draw in game.get_draws():
            # print(draw)
            for key, value in draw.items():
                if value > bag[key]:
                    bag[key] = value
        power += bag['red'] * bag['green'] * bag['blue']
        # print(bag['red'] * bag['green'] * bag['blue'])
    
    print(power)


class game_obj:
    def __init__(self, game_info):
        self.num = int(game_info.split(':')[0][5:])
        self.draws = game_info.split(':')[1].split('; ')
        for i in range(len(self.draws)):
            plays = self.draws[i].split(', ')
            self.draws[i] = dict()
            for play in plays:
                play = play.split()
                self.draws[i][play[1]] = int(play[0])

    def get_num(self):
        return self.num
    
    def get_draws(self):
        return self.draws

if __name__ == "__main__":
    main()