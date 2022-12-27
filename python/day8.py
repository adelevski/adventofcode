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


def part_one(data: list[str]) -> int:
    w, h, ans = len(data[0]), len(data), 0
    perim = (w-2)*2 + (h-2)*2 + 4
    
    for r in range(1, h-1):
        for c in range(1, w-1):
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
    return ans+perim


def part_two(data):
    w, h, ans = len(data[0]), len(data), 0
    for r in range(1, h-1):
        for c in range(1, w-1):
            cur_tree = Tree(data[r][c])

            # Above
            above = 1
            for i in range(r-1, -1, -1):
                if int(data[i][c]) < cur_tree._height and i != 0:
                    above += 1
                else:
                    break

            # Below
            below = 1
            for i in range(r+1, h):
                if int(data[i][c]) < cur_tree._height and i != h-1:
                    below += 1
                else:
                    break

            # Left
            left = 1
            for i in range(c-1, -1, -1):
                if int(data[r][i]) < cur_tree._height and i != 0:
                    left += 1
                else:
                    break

            # Right
            right = 1
            for i in range(c+1, w):
                if int(data[r][i]) < cur_tree._height and i != w-1:
                    right += 1
                else:
                    break

            ans = max(above * below * left * right, ans)
    return ans


def main():
    # Init
    with open(INPUT_FILE, "rt") as f:
        data = f.read().splitlines()

    # Part 1
    part_one_answer = part_one(data)

    # Part 2
    part_two_answer = part_two(data)

    # Print
    print(f"Part 1: {part_one_answer}")
    print(f"Part 2: {part_two_answer}")


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"\nExecution Time: {end-start:0.4f} seconds.")