def process_file(file='../Inputs/day2.txt'):
    presents = list()
    with open(file) as f:
        for dimensions in f.readlines():
            dimensions = dimensions.strip()
            l, w, h = map(int, dimensions.split('x'))
            presents.append((l,w,h))
    return presents

def part1():
    total_wrapping_paper = 0
    presents = process_file()
    for present in presents:
        l, w, h = present
        lw_area = l * w
        wh_area = w * h
        hl_area = h * l
        total_wrapping_paper += 2*lw_area
        total_wrapping_paper += 2*wh_area
        total_wrapping_paper += 2*hl_area
        total_wrapping_paper += min(lw_area, wh_area, hl_area)
    return total_wrapping_paper

def part2():
    total_ribbon = 0
    presents = process_file()
    for present in presents:
        l, w, h = present
        lw_perimeter = 2*(l+w)
        wh_perimeter = 2*(w+h)
        hl_perimeter = 2*(h+l)
        bow = l*w*h
        total_ribbon += min(lw_perimeter, wh_perimeter, hl_perimeter)
        total_ribbon += bow
    return total_ribbon

def solution():
    print("Part 1:", part1())
    print("Part 2:", part2())

solution()