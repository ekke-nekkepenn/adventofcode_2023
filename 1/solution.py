import sys

FILENAME = "input.txt"


def part1():
    result = 0

    with open(FILENAME, "r") as f:
        data = f.read().split()

    for row in data:
        num = ""
        for char in row:
            if char.isdigit():
                num += char
                break

        for char in row[::-1]:
            if char.isdigit():
                num += char
                break

        result += int(num)

    return result


def part2():
    result = 0
    num_names = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    with open(FILENAME, "r") as f:
        data = f.read().split()

    return result


def main():

    if len(sys.argv) < 2:
        return

    result = 0

    if sys.argv[1] == "1":
        result = part1()

    if sys.argv[1] == "2":
        result = part1()

    print(f"Solution for Part {sys.argv[1]}: {result}")


if __name__ == "__main__":
    main()
