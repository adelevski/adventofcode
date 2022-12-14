
part_one_base_map = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

part_one_char_map = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}

part_two_outcome_map = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

part_two_win_base_map = {
    'A': 2,
    'B': 3,
    'C': 1
}

part_two_lose_base_map = {
    'A': 3,
    'B': 1,
    'C': 2
}

part_two_draw_base_map = {
    'A': 1,
    'B': 2,
    'C': 3
}

def score_one(first, second):
    # Initialization 
    score = 0

    # Draw
    if first == part_one_char_map[second]: score += 3

    # Win
    if first == 'A' and second == 'Y': score += 6
    if first == 'B' and second == 'Z': score += 6
    if first == 'C' and second == 'X': score += 6
    
    # Base
    score += part_one_base_map[second]

    return score



def score_two(first, second):
    # Initialization
    score = 0

    # Win, Lose, Draw
    score += part_two_outcome_map[second]

    # Base
    if second == 'Z': score += part_two_win_base_map[first] # win
    if second == 'X': score += part_two_lose_base_map[first] # lose
    if second == 'Y': score += part_two_draw_base_map[first]


    return score



def print_function(score_part_one, score_part_two):
    print(f"Part 1: {score_part_one}")
    print(f"Part 2: {score_part_two}")



def main():
    # Input file
    file_path = 'day2.txt'
    file = open(file_path, 'r')

    # Initialization
    score_part_one, score_part_two = 0, 0

    # Iterator
    for line in file:
        first = line.split(" ")[0] # first character
        second = line.split(" ")[-1].split("\n")[0] # second character

        # Part 1
        score_part_one += score_one(first, second) 

        # Part 2
        score_part_two += score_two(first, second)

    print_function(score_part_one, score_part_two)



if __name__ == "__main__":
    main()