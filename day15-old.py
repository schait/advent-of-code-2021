file1 = open("inputs/day15.txt", "r")
grid = []
for line in file1.read().splitlines():
    grid.append([int(x) for x in line])

big_grid = []

for rr in range(5 * len(grid)):
    big_grid.append([])
    for cc in range(5 * len(grid[0])):
        block_y = rr // len(grid)
        block_x = cc // len(grid[0])
        r = rr % len(grid)
        c = cc % len(grid[0])
        val = grid[r][c] + block_y + block_x
        while val > 9:
            val -= 9
        big_grid[rr].append(val)

A_BIG_NUMBER = 99999999

def minimum_cost_unvisited_point(costs, unvisited_points):
    minimum_point = None
    minimum_cost = A_BIG_NUMBER
    for point in unvisited_points:
        cost = costs[point]
        if cost < minimum_cost:
            minimum_point = point
            minimum_cost = cost
    return minimum_point

def neighbors(point, num_rows, num_cols):
    r = point[0]
    c = point[1]
    adj = []
    if r < num_rows - 1:
        adj.append((r+1, c))
    if c < num_cols - 1:
        adj.append((r, c+1))
    if r > 0:
        adj.append((r-1, c))
    if c > 0:
        adj.append((r, c-1))
    return adj

def find_lowest_cost_path(grid):
    visited = set()
    costs = {(0,0): 0}
    unvisited_points = set([(0, 0)])
    num_rows = len(grid)
    num_cols = len(grid[0])
    num_points = num_rows * num_cols

    while len(visited) < num_points:
        current = minimum_cost_unvisited_point(costs, unvisited_points)
        current_cost = costs[current]
        visited.add(current)
        unvisited_points.remove(current)
        for (r, c) in neighbors(current, num_rows, num_cols):
            if current_cost + grid[r][c] < costs.get((r, c), A_BIG_NUMBER):
                costs[(r, c)] = current_cost + grid[r][c]
                unvisited_points.add((r, c))
    return costs[(num_rows-1, num_cols-1)]

print("Part 1: ", find_lowest_cost_path(grid))
print("Part 2: ", find_lowest_cost_path(big_grid))
