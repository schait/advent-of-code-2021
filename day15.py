from heapq import heappush, heappop

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

INF = float('inf')

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
    unvisited_heap = [(0, (0, 0))]
    num_rows = len(grid)
    num_cols = len(grid[0])
    num_points = num_rows * num_cols

    while len(visited) < num_points:
        current_distance, current = heappop(unvisited_heap)
        current_cost = costs[current]
        visited.add(current)
        for (r, c) in neighbors(current, num_rows, num_cols):
            if current_cost + grid[r][c] < costs.get((r, c), INF):
                costs[(r, c)] = current_cost + grid[r][c]
                heappush(unvisited_heap, (costs[r, c], (r, c)))
    return costs[(num_rows-1, num_cols-1)]

print("Part 1: ", find_lowest_cost_path(grid))
print("Part 2: ", find_lowest_cost_path(big_grid))
