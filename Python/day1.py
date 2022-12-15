def process_file(file='../Inputs/day1.txt'):
    with open(file) as f:
        return f.read()

def part1():
    return sum([1 if lisp == '(' else -1 for lisp in process_file()])
    

def part2(level_to_check=-1):
    level, pos = 0, 0
    for lisp in process_file():
        pos += 1
        if lisp == '(':
            level += 1
        else:
            level -= 1
        
        if level == level_to_check:
            return pos
    return "No Position"

def solution():
    print("Part 1:", part1())
    print("Part 2:", part2())

solution()