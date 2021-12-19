input_str3 = "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"
input_str4 = "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]"

file1 = open("inputs/day18-2.txt", "r")
inputs = file1.read().splitlines()
#print(inputs)

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
    #print("Add to prev: parent:", parent, "current child", current_child)
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
    #print("Add to next: parent:", parent, "current child", current_child)
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
            print(snail_num)
            exploded = explode_num(snail_num)
        splitted = split_num(snail_num)
        if splitted:
            print(snail_num)

# snail_num = parse_input(input_str3)
# print(snail_num)
# reduce_num(snail_num)
# print(snail_num)

addend = parse_input(inputs[0])
for i in range(1, len(inputs)):
    new_sum = f"[{str(addend.children)}, {inputs[i]}]"
    print("Raw", new_sum)
    snail_num = parse_input(new_sum)
    reduce_num(snail_num)
    print("Final", snail_num)
    addend = snail_num
            
