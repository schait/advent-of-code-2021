def get_initial_fish_dict():

    file1 = open("lanternfish.txt", "r")
    fish = [int(x) for x in file1.read().split(",")]
    fish_dict = {x: 0 for x in range(9)}
    for f in fish:
        fish_dict[f] += 1
    return fish_dict

fish_dict = get_initial_fish_dict()

for day in range(256):
    new_dict = {x: 0 for x in range(9)}
    for i in range(1, 9):
        new_dict[i - 1] = fish_dict[i]
    new_dict[6] += fish_dict[0]
    new_dict[8] = fish_dict[0]
    fish_dict = new_dict
    if day == 79:
        print("Part 1", sum(fish_dict.values()))

print("Part 2", sum(fish_dict.values()))