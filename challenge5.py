
from dataclasses import dataclass
from typing import Tuple


@dataclass
class RangeObject:
    start_from: int
    start_to: int
    length: int

    def __getitem__(self, __key: int | range) -> int | Tuple[range, ...]:
        if type(__key) is range:
            return range(max(__key.start, self.start_from) - self.start_from + self.start_to, min(
                __key.stop, self.start_from + self.length) - self.start_from + self.start_to), range(__key.start, min(self.start_from, __key.stop)), range(max(self.start_from + self.length, __key.start), __key.stop)
        elif __key >= self.start_from and __key < self.start_from + self.length:
            return self.start_to + (__key - self.start_from)
        else:
            return None

    def __contains__(self, __key: int):
        return self.__getitem__(__key) is not None


@dataclass
class MappingObject:
    ranges_list: list[RangeObject]

    def __getitem__(self, __key: int | range | list) -> int | range | list:
        items_arr = []
        for range_object in self.ranges_list:
            if type(__key) is list:
                key_cop = __key.copy()
                __key = []
                for key in key_cop:
                    in_, before, after = range_object[key]
                    items_arr.append(in_)
                    __key += bool(len(before)) * [before] \
                        + bool(len(after)) * [after]
            elif type(__key) is int and range_object[__key] is not None:
                items_arr.append(range_object[__key])
            elif type(__key) is range:
                in_, before, after = range_object[__key]
                items_arr.append(in_)
                __key = [before, after]

        if len(items_arr) == 0:
            return __key
        elif type(__key) is list:
            return items_arr + __key
        else:
            return items_arr[0]


@dataclass
class Mapping:
    mapping_objects_list: list[MappingObject]

    def __getitem__(self, __key: int | range) -> int | range:
        value = __key
        for mapping_object in self.mapping_objects_list:
            if type(value) is list:
                value = list(set(sum([mapping_object[val]
                                      for val in value], [])))
            else:
                value = mapping_object[value]

        return value


def parse_seed_line_first(line):
    return [int(num)
            for num in line.split(':')[1].split(' ') if num != '']


def parse_seed_line_seconed(line):
    seed_arr = [int(num) for num in line.split(':')[1].split(' ') if num != '']
    seeds_zip = zip(seed_arr[::2], seed_arr[1::2])
    return [range(seed_start, seed_start + seed_length) for seed_start, seed_length in seeds_zip]


def parse_lines(lines, seed_parse):
    seeds = parse_seed_line_first(
        lines[0]) if seed_parse == 1 else parse_seed_line_seconed(lines[0])
    mapping = Mapping([])
    mapping_object = None
    for line in lines[0:]:
        if ':' in line:
            if mapping_object is not None:
                mapping.mapping_objects_list.append(mapping_object)
            mapping_object = MappingObject([])
        elif mapping_object is not None and line != '':
            mapping_object.ranges_list.append(
                RangeObject(**dict(zip(['start_to', 'start_from',
                                        'length'], [int(val) for val in line.split(' ') if val != '']))))
    if mapping_object is not None:
        mapping.mapping_objects_list.append(mapping_object)
    return seeds, mapping


def stage(file_path='input5.txt', stage_num=1):
    with open(file_path, 'r') as fp:
        lines = fp.readlines()
        lines = [line.replace('\n', '') for line in lines]
    seeds, mapping = parse_lines(lines, seed_parse=stage_num)

    if stage_num == 1:
        print(min([mapping[seed] for seed in seeds]))

    elif stage_num == 2:
        print(min(min(val.start for val in mapping[seed]) for seed in seeds))


stage(stage_num=1)
stage(stage_num=2)
