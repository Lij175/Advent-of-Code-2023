

def main():
    with open('Day 1\calibration document.txt') as doc:
        doc = doc.readlines()

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
    
    print(value)


if __name__ == "__main__":
    main()