file1 = open("inputs/day18.txt", "r")
inputs = file1.read().splitlines()

class Pair:

    def __init__(self, parent=None, children=None, level=0):
        self.parent = parent
        self.children = children if children else []
        self.level = level
    
    def __repr__(self):
        return str(self.children)
    
def parse_input(string):
    root = None
    parent = None
    level = 0
    i = 0
    while i < len(string):
        char = string[i]
        if char == '[':
            pair = Pair(level=level)
            if root:
                parent.children.append(pair)
            else:
                root = pair
            pair.parent = parent
            parent = pair
            level += 1
        elif char == ']':
            parent = parent.parent
            level -= 1
        elif char.isdigit():
            num = char
            if string[i+1].isdigit():
                num += string[i+1]
                i += 1
            parent.children.append(int(num))
        i += 1
    
    return root

def replace_child(parent, old, new, reverse_lookup=False):
    loop_range = range(len(parent.children))
    if reverse_lookup:
        loop_range = reversed(loop_range)
    for i in loop_range:
        if parent.children[i] == old:
            parent.children[i] = new
            break

def add_to_previous_number(parent, current_child, to_add):
    if not parent:
        return
    if parent.children[0] == current_child:
        add_to_previous_number(parent.parent, parent, to_add)
    elif parent.children[1] == current_child:
        if type(parent.children[0]) is int:
            replace_child(parent, parent.children[0], parent.children[0] + to_add, True)
        else:
            add_to_previous_number(parent.children[0], None, to_add)
    elif type(parent.children[1]) is int:
        replace_child(parent, parent.children[1], parent.children[1] + to_add, True)
    else:
        add_to_previous_number(parent.children[1], None, to_add)
    return
    
def add_to_next_number(parent, current_child, to_add):
    if not parent:
        return
    if parent.children[1] == current_child:
        add_to_next_number(parent.parent, parent, to_add)
    elif parent.children[0] == current_child:
        if type(parent.children[1]) is int:
            replace_child(parent, parent.children[1], parent.children[1] + to_add)
        else:
            add_to_next_number(parent.children[1], None, to_add)
    elif type(parent.children[0]) is int:
        replace_child(parent, parent.children[0], parent.children[0] + to_add)
    else:
        add_to_next_number(parent.children[0], None, to_add)
    return


def explode_num(current, parent=None, done=False):
    if done:
        return True
    if type(current) is Pair:
        if current.level < 4:
            done = explode_num(current.children[0], current, done)
            if not done:
                done = explode_num(current.children[1], current, done)
        elif all([type(x) is int for x in current.children]):
            left = current.children[0]
            right = current.children[1]
            index = parent.children.index(current)
            add_to_previous_number(parent, current, left)
            add_to_next_number(parent, current, right)
            replace_child(parent, current, 0)
            return True
    return done

def split_num(current, parent=None, done=False):
    if done:
        return True
    if type(current) is Pair:
        done = split_num(current.children[0], current, done)
        if not done:
            done = split_num(current.children[1], current, done)
    elif type(current) is int and current > 9:
        half_rd_down = current // 2
        new_pair = Pair(
            parent=parent, 
            children=[half_rd_down, current - half_rd_down],
            level=parent.level + 1)
        replace_child(parent, current, new_pair)
        return True
    return done


def reduce_num(snail_num):
    exploded = True
    splitted = True
    while exploded or splitted:
        exploded = explode_num(snail_num)
        while exploded:
            #print(snail_num)
            exploded = explode_num(snail_num)
        splitted = split_num(snail_num)
    return snail_num


def add_number_strings(num_string1, num_string2):
    raw_sum = f"[{num_string1}, {num_string2}]"
    snail_num = parse_input(raw_sum)
    return reduce_num(snail_num)


def magnitude(snail_num):
    if type(snail_num) is int:
        return snail_num
    return 3 * magnitude(snail_num.children[0]) + 2 * magnitude(snail_num.children[1])
    
def part1():
    addend = parse_input(inputs[0])
    snail_num = None
    for i in range(1, len(inputs)):
        snail_num = add_number_strings(str(addend.children), inputs[i])
        addend = snail_num
    print("Part 1:", magnitude(snail_num))

def part2():
    max_sum = 0
    for i in range(len(inputs)):
        for j in range(i, len(inputs)):
            snail_num = add_number_strings(inputs[i], inputs[j])
            mag = magnitude(snail_num)
            if mag > max_sum:
                max_sum = mag
            snail_num = add_number_strings(inputs[j], inputs[i])
            mag = magnitude(snail_num)
            if mag > max_sum:
                max_sum = mag
    print("Part 2:", max_sum)

part1()
part2()
