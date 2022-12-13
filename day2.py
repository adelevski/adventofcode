




def readLines(x):
    file = open(x, 'r')
    score = 0
    for line in file:
        first = line.split(" ")[0]
        second = line.split(" ")[-1].split("\n")[0]
        if ((first=="A") and (second=="X")) or ((first=="B") and (second=="Y")) or ((first=="C") and (second=="Z")):
            if second == "X":
                score += 4
            elif second == "Y":
                score += 5
            elif second == "Z":
                score += 6
        elif first == "A":
            if second == "Y":
                score += 8
            elif second == "Z":
                score += 3
        elif first == "B":
            if second == "X":
                score += 1
            elif second == "Z":
                score += 9
        elif first == "C":
            if second == "X":
                score += 7
            elif second == "Y":
                score += 2
    print(score)



readLines('day2.txt')