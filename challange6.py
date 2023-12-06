import re
import math

file_path = 'input6.txt'

with open(file_path, 'r') as fp:
    lines = fp.readlines()


def parse_line_first(line):
    return list(map(int, re.split(r' +', line.replace('\n', '').split(':')[1])[1:]))


def parse_line_seconed(line):
    return int(''.join(re.split(r' +', line.replace('\n', '').split(':')[1])))


def roots(a, b, c):
    sqr_discriminant = (b**2 - 4*a*c)**0.5

    x1 = (-b + sqr_discriminant)/(2*a)
    x2 = (-b - sqr_discriminant)/(2*a)

    return x1, x2


def calc_options(time, distance):
    a = -1
    b = time
    c = -distance
    x1, x2 = roots(a, b, c)
    return len(range(int(x1), min(int(x2), time)))


def stage1():
    time_arr, distances_arr = [parse_line_first(line) for line in lines]

    options_arr = []
    for time, distance in zip(time_arr, distances_arr):
        options_arr.append(calc_options(time, distance))

    print(math.prod(options_arr))


def stage2():
    time, distance = [parse_line_seconed(line) for line in lines]
    print(calc_options(time, distance))


stage1()
stage2()
