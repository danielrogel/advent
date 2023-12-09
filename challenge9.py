FILE_PATH = 'input9.txt'
with open(FILE_PATH, 'r', encoding='utf-8') as fp:
    lines = fp.readlines()


samples = [[int(val) for val in line.split()] for line in lines]


def calc_prediction(sample, stage):
    diffs = sample
    count = 0
    n = 0
    while any(diffs):
        if stage == 1:
            count += diffs[-1]
        else:
            count += diffs[0] * ((-1) ** n)

        diffs = [next_val - curr_val for curr_val,
                 next_val in zip(diffs[:-1], diffs[1:])]
        n += 1
    return count


print(sum(calc_prediction(sample, stage=1) for sample in samples))
print(sum(calc_prediction(sample, stage=2) for sample in samples))
