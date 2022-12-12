

def count_calories(x: str) -> int:
    myfile = open(x, "r")
    elves = []
    curElf = 0
    while myfile:
        line  = myfile.readline()
        if line.strip():
            curElf += int(line)
        elif line == "":
            break
        else:
            elves.append(curElf)
            curElf = 0
    myfile.close()

    # Part 1 - Max 1 elf
    print(max(elves))

    # Part 2 - Max 3 elves
    print(sum(sorted(elves)[-3:]))


count_calories('data.txt')