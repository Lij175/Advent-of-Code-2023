def main():
    with open('Day 4 - Scratchcards\Small cards.txt') as doc:
        doc = doc.readlines()

    for i in range(len(doc)):
        doc[i] = doc[i].strip()
    
    part1(doc)

def part2(doc):
    pass
    
def part1(doc):
    overall_score = 0
    for card in doc:
        card_score = 0
        first = True
        winning = card[card.index(':') + 1: card.index('|')].split()
        numbers = card[card.index('|') + 1:].split()
        #print(winning, ' | ', numbers)
        for num in numbers:
            if num in winning:
                if first:
                    card_score = 1
                    first = False
                else:
                    card_score = card_score * 2

        overall_score += card_score
    
    print(overall_score)



if __name__ == "__main__":
    main()