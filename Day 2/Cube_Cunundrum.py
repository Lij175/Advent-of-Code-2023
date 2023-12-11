import game

def main():
    # the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes
    with open('Day 2\\test game.txt') as doc:
        doc = doc.readlines()
        doc[-1] += '\n'
    
    for game in doc:
        pass


if __name__ == "__main__":
    main()