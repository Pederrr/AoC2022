from typing import Tuple

def calculate_score(me: int, elf: int):
    if (me - elf) % 3 == 1:
        return 6
    if me == elf:
        return 3
    return 0


def simulate_game(file: str) -> Tuple[int, int]:
    score_1 = 0;
    score_2 = 0;
    with open(file, "r") as input:
        for line in input:
            line = line.strip()

            (elf, me) = line.split(" ")
            elf = ord(elf) - ord("A");
            me = ord(me) - ord("X");
            score_1 += me + 1 + calculate_score(me, elf)

            me = (elf + me - 1) % 3
            score_2 += me + 1 + calculate_score(me, elf)

    return (score_1, score_2);
    

if __name__ == "__main__":
    (first, second) = simulate_game("./input.txt");
    print("1: ", first)
    print("2: ", second)
