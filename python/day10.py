"""
Atanas Delevski
1/6/2023
Advent of Code 2022 - Day 10 
"""
import time 

INPUT_FILE = 'data/day10.txt'

def arrayRotate(arr, reverse):
    if reverse:
        arr[:] = arr[1:] + arr[0:1]
    else:
        arr[:] = arr[-1:] + arr[0:-1]
    return arr

def exec(data):
    ans = []
    cycles = 0
    reg = 1

    sprite = "###....................................."
    # sprite = '###
    sprite = [pixel for pixel in sprite]
    cur_row = []
    display = []

    def extractInfo(instruction):
        cycles_to_complete = 0
        addX = 0
        if 'noop' in instruction:
            cycles_to_complete = 1
        else:
            cycles_to_complete = 2
            addX = int(instruction.split(' ')[1])
        return [cycles_to_complete, addX]
    
    for instruction in data:
        [cycles_to_complete, addX] = extractInfo(instruction)

        for i in range(0, cycles_to_complete):
            cycles += 1

            if ((cycles - 20) % 40 == 0):
                ans.append(reg*cycles)
            if len(cur_row) == 40:
                display.append(cur_row)
                cur_row = []
            cur_row.append(sprite[(cycles - 1) % 40])

        if addX != 0:
            reg += addX
            for i in range(0, abs(addX)):
                if addX > 0:
                    sprite = arrayRotate(sprite, False)
                else:
                    sprite = arrayRotate(sprite, True)
    display.append(cur_row)
    return sum(ans), display

def main():
    # Init
    with open(INPUT_FILE, "rt") as f:
        data = f.read().splitlines()

    # Execution
    part_one_answer, part_two_answer = exec(data)

    # Print
    print(f"Part 1: {part_one_answer}")
    for row in part_two_answer:
        print("".join(row))

if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"time: {end-start}")