"""
Atanas Delevski
12/21/2022
Advent of Code 2022 - Day 7
"""


def part_one(lines):
    d = {}
    for line in lines:
        x = line[:-2]
        parts = x.split(' ')
        print(parts)


def part_two(lines):
    print(lines)


def main():
    file_path = 'data/day7.txt'
    file = open(file_path, 'r')
    lines = file.readlines()

    # Part 1
    part_one_answer = part_one(lines)

    # Part 2 
    # part_two_answer = part_two(lines)

    # Print
    print(f"Part 1: {part_one_answer}")
    # print(f"Part 2: {part_two_answer}")


if __name__ == "__main__":
    main()