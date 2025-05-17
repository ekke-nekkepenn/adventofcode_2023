import sys

FILENAME = "input.txt"


def remove_left_side(char, string):
    for i, c in enumerate(string):
        if c == char:
            if (i + 1) < len(string):
                return string[(i + 1) :]
    return string

def format_text(text: str):
    data = [remove_left_side(":", s).split(";") for s in text.splitlines()]
    for line in data:
        for i, pull in enumerate(line):
            line[i] = [sp.split() for sp in pull.split(",")]
    return data
 

def part1():
    result = 0

    with open(FILENAME, "r") as f:
        text = f.read()

    # FORMAT DATA
    data = format_text(text)
    # above
    # turns this -> "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

    # into this -> [ LINE
    #                   [ PULL
    #                       BALL       BALL
    #                       [3, blue], [4, red]
    #                   ],
    #                   [
    #                       [1, red], [2, green], [6, blue]
    #                   ],
    #                   [
    #                       [2, green]
    #                   ],
    #                   ]
    #              ]

    MAX_RED = 12
    MAX_GREEN = 13
    MAX_BLUE = 14

    for i, line in enumerate(data):
        for pull in line:
            r = 0
            g = 0
            b = 0
            for ball in pull:
                if ball[1] == "red":
                    r += int(ball[0])
                elif ball[1] == "green":
                    g += int(ball[0])
                if ball[1] == "blue":
                    b += int(ball[0])

            if r > MAX_RED or g > MAX_GREEN or b > MAX_BLUE:
                break

        # for loop else clause only happens if no break happend in the loop
        else:
            result += (i + 1)

    return result


def part2():
    result = 0
    with open(FILENAME, "r") as f:
        text = f.read()
    
    data = format_text(text)

    for line in data:
        r = b = g = 0
        for pull in line:
            for ball in pull:
                curb = int(ball[0])
                if ball[1] == "red":
                    r = curb if curb > r else r

                elif ball[1] == "green":
                    g = curb if curb > g else g
                
                elif ball[1] == "blue":
                    b = curb if curb > b else b

        result += r * g* b

    return result


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
