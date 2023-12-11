def main():
    with open('Day 2\game.txt') as doc:
        doc = doc.readlines()
        doc[-1] += '\n'
    
    for line in doc:
        game = game(line)
        print(game)


if __name__ == "__main__":
    main()