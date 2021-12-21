from copy import deepcopy

MAX_STEPS = 50
PADDING = MAX_STEPS * 2 + 1

file1 = open("inputs/day20.txt", "r")
enhancer = ""
orig_image = []
enhancer_done = False
darks = ['.' for i in range(PADDING)]
for line in file1.read().splitlines():
    if not line.strip():
        enhancer_done = True
    elif enhancer_done:
        orig_image.append(darks + [ch for ch in line.strip()] + darks)
    else:
        enhancer += line.strip()

for i in range(PADDING):
    orig_image.insert(0, ['.' for j in range(len(orig_image[0]))])
    orig_image.append(['.' for j in range(len(orig_image[0]))])

NUM_ROWS = len(orig_image)
NUM_COLS = len(orig_image[0])

def print_image(image):
    print()
    for row in image:
        print(row)

def get_new_value(row, col, image):
    binary_num = ""
    for r in [row-1, row, row+1]:
        for c in [col-1, col, col+1]:
            binary_num += "1" if image[r][c] == "#" else "0"
    return enhancer[int(binary_num, 2)]

def count_light_pixels(image):
    count = 0
    for r in range(NUM_ROWS):
        for c in range(NUM_COLS):
            if image[r][c] == "#":
                count += 1
    return count

def enhance_image(image, steps):
    count = 0
    for step in range(steps):
        count = 0
        new_image = deepcopy(image)
        for r in range(1, NUM_ROWS - 1):
            for c in range(1, NUM_COLS - 1):
                new_image[r][c] = get_new_value(r, c, image)
                if steps < r < NUM_ROWS - steps and steps < c < NUM_COLS - steps and new_image[r][c] == "#":
                    count += 1
        #print_image(new_image)
        image = new_image
    return count

#print_image(orig_image)
print("Part 1:", enhance_image(orig_image, 2))
print("Part 2:", enhance_image(orig_image, MAX_STEPS))

