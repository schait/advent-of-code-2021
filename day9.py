class GraphNode:

    def __init__(self, height):
        self.height = height
        self.down = None
        self.left = None
        self.right = None
        self.up = None
    
    def neighbors(self):
        return [x for x in [self.down, self.up, self.left, self.right] if x]
    
    def neighbor_heights(self):
        return [x.height for x in [self.down, self.up, self.left, self.right] if x]

    def __repr__(self):
        return str(self.height)

def get_grid():
    file1 = open("heightmap.txt", "r")
    grid = []
    for line in file1.read().splitlines():
        grid.append([GraphNode(int(x)) for x in line])
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if r > 0:
                grid[r][c].up = grid[r-1][c]
            if c > 0:
                grid[r][c].left = grid[r][c-1]
            if r < len(grid) - 1:
                grid[r][c].down = grid[r+1][c]
            if c < len(grid[0]) - 1:
                grid[r][c].right = grid[r][c+1]

    return grid
    

def find_low_points(grid):
    low_points = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c].height < min(grid[r][c].neighbor_heights()):
                low_points.append(grid[r][c])
    return low_points

def find_basin(current, basin):
    for neighbor in current.neighbors():
        if neighbor.height < 9 and neighbor not in basin:
            basin.append(neighbor)
            basin = find_basin(neighbor, basin)
    return basin

grid = get_grid()
low_points = find_low_points(grid)

basin_sizes = []
for low_point in low_points:
    basin = find_basin(low_point, [low_point])
    basin_sizes.append(len(basin))
sorted_basin_sizes = sorted(basin_sizes, reverse=True)

print("Part 1:", len(low_points) + sum([x.height for x in low_points]))
print("Part 2:", sorted_basin_sizes[0] * sorted_basin_sizes[1] * sorted_basin_sizes[2])
