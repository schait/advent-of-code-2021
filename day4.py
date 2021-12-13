class BingoSquare:

    def __init__(self, num, marked=False):
        self.num = num
        self.marked = marked
    
    def __repr__(self):
        return f"{self.num} {self.marked}"

class Board:

    def __init__(self, rows):
        self.grid = []
        for row in rows:
            self.grid.append([BingoSquare(x) for x in row])
    
    def __repr__(self):
        return str(self.grid)
    
    def mark_number(self, num):
        for row in self.grid:
            for square in row:
                if square.num == num:
                    square.marked = True
                    return
    
    def has_bingo(self):
        for i in range(5):
            if all([self.grid[i][j].marked for j in range(5)]):
                return True
            if all([self.grid[j][i].marked for j in range(5)]):
                return True
    
    def sum_unmarked_squares(self):
        total = 0
        for i in range(5):
            total += sum(x.num for x in self.grid[i] if not x.marked)
        return total
            

def get_numbers_and_boards():
    file1 = open("inputs/day4.txt", "r")
    lines = file1.read().splitlines()
    numbers_drawn = [int(x) for x in lines[0].split(",")]
    boards = []
    rows = []
    for line in lines[1:]:
        if not line:
            continue
        rows.append([int(x) for x in line.split()])
        if len(rows) == 5:
            boards.append(Board(rows))
            rows = []
    return numbers_drawn, boards


def part1(numbers_drawn, boards):
    for num in numbers_drawn:
        for board in boards:
            board.mark_number(num)
            if board.has_bingo():
                return num * board.sum_unmarked_squares()

def part2(numbers_drawn, boards):
    boards_without_bingos = list(boards)
    last_board = False
    for num in numbers_drawn:
        for i in range(len(boards_without_bingos) - 1, -1, -1):
            board = boards_without_bingos[i]
            board.mark_number(num)
            if board.has_bingo():
                if last_board:
                    return num * board.sum_unmarked_squares()
                del boards_without_bingos[i]
        if len(boards_without_bingos) == 1:
            last_board = True

numbers_drawn, boards = get_numbers_and_boards()
print("Part 1", part1(numbers_drawn, boards))
print("Part 2", part2(numbers_drawn, boards))
