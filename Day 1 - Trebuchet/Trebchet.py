

def main():
    with open('Day 1 - Trebuchet\\calibration document.txt') as doc:
        doc = doc.readlines()
        doc[-1] += '\n'
   
    print(part1(doc))
    print(part2(doc))

    # Initialize the sum of calibration values
    total_calibration_sum = 0
    # Iterate through each line in the calibration document
    for line in doc:
        # Extract the calibration value for the current line
        calibration_value = extract_calibration_values(line)

        # Add the calibration value to the total sum
        total_calibration_sum += calibration_value
    
    print(total_calibration_sum)


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

def is_digit(char):
    # Check if the character is a digit
    return '0' <= char <= '9'

def extract_calibration_values(line):
    # Find the first digit in the line
    for char in line:
        if is_digit(char):
            first_digit = int(char)
            break

    # Find the last digit in the line
    for char in line[::-1]:
        if is_digit(char):
            last_digit = int(char)
            break

    # Combine the first and last digits to form a two-digit number
    calibration_value = first_digit * 10 + last_digit
    return calibration_value


if __name__ == "__main__":
    main()

