def main():
    with open('Day 3 - Gear Ratios\smol schematic.txt') as doc:
        doc = doc.readlines()
    schematic = []
    for line in doc:
        line.strip()
        list_of_line = []
        for symbol in line:
            list_of_line.append(symbol)
        schematic.append(list_of_line)
    
def get_surrounding(number, schematic):
    '''
    numer in format of ((1,2), (1,3), (1,4)). ie. indexs of number
    '''
    num_rows = len(schematic)
    num_cols = len(schematic[0])
    if number[0][0] == 0 and number[0][1] == 0:
        # top left
        pass
    elif number[-1][0] == 0 and number[-1][1] == num_cols - 1:
        # top right
        pass
    elif number[0][0] == num_rows - 1 and number[0][1] == 0:
        # bottom left
        pass
    elif number[-1][0] == num_rows - 1 and number[-1][1] == num_cols - 1:
        # bottom right
        pass
    elif number[0][0] == 0:
        # top row
        pass
    elif number[0][0] == num_rows - 1:
        # bottom row
        pass
    elif number[0][1] == 0:
        # left col
        pass
    elif number[-1][1] == num_cols - 1:
        # right col
        pass


if __name__ == "__main__":
    main()