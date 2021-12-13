file1 = open('inputs/day3.txt', 'r')
lines = file1.read().splitlines()

def find_common_bit(bit_idx, binary_nums, least=False):
    num_ones = len([bnum[bit_idx] for bnum in binary_nums if bnum[bit_idx] == "1"])
    if least:
        return "1" if num_ones * 2 < len(binary_nums) else "0"
    else:
        return "1" if num_ones * 2 >= len(binary_nums) else "0"


def filter_by_common_bit(bit_idx, binary_nums, least=False):
    common_bit = find_common_bit(bit_idx, binary_nums, least)
    return [x for x in binary_nums if x[bit_idx] == common_bit]


def convert_binary_string_to_decimal(bin_string):
    return int(bin_string, 2)


def part1():
    gamma = ""
    epsilon = ""
    for i in range(len(lines[0])):
        most_common = int(find_common_bit(i, lines))
        gamma += str(most_common)
        epsilon += str(1 - most_common)
    gamma_dec = convert_binary_string_to_decimal(gamma)
    epsilon_dec = convert_binary_string_to_decimal(epsilon)
    return gamma_dec * epsilon_dec


def part2():
    i = 0
    o2_candidates = list(lines)
    co2_candidates = list(lines)
    while len(o2_candidates) > 1 or len(co2_candidates) > 1:
        if len(o2_candidates) > 1:
            o2_candidates = filter_by_common_bit(i, o2_candidates)
        if len(co2_candidates) > 1:
            co2_candidates = filter_by_common_bit(i, co2_candidates, least=True)
        i += 1
    o2 = convert_binary_string_to_decimal(o2_candidates[0])
    co2 = convert_binary_string_to_decimal(co2_candidates[0])
    return o2 * co2

print("Part 1: ", part1())
print("Part 2: ", part2())

