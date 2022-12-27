# --- Day 3: Perfectly Spherical Houses in a Vacuum ---
INPUT_TXT = '../Inputs/day3.txt'
MOVES = {'>': (1, 0), '<': (-1, 0), '^': (0, 1), 'v': (0, -1)}


def part1():
    x, y = 0, 0
    seen = [(x, y)]
    for move in open(INPUT_TXT).readline():
        dx, dy = MOVES[move]
        x, y = x+dx, y+dy
        if (x, y) not in seen:
            seen.append((x, y))
    return len(seen)


def part2():
    santa_index = 0
    santas = [(0, 0), (0, 0)]
    seen = [(0, 0)]
    for move in open(INPUT_TXT).readline():
        santa_x, santa_y = santas[santa_index]
        dx, dy = MOVES[move]
        santa_x, santa_y = santa_x+dx, santa_y+dy
        if (santa_x, santa_y) not in seen:
            seen.append((santa_x, santa_y))
        santas[santa_index] = (santa_x, santa_y)
        santa_index = (santa_index + 1) % len(santas)
    return len(seen)


print(f"part 1: {part1()}")
print(f"part 2: {part2()}")
