def main():
    with open('Day 3 - Gear Ratios\engine schematic.txt') as doc:
        doc = doc.readlines()
    schematic = [['.' for n in range(len(doc[0]) + 1)]]
    for line in doc:
        line = line.strip()
        list_of_line = ['.']
        for symbol in line:
            list_of_line.append(symbol)
        list_of_line.append('.')
        schematic.append(list_of_line)
    schematic.append(['.' for n in range(len(doc[0]) + 1)])
    
    '''
    for line in schematic:
        print(''.join(line))
    '''
    part1(schematic)


def part1(schematic):
    sum = 0
    num = 0
    num_loc = list()
    for row in range(len(schematic)):
        for col in range(len(schematic[row])):
            if schematic[row][col] in '1234567890':
                num = num * 10 + int(schematic[row][col])
                num_loc.append([row, col])
            elif num != 0:
                if(has_adjacent(num_loc, schematic)):
                    #print(num_loc)
                    sum += num
                num = 0
                num_loc.clear()
    
    print(sum)

    
    
def has_adjacent(num_loc, schematic):
    '''
    numer in format of [[1,2], [1,3], [1,4]]. ie. indexs of number
    '''
    
    for index in num_loc:
        row, col = index
        if schematic[row-1][col-1] not in '1234567890.' or schematic[row][col-1] not in '1234567890.' or schematic[row+1][col-1] not in '1234567890.' or\
            schematic[row-1][col] not in '1234567890.' or schematic[row][col] not in '1234567890.' or schematic[row+1][col] not in '1234567890.' or\
            schematic[row-1][col+1] not in '1234567890.' or schematic[row][col+1] not in '1234567890.' or schematic[row+1][col+1] not in '1234567890.':
            return True

    
    return False


if __name__ == "__main__":
    main()