import re

file1 = open("inputs/day17.txt", "r")
inpt = file1.read()
min_x, max_x, min_y, max_y = [int(x) for x in re.findall('-?\d+', inpt)]

OVERSHOOT = -2
UNDERSHOOT = -1

def in_target_area(x, y):
    return min_x <= x <= max_x and min_y <= y <= max_y

def trace_path(x_velocity, y_velocity):
    x = 0
    y = 0
    highest_point = 0
    while x <= max_x and y >= min_y:
        x += x_velocity
        y += y_velocity
        if y > highest_point:
            highest_point = y
        if x_velocity > 0:
            x_velocity -= 1
        y_velocity -= 1
        if in_target_area(x, y):
            return highest_point
    
    if x > max_x:
        return OVERSHOOT
    if y < min_y:
        return UNDERSHOOT

def both_parts():
    highest_point = 0
    min_x_velocity = 1
    num_solutions = 0
    # sum of numbers from x velocity to 1 has to be at least equal to min x
    while (min_x_velocity * (min_x_velocity + 1)) / 2 < min_x:
        min_x_velocity += 1
    for x_velocity in range(min_x_velocity, max_x + 1):
        y_velocity = -abs(min_y)
        while y_velocity < abs(min_y):
            result = trace_path(x_velocity, y_velocity)
            if result >= 0:
                num_solutions += 1
            if result > highest_point:
                highest_point = result
            if result == OVERSHOOT:
                break
            y_velocity += 1
    print("Part 1:", highest_point)
    print("Part 2:", num_solutions)

both_parts()