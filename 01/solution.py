from typing import List;

def sum_calories(file: str) -> List[int]:
    result = []
    
    with open(file, "r") as input:
        sum = 0
        for line in input:
            line = line.strip()

            if line == "":
                result.append(sum)
                sum = 0
            else:
                sum += int(line)

    return sorted(result)


if __name__ == "__main__":
    calories = sum_calories("./input.txt")
    print("1: ", calories[-1])
    print("2: ", sum(calories[-1:-4:-1]))
