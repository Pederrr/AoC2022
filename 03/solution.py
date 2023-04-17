from functools import reduce
from typing import List, Tuple

def calculate_priority(item: str) -> int:
    if item.islower():
        return ord(item) - ord("a") + 1
    return ord(item) - ord("A") + 27


def calculate_total_priority(rucksack: str) -> int:
    first_compartment = set(rucksack[0:len(rucksack) // 2])
    second_compartment = set(rucksack[len(rucksack) // 2:])

    common_items = first_compartment & second_compartment

    return sum(map(calculate_priority, common_items))

def find_common_item(rucksacks: List[str]) -> str:
    common_item = reduce(set.intersection, map(set, rucksacks))
        
    if len(common_item) != 1:
        # this should not happen
        assert(False)

    return common_item.pop()


def scan_rucksacks(file: str) -> Tuple[int, int]:
    total1 = 0
    total2 = 0
    lines = []
    with open(file, "r") as input:
        for line in input:
            total1 += calculate_total_priority(line.strip())

            lines.append(line.strip())
            if len(lines) == 3:
                total2 += calculate_priority(find_common_item(lines))
                lines = []


    return total1, total2


if __name__ == "__main__":
    (first, second) = scan_rucksacks("./input.txt")
    print("1: ", first)
    print("2: ", second)
