class Solution:
    def solve_part_one(data):
        total = 0
        for line in data:
            total += Solution.find_winnings_in_(line)

        print(total)

    def format_(line) -> tuple[list[str], list[str]]:
        line = line.split(": ")[1]
        winning_nums, your_nums = line.split(" | ")
        winning_nums = winning_nums.split()
        your_nums = your_nums.split()
        return winning_nums, your_nums

    def find_winnings_in_(line) -> int:
        # first format the input to use it
        # Card 1: n1 n2 ...  | m1 m2 ...
        winning_nums, your_nums = Solution.format_(line)
        winnings = 0
        exp = 0
        for n in your_nums:
            if n in winning_nums:
                winnings = 2**exp
                exp += 1

        return winnings

    def solve_part_two(data):
        ...
        # find total number of scratchcards
        # for each winnning number on scratchcards copy subsequent scratchcards up to won numbers
        # card 1 has 3 winning numbers copy card 2 3 4 each 3


with open("input") as file:
    data = file.read().splitlines()

Solution.solve_part_one(data)
# Solution.solve_part_two(data)
