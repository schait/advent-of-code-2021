class Cave:

    def __init__(self, name):
        self.name = name
        self.is_small = name.lower() == name
        self.adj = []
    
    def add_path(self, other_cave):
        # adds path in both directions
        self.adj.append(other_cave)
        other_cave.adj.append(self)
    
    def __repr__(self):
        return self.name

caves_by_name = {}

file1 = open("day12.txt", "r")
lines = file1.read().splitlines()

for line in lines:
    cave1, cave2 = line.strip().split("-")
    if cave1 not in caves_by_name:
        caves_by_name[cave1] = Cave(cave1)
    if cave2 not in caves_by_name:
        caves_by_name[cave2] = Cave(cave2)
    caves_by_name[cave1].add_path(caves_by_name[cave2])

start_cave = caves_by_name['start']

def part1(current, seen, num_paths=0):
    if current.name == 'end':
        num_paths += 1
        return num_paths
    for next_cave in current.adj:
        if next_cave not in seen or not next_cave.is_small:
            num_paths = part1(next_cave, seen + [current], num_paths)
    return num_paths

def part2(current, seen, two_smalls=False, num_paths=0):
    if current.name == 'end':
        num_paths += 1
        return num_paths
    for next_cave in current.adj:
        if next_cave not in seen or not next_cave.is_small:
            num_paths = part2(next_cave, seen + [current], two_smalls, num_paths)
        elif not two_smalls and next_cave.name != 'start':
            num_paths = part2(next_cave, seen + [current], True, num_paths)
    return num_paths

print(part1(start_cave, []))
print(part2(start_cave, []))




