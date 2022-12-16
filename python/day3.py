"""
Atanas Delevski
12/14/2022
Advent of Code 2022 - Day 3 (Parts I & II)
"""


def score_asci(x):
    if 65 <= x <= 90:
        return (x-38)
    else:
        return (x-96)

def part_one(x):
    first, second = x[:len(x)//2], x[len(x)//2:]
    letter_asci = ord([x for x in first if x in second][0])
    return score_asci(letter_asci)
    
def part_two(lines):
    part_two_score = 0
    for i in range(0, len(lines), 3):
        part_two_score += score_asci(ord(list(set(lines[i]) & set(lines[i+1]) & set(lines[i+2]))[0]))
    return part_two_score

def main():
    # Init
    file_path = "data/day3.txt"
    file = open(file_path, "r")
    lines = file.readlines()

    # Part 1
    part_one_score = sum([part_one(line) for line in lines])

    # Part 2
    part_two_score = part_two(lines)

    # Output
    print(f"Part 1: {part_one_score}")
    print(f"Part 2: {part_two_score}")
    

if __name__ == "__main__":
    main()