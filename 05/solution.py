from typing import List, Tuple

Stack = List[str]
Source = int
Destination = int
Quantity = int
Command = Tuple[Quantity, Source, Destination]


def parse_stacks(lines: List[str]) -> List[Stack]:
    header = lines.pop().split("  ")
    stacks = [[] for _ in header]
    for line in reversed(lines):
        for i in range(1, len(line), 4):
            if line[i] != " ":
                stacks[i // 4].append(line[i])

    return stacks


def parse_command(command: str) -> Command:
    c = command.strip().split(" ");
    return (int(c[1]), int(c[3]), int(c[5]))


def crate_mover_9000(stacks: List[Stack], commands: List[Command]) -> None:
    for (quantity, source, destination) in commands: 
        for _ in range(quantity):
            crate = stacks[source - 1].pop()
            stacks[destination - 1].append(crate)


def crate_mover_9001(stacks: List[Stack], commands: List[Command]) -> None:
    for (quantity, source, destination) in commands: 
        crates = []
        for _ in range(quantity):
             crates.append(stacks[source - 1].pop())

        stacks[destination - 1] += reversed(crates)


def get_result(stacks: List[Stack]) -> str:
    return "".join([stack[-1] for stack in stacks])


def solve(file: str) -> None:
    lines = []
    with open(file, "r") as input:
        lines = input.readlines()

    stacks1 = parse_stacks(lines[0:9])
    stacks2 = [stack.copy() for stack in stacks1]

    commands = [parse_command(x) for x in lines[10:]]

    crate_mover_9000(stacks1, commands)
    print("1: ", get_result(stacks1))

    crate_mover_9001(stacks2, commands)
    print("2: ", get_result(stacks2))
    


if __name__ == "__main__":
    solve("./input.txt")
