from collections import defaultdict

file1 = open("inputs/day21.txt", "r")
lines = file1.read().splitlines()
orig_positions = [int(line.strip()[-1]) for line in lines]
print(orig_positions)


def alt_modulo(value, n):
    m = value % n
    if m == 0:
        return n
    return m

def part1():
    positions = list(orig_positions)
    scores = [0, 0]
    turn = 0
    die_roll = 1
    num_rolls = 0

    while scores[0] < 1000 and scores[1] < 1000:
        for i in range(3):
            positions[turn] = alt_modulo(positions[turn] + die_roll, 10)
            die_roll = alt_modulo(die_roll + 1, 100)
            num_rolls += 1
        scores[turn] += positions[turn]
        turn = 1 - turn

    print("Part 1:", min(scores) * num_rolls)


def part2():
    # (pos[0], pos[1], scores[0], scores[1]): count
    universe_state_count = {(orig_positions[0], orig_positions[1], 0, 0): 1}
    turn = 0
    wins = [0, 0]
    while universe_state_count:
        new_state_count = defaultdict(lambda: 0)
        for universe_state, count in universe_state_count.items():
            old_pos = universe_state[turn]
            opp_pos = universe_state[1 - turn]  # won't change
            old_score = universe_state[turn + 2]
            opp_score = universe_state[(1 - turn) + 2]
            for roll1 in (1, 2, 3):
                for roll2 in (1, 2, 3):
                    for roll3 in (1, 2, 3):
                        new_pos = alt_modulo(old_pos + roll1 + roll2 + roll3, 10)
                        new_score = old_score + new_pos
                        if new_score >= 21:
                            wins[turn] += count
                        else:
                            if turn:
                                key = (opp_pos, new_pos, opp_score, new_score)
                            else:
                                key = (new_pos, opp_pos, new_score, opp_score)
                            new_state_count[key] += count
        turn = 1 - turn
        universe_state_count = new_state_count
    print("Part 2:", wins)

part1()
part2()
