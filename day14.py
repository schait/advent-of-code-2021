from collections import defaultdict

file1 = open("inputs/day14.txt", "r")
lines = file1.read().splitlines()
polymer = lines[0].strip()
insertions = {}
for line in lines[2:]:
    pair, to_insert = line.strip().split(" -> ")
    insertions[pair] = to_insert

pair_count = defaultdict(lambda: 0)
for i in range(len(polymer) - 1):
    pair_count[polymer[i:i+2]] += 1

def most_common_minus_least_common(pair_count):
    freqs = defaultdict(lambda: 0)
    for pair, count in pair_count.items():
        freqs[pair[0]] += count
        freqs[pair[1]] += count
    # everything is double counted except for first element and last element in polymer
    # so add 1 to those counts and then divide all counts by 2
    freqs[polymer[0]] += 1
    freqs[polymer[-1]] += 1
    for key in freqs:
        freqs[key] //= 2
    return max(freqs.values()) - min(freqs.values())

for step in range(40):
    new_pair_count = defaultdict(lambda: 0)
    for pair, count in pair_count.items():
        if pair in insertions:
            new_pair_count[pair[0] + insertions[pair]] += count
            new_pair_count[insertions[pair] + pair[1]] += count
    pair_count = new_pair_count
    if step == 9:
        print("Part 1:", most_common_minus_least_common(pair_count))
print("Part 2:", most_common_minus_least_common(pair_count))
            
