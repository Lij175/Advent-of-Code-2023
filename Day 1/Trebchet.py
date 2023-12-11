

def main():
    with open('Day 1\calibration document.txt') as doc:
        doc = doc.readlines()
        doc[-1] += '\n'

    print(part1(doc))
    print(part2(doc))


def part2(doc):
    valid_digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    value = 0
    digit3 = 'one two six ten'
    digit4 = 'four five nine'
    digit5 = 'three seven eight'
    for line in doc:
        first = 0
        second = 0
        while True:
            if line[0] in '1234567890':
                first = int(line[0])
                break
            elif line[0:3] in digit3:
                first = valid_digits[line[0:3]]
                break
            elif line[0:4] in digit4:
                first = valid_digits[line[0:4]]
                break
            elif line[0:5] in digit5:
                first = valid_digits[line[0:5]]
                break
            line = line[1:]
        
        while len(line) > 0:
            if line[0:3] in digit3:
                second = valid_digits[line[0:3]]
            elif line[0:4] in digit4:
                second = valid_digits[line[0:4]]
            elif line[0:5] in digit5:
                second = valid_digits[line[0:5]]
            elif line[0] in '1234567890':
                second = int(line[0])
            line = line[1:]
        
        value += first * 10 + second
    
    return value
        



def part1(doc):
    value = 0
    for line in doc:
        line_value = 0
        for digit in line:
            if digit in '1234567890':
                line_value = int(digit) * 10
                break
        for i in range(len(line)-1, -1, -1):
            if line[i] in '1234567890':
                line_value += int(line[i])
                break
        value += line_value
    
    return value


if __name__ == "__main__":
    main()