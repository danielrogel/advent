
import math

FILE_PATH = 'input8.txt'
with open(FILE_PATH, 'r', encoding='utf-8') as fp:
    lines = fp.readlines()


def parse_line(line):
    return line.split(' = ')[0], line.split(' = ')[1].replace('\n', '')[1:-1].split(', ')


l_r_inst = lines[0].replace('\n', '')
movement_dict = dict([parse_line(line) for line in lines[2:]])


def count_steps(curr_position, stage):
    count = 0
    while True:
        for c in l_r_inst:
            curr_position = movement_dict[curr_position][0 if c == 'L' else 1]
            count += 1
            if stage == 2 and curr_position[-1] == 'Z':
                return count
            if stage == 1 and curr_position == 'ZZZ':
                return count


print(count_steps(curr_position='AAA', stage=1))

curr_positions = [key for key in movement_dict.keys() if key[-1] == 'A']
print(math.lcm(*[count_steps(pos, stage=2) for pos in curr_positions]))
