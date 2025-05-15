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
    # THIS PART IS SOLVED FOR THE LOLS Please dont take it seriously
    result = 0
    num_names = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
    }

    with open(FILENAME, "r") as f:
        data = f.read().split()

    # find first letter from the left
    for line in data:
        found_left = [None, None]
        for k in num_names.keys():
            match = line.find(k)

            if match == -1:
                continue

            if found_left[0] is None or found_left[0] > match:
                found_left[0] = match
                found_left[1] = k

        found_right = [None, None]
        for k in num_names.keys():
            match = line[::-1].find(k[::-1])

            if match == -1:
                continue

            if found_right[0] is None or found_right[0] > match:
                found_right[0] = match
                found_right[1] = k

        result += int(num_names[found_left[1]] + num_names[found_right[1]])

    return result


def find_sub_string(stringA, stringB):
    # match stringB to stringA
    lenA = len(stringA)
    lenB = len(stringB)
    for i, _ in enumerate(stringA):
        if (i + lenB) > lenA:
            break

        if stringB == stringA[i:lenB]:
            return i, stringB

    return None


def main():

    if len(sys.argv) < 2:
        return

    result = 0

    if sys.argv[1] == "1":
        result = part1()

    if sys.argv[1] == "2":
        result = part2()

    print(f"Solution for Part {sys.argv[1]}: {result}")


if __name__ == "__main__":
    main()
