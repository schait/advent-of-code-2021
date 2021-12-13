def parse_input():
    points = set()
    folds = []
    file1 = open("day13.txt", "r")
    lines = file1.read().splitlines()
    for line in lines:
        if line.startswith("fold along"):
            axis, coord = line.replace("fold along ", "").strip().split("=")
            folds.append((axis, int(coord)))
        elif line:
            x, y = line.strip().split(",")
            points.add((int(x), int(y)))
    return points, folds

points, folds = parse_input()

for i, fold in enumerate(folds):
    new_points = set()
    fold_line = fold[1]
    fold_axis = fold[0]
    for point in points:
        if fold_axis == 'x':
            if point[0] > fold_line:
                new_coord = fold_line + fold_line - point[0]
                new_points.add((new_coord, point[1]))
            elif point[0] < fold_line:
                new_points.add(point)
        elif fold_axis == 'y':
            if point[1] > fold_line:
                new_coord = fold_line + fold_line - point[1]
                new_points.add((point[0], new_coord))
            elif point[1] < fold_line:
                new_points.add(point)
    points = new_points
    if i == 0:
        print("Part 1: ", len(points))

max_x = max([p[0] for p in points])
max_y = max([p[1] for p in points])
for y in range(max_y+1):
    print(''.join(["#" if (x, y) in points else " " for x in range(max_x+1)]))
