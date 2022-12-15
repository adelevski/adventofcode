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
    return score_asci(letter_asci)
    
def part_two(x):
    pass

def main():
    file_path = "data/day3.txt"
    file = open(file_path, "r")
    part_one_score = sum(part_one(line) for line in file)
    part_two_score = 0

    # part 2
    for i in range(0, len(file), 3):
        d1 = [letter for letter in file[i]]
        d2 = [letter for letter in file[i+1]]
        d3 = [letter for letter in file[i+2]]
        df = [d1.add(d2)]
        df = set([df.add(d3)])
        part_two_score += score_asci(list(df)[0])

    print(f"Part 1: {part_one_score}")
    

if __name__ == "__main__":
    main()