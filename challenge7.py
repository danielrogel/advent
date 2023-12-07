from collections import namedtuple

Card = namedtuple('Card', ['rank', 'value'])


class Hand(object):

    def __init__(self, cards, bid, wildcard=False):
        self.wildcard, self.cards, self.bid = wildcard, cards, bid
        self.strength = self.calc_strength()

    def calc_type_value(self):
        hand_type = ["11111", "2111", "221", "311", "32", "41", "5"]
        rank_count = {}
        for card in self.cards:
            rank_count[card.rank] = rank_count.get(card.rank, 0) + 1
        if self.wildcard:
            joker_count = rank_count.get('J', 0)
            if 'J' in rank_count.keys():
                del rank_count["J"]
            if len(rank_count) > 0:
                rank_count[max(rank_count, key=rank_count.get)] += joker_count
            else:
                rank_count["J"] = joker_count
        type_value = [str(multiplicity) for multiplicity in sorted(
            rank_count.values(), reverse=True)]
        type_value = ''.join(type_value)
        return chr(hand_type.index(type_value))

    def calc_strength(self):
        type_value = self.calc_type_value()
        return "".join([type_value] + [chr(card.value) for card in self.cards])

    def __repr__(self) -> str:
        return ''.join([card.rank for card in self.cards])


def line_to_hand(line, wildcard=False):
    line = line.split()
    rank_labels = ['2', '3', '4', '5', '6',
                   '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    rank_labels_wildcard = ['J', '2', '3', '4',
                            '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
    cards = [Card(rank, rank_labels_wildcard.index(rank) if wildcard
                  else rank_labels.index(rank)) for rank in line[0]]
    bid = int(line[1])
    return Hand(cards, bid, wildcard)


def stage(stage_num, file_path='input7.txt'):
    with open(file_path, 'r') as fp:
        lines = fp.readlines()

    # Calculate the total bid amount
    total_bid = sum(
        rank * card.bid
        for rank, card in zip(
            range(1, len(lines) + 1),
            sorted(
                [line_to_hand(line, wildcard=(stage_num == 2))
                 for line in lines],
                key=lambda x: x.strength
            )
        )
    )
    print(total_bid)


stage(stage_num=1)
stage(stage_num=2)
