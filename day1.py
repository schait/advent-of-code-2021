file1 = open('inputs/day1.txt', 'r')
nums = [int(x) for x in file1.readlines()]

def count_increases(offset):
    increase_count = 0
    for i, num in enumerate(nums):
        if i > 0 and nums[i] > nums[i - offset]:
            increase_count += 1
    return increase_count

print("Part 1: ", count_increases(1))
print("Part 2: ", count_increases(3))
