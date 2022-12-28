"""
Atanas Delevski
12/27/2022
Advent of Code 2022 - Day 9
"""
import time


INPUT_PATH = "data/smol.txt"


def main():
    with open(INPUT_PATH) as f:
        data = f.read().splitlines()
    
    ans = 0
    grid = [['s']]
    cur_row = 0
    cur_col = 0
    for dir, steps in [s.split(' ') for s in data]:
        steps = int(steps)
        print(f"Dir: {dir}, Steps: {steps}")
        if dir == 'R':
            if len(grid[cur_row]) < cur_col + steps + 1:
                for i in range(len(grid[cur_row]), cur_col + steps + 1):
                    grid[cur_row].append('#')
            if grid[cur_row][cur_col] != 's':
                grid[cur_row][cur_col] = '*'
            cur_col += steps
            grid[cur_row][cur_col] = 'H'
        elif dir == 'L':
            
            for i in range(((cur_row-1)+steps) - len(grid[cur_row])):
                if len(grid[cur_row]) < (cur_row-1)+steps:
                    grid[cur_row].insert(0, '#')
            
            if grid[cur_row][cur_col] != 's':
                grid[cur_row][cur_col] = '*'    
            cur_col -= steps
            grid[cur_row][cur_col] = 'H'
        elif dir == 'U':
            if len(grid) < abs(cur_row - steps):
                for i in range(abs(len(grid) - (cur_row - steps)) - 1):
                    grid.insert(0, ['*']*len(grid[cur_row]))
                    grid[cur_row-i-1][cur_col] = '#'
            if grid[cur_row+steps][cur_col] != 's':
                grid[cur_row+steps][cur_col] = '*'
            cur_row =  max(0, cur_row -steps)
            grid[cur_row][cur_col] = 'H'
        else:
            for i in range(steps):
                grid.append(['*']*len(grid[cur_row]))
            if grid[cur_row][cur_col] != 's':
                grid[cur_row][cur_col] = '*'
            cur_row += steps
            grid[cur_row][cur_col] = 'H'
        
        
        for row in grid:
            if len(row) < max([len(r) for r in grid]):
                row.append('*')
            print(row)
        print(f"Row: {cur_row}, Col: {cur_col}")

        for row in grid:
            for sign in row:
                if sign == '#' or sign == 's':
                    ans += 1
    print(ans)
    f.close()


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Execution time: {end-start} seconds.")