






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
    return max(elves)


print(count_calories('data.txt'))