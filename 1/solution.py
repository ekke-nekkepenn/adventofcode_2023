import sys


FILENAME = "input.txt"

def convert_file():
    left = []
    right = []
    with open(FILENAME, "r") as f:
        for i, e in enumerate(f.read().split()):
            if i % 2 == 0:
                left.append(int(e))
            else:
                right.append(int(e))
    return left, right
 
def part1():
    result = 0
    # first convert the input to something more useful
    left, right = convert_file()
               
    left = sorted(left)
    right = sorted(right)
    for i, e in enumerate(left):
        result += abs(left[i] - right[i])

    return result


def part2():
    result = 0
    left, right = convert_file()
    # frequency of element in "left" in "right"
    frequency = {k:0 for k in left}
    for i in right:
        try:
            frequency[i] += 1
        except KeyError:
            continue

    for i in left:
        result += i * frequency[i]
    
    return result




def main():
    result = 0
    
    if len(sys.argv) < 2:
        print(f"python {sys.argv[0]} (1) or (2)")
        return

    if sys.argv[1] == '1':
        result = part1()

    elif sys.argv[1] == '2':
        result = part2()

    else:
        print(f"python {sys.argv[0]} (1) or (2)")
        return

    print(f"Solution for part {sys.argv[1]}: {result}")



if __name__ == "__main__":
    main()
