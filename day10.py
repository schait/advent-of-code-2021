file1 = open("day10.txt", "r")
lines = file1.read().splitlines()

matches = {'[': ']', '<': '>', '(': ')', '{': '}'}
openers_set = {'[', '{', '(', '<'}
error_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
autocomplete_scores = {')': 1, ']': 2, '}': 3, '>': 4}

error_score = 0
autocompletes = []
for line in lines:
    openers = []
    corrupted = False
    for char in line:
        if char in openers_set:
            openers.append(char)
        elif char == matches[openers[-1]]:
            openers.pop()
        else:
            error_score += error_scores[char]
            corrupted = True
            break
    if not corrupted:
        autocompletes.append([matches[ch] for ch in reversed(openers)])

part2_scores = []
for a in autocompletes:
    score = 0
    for char in a:
        score = 5 * score + autocomplete_scores[char]
    part2_scores.append(score)
part2_scores.sort()

print("Part 1", error_score)
print("Part 2", part2_scores[len(part2_scores) // 2])