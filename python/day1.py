"""
Atanas Delevski
12/12/2022
Advent of Code - Day 1 (Parts I & II)
"""


def consolidate(file_path):
    file = open(file_path, "r")
    elves = []
    curElf = 0
    while file:
        line = file.readline()
        if line.strip():
            curElf += int(line)
        elif line == "":
            break
        else:
            elves.append(curElf)
            curElf = 0
    file.close()
    return elves


def main():
    # Init
    file_path = 'data/day1.txt'
    
    # Consolidate elf food 
    elves = consolidate(file_path)

    # Part 1 - Max 1 Elf
    print(f"Part 1: {max(elves)}")

    # Part 2 - Max 3 Elves 
    print(f"Part 2: {sum(sorted(elves)[-3:])}")
    

if __name__ == "__main__":
    main()