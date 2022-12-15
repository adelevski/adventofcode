"""
Atanas Delevski
12/14/2022
Advent of Code 2022 - Day 3 (Parts I & II)
"""




def score_asci(x):
    if 65 <= x <= 90:
        return (x-35)
    else:
        return (x-96)

def part_one(x):
    first, second = x[:len(x)//2], x[len(x)//2:]
    letter_asci = ord([x for x in first if x in second][0])
    print(letter_asci)
    return score_asci(letter_asci)
    
def part_two(x):
    pass

def main():
    # Init
    file_path = "data/day3.txt"
    file = open(file_path, "r")
    lines = file.readlines()

    
    # Part 1
    scores = [part_one(line) for line in lines]
    part_one_score = sum(scores)

    # Part 2
    part_two_score = 0
    for i in range(0, len(lines), 3):
        letter = list(set(lines[i]) & set(lines[i+1]) & set(lines[i+2]))[0]
        letter_asci = ord(letter)
        part_two_score += score_asci(letter_asci)

    print(f"Part 1: {part_one_score}")
    print(f"Part 2: {part_two_score}")
    

if __name__ == "__main__":
    main()