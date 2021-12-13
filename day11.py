file1 = open("inputs/day11.txt", "r")
grid = []
for line in file1.read().splitlines():
    grid.append([int(x) for x in line])

NUM_ROWS = len(grid)
NUM_COLS = len(grid[0])

def neighbors(row, col):
    neighbor_coords = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            new_row = row + dy
            new_col = col + dx
            if 0 <= new_row < NUM_ROWS and 0 <= new_col < NUM_COLS:
                neighbor_coords.append((new_row, new_col))
    return neighbor_coords

def flash(grid, row, col):
    grid[row][col] = "F"
    for new_row, new_col in neighbors(row, col):
        if grid[new_row][new_col] != "F":  # if already flashed in this step, don't update
            grid[new_row][new_col] += 1
            if grid[new_row][new_col] > 9:
                flash(grid, new_row, new_col)

num_flashes = 0
prev_num_flashes = 0
part1 = 0
part2 = 0
step = 1
while part1 == 0 or part2 == 0:
    for r in range(NUM_ROWS):
        for c in range(NUM_COLS):
            if grid[r][c] != "F":  # if already flashed in this step, don't update
                grid[r][c] += 1
                if grid[r][c] > 9:
                    flash(grid, r, c)
    
    # count flashes and reset all octopi that flashed during current step to 0
    for r in range(NUM_ROWS):
        for c in range(NUM_COLS):
            if grid[r][c] == "F":
                num_flashes += 1
                grid[r][c] = 0

    if num_flashes - prev_num_flashes == NUM_ROWS * NUM_COLS:  # all flashed!
        part2 = step
    prev_num_flashes = num_flashes

    if step == 100:
        part1 = num_flashes
    step += 1

print("Part 1", part1)
print("Part 2", part2)