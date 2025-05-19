import sys

FILENAME = "input.txt"

class Schematic:
    def __init__(self, data, size_x, size_y):
        self.data = data
        self.size_x = size_x
        self.size_y = size_y

class Vec:
    def __init__(self, x, y):
        self.x
        self.y

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)


    

def part1():
    result = 0

    with open(FILENAME, "r") as f:
        data = f.read().splitlines()
        schematic = Schematic(data, len(data[0]), len(data))
        print(schematic.data)
    
    for y, line in enumerate(schematic.data):
        for x, c in enumerate(line):
            if c != "*":
                continue

            result += get_nums_around(schematic, x, y)
    return result


def part2():
    result = 0
    return result

def get_nums_around(schematic, x, y):
    result = 0
    up = Vec(0, -1)
    down = Vec(0, 1)
    right = Vec(1, 0)
    left = Vec(-1, 0)




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
