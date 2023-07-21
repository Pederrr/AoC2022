from typing import List


def check_row(row: int, trees: List[List[int]], visible: List[List[int]]) -> None:
    max_seen_right = -1
    max_seen_left = -1

    for i in range(0, len(trees[row])):
        if trees[row][i] > max_seen_left:
            visible[row][i] = 1
            max_seen_left = trees[row][i]
        if trees[row][-i - 1] > max_seen_right:
            visible[row][-i - 1] = 1
            max_seen_right = trees[row][-i - 1]


def check_col(col: int, trees: List[List[int]], visible: List[List[int]]) -> None:
    max_seen_top = -1
    max_seen_down = -1

    for i in range(0, len(trees)):
        if trees[i][col] > max_seen_top:
            visible[i][col] = 1
            max_seen_top = trees[i][col]
        if trees[-i - 1][col] > max_seen_down:
            visible[-i - 1][col] = 1
            max_seen_down = trees[-i - 1][col]


def visible_from_outside(trees: List[List[int]]) -> int:
    visible = [[0 for _ in row] for row in trees]

    for i in range(len(trees)):
        check_row(i, trees, visible)
        check_col(i, trees, visible)

    return sum([sum(row) for row in visible])


def look_up(trees: List[List[int]], row: int, col: int) -> int:
    original_height = trees[row][col]
    distance = 0
    row -= 1
    while row >= 0:
        distance += 1
        if trees[row][col] >= original_height:
            break
        row -= 1
    return distance


def look_down(trees: List[List[int]], row: int, col: int) -> int:
    original_height = trees[row][col]
    distance = 0
    row += 1
    while row < len(trees):
        distance += 1
        if trees[row][col] >= original_height:
            break
        row += 1
    return distance


def look_left(trees: List[List[int]], row: int, col: int) -> int:
    original_height = trees[row][col]
    distance = 0
    col -= 1
    while col >= 0:
        distance += 1
        if trees[row][col] >= original_height:
            break
        col -= 1
    return distance


def look_right(trees: List[List[int]], row: int, col: int) -> int:
    original_height = trees[row][col]
    distance = 0
    col += 1
    while col < len(trees[row]):
        distance += 1
        if trees[row][col] >= original_height:
            break
        col += 1
    return distance


def find_best_spot(trees: List[List[int]]) -> int:
    visible = [
        [
            look_up(trees, row, col)
            * look_down(trees, row, col)
            * look_left(trees, row, col)
            * look_right(trees, row, col)
            for col in range(len(trees[row]))
        ]
        for row in range(len(trees))
    ]

    return max([max(row) for row in visible])


def solve(file: str) -> None:
    trees: List[List[int]] = []
    with open(file, "r") as input:
        trees = [[int(tree) for tree in line.strip()] for line in input]
    print("1: ", visible_from_outside(trees))
    print("2: ", find_best_spot(trees))


if __name__ == "__main__":
    solve("./input.txt")
