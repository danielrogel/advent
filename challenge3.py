import re
import math

DIGITS = list(map(str, range(10)))
NON_VALID_SYMBOLS = set(['.'] + DIGITS)


def get_value(lines, line_number, line_width, index):
    if line_number < 0 or index < 0 or index >= line_width or line_number >= len(lines):
        return '.'
    return lines[line_number][index]


def adjacent_symbols(lines, line_number, start, end, line_width=140):
    line_numbers = list(range(line_number - 1, line_number + 2))
    index_numbers = list(range(start - 1, end + 1))
    return {str(line_number_k)+'_'+str(index_k):
            get_value(lines, line_number_k, line_width, index_k)
            for line_number_k in line_numbers for index_k in index_numbers}


def get_number_desc(lines, line_number, index, line_width=140):
    i = 1
    while index - i >= 0:
        if not lines[line_number][index - i] in DIGITS:
            break
        i += 1
    start = index-(i-1)
    j = 1
    while index + j < line_width:
        if not lines[line_number][index + j] in DIGITS:
            break
        j += 1
    end = index+(j)

    return start, end, int(lines[line_number][start:end])


def create_numbers_set(lines, line_number, start, end):
    number_matches = set()
    for key, value in adjacent_symbols(lines, line_number, start, end).items():
        if value in DIGITS:
            line_number_k, index = key.split('_')
            start_k, end_k, value_k = get_number_desc(
                lines, int(line_number_k), int(index))
            number_matches.add(
                (int(line_number_k), start_k, end_k, value_k))
    return number_matches


def stage1(file_path='input3.txt'):

    with open(file_path, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
        lines = [line.replace('\n', '') for line in lines]

    part_sum = 0
    for line_number, line in enumerate(lines):
        for match in re.finditer(r'\d+', line):
            start, end = match.start(0), match.end(0)
            value = int(line[start: end])
            if set(adjacent_symbols(lines, line_number, start,
                                    end).values()).issubset(NON_VALID_SYMBOLS):
                continue
            part_sum += value
    print(part_sum)


def stage2(file_path='input3.txt'):

    with open(file_path, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
        lines = [line.replace('\n', '') for line in lines]

    part_mul_sum = 0
    for line_number, line in enumerate(lines):
        for match in re.finditer(r'\*', line):
            start, end = match.start(0), match.end(0)
            number_matches = create_numbers_set(lines, line_number, start, end)
            if len(number_matches) > 1:
                part_mul_sum += math.prod([tuple_[-1]
                                           for tuple_ in number_matches])

    print(part_mul_sum)


stage1()
stage2()
