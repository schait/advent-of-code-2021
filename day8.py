wires = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
segments = ['top', 'bottom', 'middle', 'topleft', 'topright', 'botleft', 'botright']

def get_segment_entries():
    file1 = open("inputs/day8.txt", "r")
    segment_entries = []
    for line in file1.readlines():
        patterns, digits = line.split("|")
        patterns = patterns.strip().split()
        for i in range(len(patterns)):
            patterns[i] = set(patterns[i])
        digits = digits.strip().split()
        for i in range(len(digits)):
            digits[i] = set(digits[i])
        segment_entries.append({"patterns": patterns, "digits": digits})
    return segment_entries

def count_wires(patterns):
    wire_counts = {w: 0 for w in wires}
    for pattern in patterns:
        for wire in pattern:
            wire_counts[wire] += 1
    return wire_counts

def decode_digits(patterns, segment_map):
    digits = ""
    for pattern in patterns:
        if len(pattern) == 2:
            digit = "1"
        elif len(pattern) == 3:
            digit = "7"
        elif len(pattern) == 4:
            digit = "4"
        elif len(pattern) == 7:
            digit = "8"
        elif len(pattern) == 6:
            if segment_map['middle'] not in pattern:
                digit = "0"
            elif segment_map['botleft'] not in pattern:
                digit = "9"
            elif segment_map['topright'] not in pattern:
                digit = "6"
        elif len(pattern) == 5:
            if segment_map['botright'] not in pattern:
                digit = "2"
            elif segment_map['topright'] not in pattern:
                digit = "5"
            else:
                digit = "3"
        if not digit:
            raise Exception(f"Unable to decode digit {digit} with segment map {segment_map}")
        digits += digit
    return int(digits)


def solve_display(segment_entry):
    segment_map = {x: None for x in segments}

    patterns = sorted(segment_entry['patterns'], key = lambda x: len(x))
    
    one = patterns[0]
    seven = patterns[1]
    four = patterns[2]
    top_wire = (seven - one).pop()
    segment_map['top'] = top_wire  # the top wire is in 7 but not 1

    wire_counts = count_wires(patterns)
    for wire, count in wire_counts.items():
        if count == 9:
            segment_map['botright'] = wire  # bottom right is in every number but 2
        elif count == 4:
            segment_map['botleft'] = wire
        elif count == 6:
            segment_map['topleft'] = wire
    segment_map['topright'] = (one - set(segment_map['botright'])).pop()
    segment_map['middle'] = (four - {segment_map['botright'], segment_map['topright'], segment_map['topleft']}).pop()
    segment_map['bottom'] = (set(wires) - set(segment_map.values())).pop()
    return decode_digits(segment_entry['digits'], segment_map)

def part1(segment_entries):
    count = 0
    for entry in segment_entries:
        count += len([d for d in entry['digits'] if len(d) in [2, 3, 4, 7]])
    return count

segment_entries = get_segment_entries()
print("Part 1", part1(segment_entries))
print("Part 2", sum([solve_display(s) for s in segment_entries]))