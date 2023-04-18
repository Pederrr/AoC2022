from typing import Tuple

Range = Tuple[int, int]


def parse_range(range: str) -> Range:
    r = range.split("-")
    return (int(r[0]), int(r[1]))


def parse_line(line: str) -> Tuple[Range, Range]:
    ranges = line.strip().split(",")
    
    return parse_range(ranges[0]), parse_range(ranges[1]);


def contains(a: Range, b: Range) -> bool:
    return b[0] >= a[0] and b[1] <= a[1]


def overlap(a: Range, b: Range) -> bool:
    return (b[0] >= a[0] and b[0] <= a[1]) \
            or (b[1] >= a[0] and b[1] <= a[1])


def solve(file: str) -> None:
    contains_count = 0
    overlap_count = 0
    with open(file, "r") as input:
        for line in input:
            (a, b) = parse_line(line)
            if contains(a, b) or contains(b, a):
                contains_count += 1
            if overlap(a, b) or overlap(b, a):
                overlap_count += 1

    print("1: ", contains_count)
    print("2: ", overlap_count)
            

if __name__ == "__main__":
    solve("./input.txt")    
