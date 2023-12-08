from collections import defaultdict
import re
import math


def check_validity(pull, max_red=12, max_green=13, max_blue=14):
    '''pull is of the form '[number color number color .. ]'''
    dict_ = pull_to_dict(pull)
    if dict_['red'] <= max_red and dict_['green'] <= max_green and dict_['blue'] <= max_blue:
        return True
    return False


def pull_to_dict(pull):
    '''pull is of the form '[number color number color .. ]'''
    dict_ = defaultdict(
        int, zip(pull[1::2], [int(num_str) for num_str in pull[::2]]))
    return dict_


def parse_line(line):
    game_id = int(re.findall(r'\d+', line)[0])
    pulls = [a.replace(',', '').split()
             for a in line.split(': ')[-1].split(';')]
    return game_id, pulls


def calc_power(dict_lst):
    return math.prod([max([dict_[key] for dict_ in dict_lst])
                      for key in ['green', 'blue', 'red']])


def stage1(file_path='input2.txt'):
    with open(file_path, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    game_ids_lst = []
    for line in lines:
        game_id, pulls = parse_line(line)
        if all([check_validity(pull) for pull in pulls]):
            game_ids_lst.append(game_id)

    print(sum(game_ids_lst))


def stage2(file_path='input2.txt'):
    with open(file_path, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    power = 0
    for line in lines:
        _, pulls = parse_line(line)
        power += calc_power([pull_to_dict(pull) for pull in pulls])

    print(power)


stage1()
stage2()
