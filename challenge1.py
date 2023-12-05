import re
import unicodedata


DIGIT_NAMES = [unicodedata.name(str(i)).split()[-1].lower()
               for i in range(1, 10)]


def to_str(num):
    '''digit representating to string of the digit'''
    if not num.isnumeric():
        return str(DIGIT_NAMES.index(num) + 1)
    else:
        return str(num)


def number_from_line(line):
    res = re.findall(
        r'(?=' + r'(\d|' + '|'.join(DIGIT_NAMES) + ')' + ')', line)
    return int(to_str(res[0]) + to_str(res[-1]))


def stage1(file_path='input1.txt'):
    with open(file_path, 'r') as fp:
        lines = fp.readlines()

    print(sum([int(re.findall(r'\d', line)[0] + re.findall(r'\d', line)[-1])
               for line in lines]))


def stage2(file_path='input1.txt'):
    with open(file_path, 'r') as fp:
        lines = fp.readlines()

    print(sum([number_from_line(line)
               for line in lines]))


stage1()
stage2()
