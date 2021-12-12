def get_positions():
    file1 = open("crabs.txt", "r")
    pos = [int(x) for x in file1.read().split(",")]
    return pos


def part1(pos):
    len_pos = len(pos)
    if len_pos % 2 == 0:
        midpt = (pos[len_pos//2] + pos[len_pos//2 - 1])//2
    else:
        midpt = pos[len_pos//2]
    return sum([abs(x - midpt) for x in pos])

def part2(pos):
    avg = int(sum(pos)/len(pos))  # this is the optimal position because of calculus
    total_fuel = 0
    for p in pos:
        dist = abs(p - avg)
        total_fuel += (dist) * (dist + 1) / 2
    return int(total_fuel)

pos = get_positions()
pos.sort()
print("Part 1", part1(pos))
print("Part 2", part2(pos))