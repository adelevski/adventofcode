"""
Atanas Delevski
12/21/2022
Advent of Code 2022 - Day 6 (Parts I & II)?
"""


def solver(x, n):
    for i in range(len(x)):
        chars = x[i:i+n]
        if len(set(chars)) > n-1:
            return i+n 
    return None
        

def main():
    # Init
    file_path = "data/day6.txt"
    file = open(file_path, 'r')
    lines = file.readlines()

    # Part 1
    part_one_answer = solver(lines[0], 4)

    # Part 2
    part_two_answer = solver(lines[0], 14)

    # Print 
    print(f"Part 1: {part_one_answer}")
    print(f"Part 2: {part_two_answer}")

if __name__ == "__main__":
    main()
