

from dataclasses import dataclass
import re
from operator import attrgetter


@dataclass
class ScratchCard:
    card_num: int
    winning_numbers: set
    my_numbers: set
    multiplicity: int = 1


def parse_line(line):
    line = line.replace('\n', '').split(':')
    card_num = int(line[0].split(' ')[-1])
    winning_numbers, my_numbers = [[int(num) for num in re.split(
        "\s+", val) if num != ''] for val in line[-1].split('|')]
    return {'card_num': card_num, "winning_numbers": set(winning_numbers), "my_numbers": set(my_numbers)}


def calc_worth(scrath_card):
    return int(2**(len(scrath_card.winning_numbers.intersection(scrath_card.my_numbers))-1))


def stage1(file_path='input4.txt'):
    with open(file_path, 'r') as fp:
        lines = fp.readlines()
    fp.close()
    card_arr = [ScratchCard(**parse_line(line)) for line in lines]
    print(sum([calc_worth(card) for card in card_arr]))


def stage2(file_path='input4.txt'):
    with open(file_path, 'r') as fp:
        lines = fp.readlines()
    fp.close()
    card_arr = sorted([ScratchCard(**parse_line(line))
                      for line in lines], key=attrgetter('card_num'))
    for scrath_card in card_arr:
        card_num = scrath_card.card_num
        n_inter = len(scrath_card.winning_numbers.intersection(
            scrath_card.my_numbers))

        for i in range(1, n_inter + 1):
            next_card = next(x for x in card_arr if x.card_num == card_num + i)
            next_card.multiplicity += scrath_card.multiplicity
    print(sum(card.multiplicity for card in card_arr))


stage1()
stage2()
