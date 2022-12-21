"""
Atanas Delevski
12/20/2022
Advent of Code 2022 - Day 4 (Part I & II?)
"""


def part_one(lines):
    ans = 0
    for line in lines:
        f, s = line.split(',')
        f_f, f_s = [int(x) for x in f.split('-')]
        s_f, s_s = [int(x) for x in s.split('-')]
        if (s_f <= f_f <= s_s) and (s_f <= f_s <= s_s):
            ans += 1
        elif (f_f <= s_f <= f_s) and (f_f <= s_s <= f_s):
            ans += 1
    return ans


def part_two(lines):
    ans = 0
    for line in lines:
        f, s = line.split(',')
        f_f, f_s = [int(x) for x in f.split('-')]
        s_f, s_s = [int(x) for x in s.split('-')]
        if (s_s < f_f) or (s_f > f_s):
            continue
        else:
            ans += 1
    return ans


def main():
    # Init
    file_path = 'data/day4.txt'
    file = open(file_path, "r")
    lines = file.readlines()

    # Part 1:
    part_one_answer = part_one(lines)

    # Part 2:
    part_two_answer = part_two(lines)

    # Printing
    print(f"Part 1: {part_one_answer}")
    print(f"Part 2: {part_two_answer}")


if __name__ == "__main__":
    main()