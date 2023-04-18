from typing import Tuple, List

Size = int
Index = int

def is_command(line: str) -> bool:
    return line[0] == "$"


def is_cd(line: str) -> bool:
    return is_command and line[2:4] == "cd"


def is_cd_return(line: str) -> bool:
    return is_cd(line) and line[5:7] == ".."

def is_ls(line: str) -> bool:
    return is_command(line) and line[2:4] == "ls"


def parse_size(line: str) -> Size:
    size = line.split(" ")[0]
    if size == "dir":
        return 0
    
    return int(size)


def read_ls(lines: List[str], index: Index) -> Tuple[Size, Index]:
    size = 0
    while index < len(lines) and not is_command(lines[index]):
        size += parse_size(lines[index])
        index += 1

    return size, index



def read_dir(lines: List[str], index: Index, dirs_sizes: List[int]) -> Tuple[Size, Index]:
    total_size = 0
    while index < len(lines):
        if is_cd_return(lines[index]):
            dirs_sizes.append(total_size)
            return total_size, index + 1
        if is_cd(lines[index]):
            size, new_index = read_dir(lines, index + 1, dirs_sizes)
            index = new_index
            total_size += size
        elif is_ls(lines[index]):
            size, new_index = read_ls(lines, index + 1)
            index = new_index
            total_size += size
    
    dirs_sizes.append(total_size)
    return total_size, index


def find_dir_to_remove(sizes: List[int]) -> int:
    available_space = 70000000
    needed_space = 30000000

    # the last in sizes is size of '/'
    unused_space = available_space - sizes[-1] 

    canditate = sizes[-1]
    
    for size in sizes:
        space_after_delete = unused_space + size
        if space_after_delete >= needed_space and size <= canditate:
            canditate = size

    return canditate



def solve(file: str) -> None:
    lines = []
    with open(file, "r") as input:
        lines = input.readlines()

    dirs_sizes = []

    read_dir(lines, 0, dirs_sizes)
    
    print("1: ", sum(filter(lambda size: size <= 100000, dirs_sizes)))
    print("2: ", find_dir_to_remove(dirs_sizes)) 

    

if __name__ == "__main__":
    solve("./input.txt")
