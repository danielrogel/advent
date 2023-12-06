import re
import math


def open_file(file_path='input6.txt'):
    with open(file_path, 'r') as fp:
        return fp.readlines()


def parse_line_first(line):
    return list(map(int, re.split(r' +', line.replace('\n', '').split(':')[1])[1:]))


def parse_line_seconed(line):
    return int(''.join(re.split(r' +', line.replace('\n', '').split(':')[1])))


def roots(a, b, c):
    return (-b + (b**2 - 4*a*c)**0.5)/(2*a), (-b - (b**2 - 4*a*c)**0.5)/(2*a)


def calc_options(time, distance):
    a, b, c = -1, time, -distance
    x1, x2 = roots(a, b, c)
    return len(range(int(x1), min(int(x2), time)))


def stage1():
    lines = open_file()
    time_arr, distances_arr = [parse_line_first(line) for line in lines]
    print(math.prod([calc_options(time, distance)
          for time, distance in zip(time_arr, distances_arr)]))


def stage2():
    lines = open_file()
    time, distance = [parse_line_seconed(line) for line in lines]
    print(calc_options(time, distance))


stage1()
stage2()
