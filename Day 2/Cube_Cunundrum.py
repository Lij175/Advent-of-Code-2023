def main():
    with open('Day 1\calibration document.txt') as doc:
        doc = doc.readlines()
        doc[-1] += '\n'
    
    print(doc)


if __name__ == "__main__":
    main()