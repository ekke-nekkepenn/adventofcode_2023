import sys

FILENAME = "input.txt"

def part1():
    result = 0
    return result

def part2():
    result = 0
    return result

def main():

    if len(sys.argv) < 2:
        return

    result = 0
    
    if sys.argv[1] == '1':
        result = part1()

    if sys.argv[1] == '2':
        result = part1()

    print(f"Solution for Part {sys.argv[1]}: {result}")


if __name__ == "__main__":
    main()