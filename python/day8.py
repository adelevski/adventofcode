"""
Atanas Delevski
12/23/2022
Advent of Code 2022 - Day 8
"""
from dataclasses import dataclass
from pathlib import Path
import time


SCRIPT_DIR = Path(__file__).parent
PROJ_DIR = SCRIPT_DIR.parent
INPUT_FILE = Path(PROJ_DIR, "data/day8.txt")


class Tree:
    """ Has height, and 4 neightbors. U, D, L, R """
    def __init__(self, height: str):
        self._height = int(height)
    
    def is_not_blocked(self, neighbors: list[str]):
        for neighbor in neighbors:
            if int(neighbor) >= self._height:
                return False
        return True


def main():
    with open(INPUT_FILE, "rt") as f:
        data = f.read().splitlines()

    width, height = len(data[0]), len(data)
    perim = (width-2)*2 + (height-2)*2 + 4

    ans = 0
    

    for r in range(1, height-1):
        for c in range(1, width-1):
            cur_tree = Tree(data[r][c])

            # UP
            trees_above = []

            for i in range(r-1, -1, -1):
                trees_above.append(data[i][c])
            above = cur_tree.is_not_blocked(trees_above)

            # Down
            trees_below = []
            for i in range(r+1, len(data)):
                trees_below.append(data[i][c])
            below = cur_tree.is_not_blocked(trees_below)

            # Left
            trees_left = []
            for i in range(c-1, -1, -1):
                trees_left.append(data[r][i])
            left = cur_tree.is_not_blocked(trees_left)

            # Right
            trees_right = []
            for i in range(c+1, len(data[r])):
                trees_right.append(data[r][i])
            right = cur_tree.is_not_blocked(trees_right)

            if (above or below or left or right):
                ans += 1
        
    print(ans + perim)


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"\nExecution Time: {end-start:0.4f} seconds.")