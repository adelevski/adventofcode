"""
Atanas Delevski
12/20/2022
Advent of Code - Day 5 (Parts I & II?)
"""


dumb_dict = {
    '1': 'NCRTMZP',
    '2': 'DNTSBZ',
    '3': 'MHQRFCTG',
    '4': 'GRZ',
    '5': 'ZNRH',
    '6': 'FHSWPZLD',
    '7': 'WDZRCGM',
    '8': 'SJFLHWZQ',
    '9': 'SQPWN'
}


def part_one(lines):
    for line in lines:
        words = line.split(' ')
        num, cur, dest = words[1], words[3], words[5]
        if '\n' in dest:
            dest = dest[:-1]
        for i in range(int(num)):
            dumb_dict[dest] = dumb_dict[dest] + dumb_dict[cur][-1]
            dumb_dict[cur] = dumb_dict[cur][:-1]
    return dumb_dict


def part_two(lines):
    pass


def  main():
    # Init
    file_path = 'data/day5.txt'
    file = open(file_path, 'r')
    lines = file.readlines()

    # Part 1:
    part_one_answer = part_one(lines[10:])

    # Print'
    print(f"Part 1: {''.join([part_one_answer[x][-1] for x in part_one_answer.keys()])}")


if __name__ == '__main__':
    main()