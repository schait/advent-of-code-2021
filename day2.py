file1 = open('inputs/day2.txt', 'r')
directions = []
for line in file1.readlines():
    direction, amount = line.split(" ")
    directions.append((direction, int(amount)))

y = 0
x = 0
for direction, amount in directions:
    if direction == "forward":
        x += amount
    elif direction == "down":
        y += amount
    elif direction == "up":
        y -= amount
print("Part 1:", x*y)


y = 0
x = 0
aim = 0
for direction, amount in directions:
    if direction == "forward":
        x += amount
        y += (aim * amount)
    elif direction == "down":
        aim += amount
    elif direction == "up":
        aim -= amount
print("Part 2:", x*y)