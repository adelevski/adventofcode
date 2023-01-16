"""
Atanas Delevski
1/16/2023
Advent of Code 2022 - Day 11
"""
import time

INPUT_PATH = 'data/day11.txt'

def main():
    with open(INPUT_PATH) as f:
        data = f.read().splitlines()
    print(data)

if __name__ == '__main__':
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Time: {end-start} seconds.")