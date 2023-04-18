from collections import deque


def find_marker(datastream: str, marker_size: int) -> int:
    last_four = deque(datastream[0:marker_size])
    for i in range(marker_size, len(datastream)):
        last_four.append(datastream[i])
        last_four.popleft()

        if len(set(last_four)) == marker_size:
            return i + 1
    
    return -1


def solve(file: str) -> None:
    datastream = ""
    with open(file, "r") as input:
        datastream = input.readline().strip()
        
    print("1: ", find_marker(datastream, 4))
    print("2: ", find_marker(datastream, 14))


if __name__ == "__main__":
    solve("./input.txt")

