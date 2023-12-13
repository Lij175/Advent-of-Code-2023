def main():
    with open('Day 3 - Gear Ratios\\smol schematic.txt') as doc:
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
    
    for line in schematic:
        print(''.join(line))
    
    part1(schematic)
    #part2(schematic)


def part2(schematic):
    schemadictionary = dict() # key: 'row:col' <> value: [symbol, 0: '.' -1: '*', -2: num(temporary)]
    for row in range(len(schematic)):
        for col in range(len(schematic[row])):
            curr = schematic[row][col]
            schemadictionary[f'{row}:{col}'] = 0
    

    num = 0
    num_loc = list()
    for row in range(len(schematic)):
        for col in range(len(schematic[row])):
            if schematic[row][col] in '1234567890':
                num = num * 10 + int(schematic[row][col])
                num_loc.append([row, col])
            elif num != 0:
                for index in num_loc:
                    row, col = index
                    schemadictionary[f'{row}:{col}'] = num
                num = 0
                num_loc.clear()
    '''
    for row in range(len(schematic)):
        for col in range(len(schematic[row])):
            print(schematic[row][col], end= '')
        print()
    '''
    
    sum = 0
    for row in range(len(schematic)):
        for col in range(len(schematic[row])):
            if schematic[row][col] == '*':
                sum += find_gear_ratio([row,col], schemadictionary)
    
    print(sum)
            

def find_gear_ratio(loc, schemadictionary):
    nums = []
    row, col = loc
    nums.append(schemadictionary[f'{row-1}:{col-1}'])
    if schemadictionary[f'{row-1}:{col}'] != schemadictionary[f'{row-1}:{col-1}']:
        nums.append(schemadictionary[f'{row-1}:{col}'])
    if schemadictionary[f'{row-1}:{col+1}'] != schemadictionary[f'{row-1}:{col}']:
        nums.append(schemadictionary[f'{row-1}:{col+1}'])

    nums.append(schemadictionary[f'{row}:{col-1}'])
    nums.append(schemadictionary[f'{row}:{col+1}'])
    
    nums.append(schemadictionary[f'{row+1}:{col-1}'])
    if schemadictionary[f'{row+1}:{col}'] != schemadictionary[f'{row+1}:{col-1}']:
        nums.append(schemadictionary[f'{row+1}:{col}'])
    if schemadictionary[f'{row+1}:{col+1}'] != schemadictionary[f'{row+1}:{col}']:
        nums.append(schemadictionary[f'{row+1}:{col+1}'])
    
    nums2 = []
    for num in nums:
        if num != 0:
            nums2.append(num)

    if len(nums2) > 2 or len(nums2) < 2:
        return 0
    else:
        ratio = 1
        for num in nums2:
            ratio *= num
        # print(ratio)
        return ratio
    

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