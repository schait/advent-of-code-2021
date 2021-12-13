file1 = open("inputs/day5.txt", "r")
lines = file1.read().splitlines()

def get_vents(diagonals=False):
    vents = []
    for line in lines:
        endpoints = line.split(" -> ")
        x1, y1 = [int(n) for n in endpoints[0].split(",")]
        x2, y2 = [int(n) for n in endpoints[1].split(",")]
        if not diagonals and x1 != x2 and y1 != y2:
            continue
        if x1 == x2:
            dx = 0
        else:
            dx = int((x2 - x1) / abs(x2 - x1))
        if y1 == y2:
            dy = 0
        else:
            dy = int((y2 - y1) / abs(y2 - y1))
        x = x1
        y = y1
        #print(x1, y1, x2, y2, dx, dy)
        while x != x2 or y != y2:
            vents.append((x, y))
            x += dx
            y += dy
        vents.append((x2, y2))
    return vents

def get_overlaps(vents):
    vents_set = set()
    overlaps = set()
    for vent in vents:
        if vent in vents_set:
            overlaps.add(vent)
        else:
            vents_set.add(vent)
    return len(overlaps)

vents = get_vents()
print("Part 1:", get_overlaps(vents))

vents = get_vents(diagonals=True)
print("Part 2:", get_overlaps(vents))