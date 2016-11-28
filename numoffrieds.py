# -*- coding:utf-8 -*-

friends = [
        'NYNNN',
        'YNYNN',
        'NYNYN',
        'NNYNY',
        'NNNYN'
    ]


class Human(object):
    def __init__(self, index):
        self.index = index,
        self.friends = set()

    def get_index(self):
        return self.index[0]

    def get_friends_num(self):
        return len(self.friends)


def recursion_depth(friends, maxtimes=2):
    def recusion(human, items, times=0):
        times += 1
        for i, h in enumerate(items):
            if h == 'Y' and human.get_index() != i and times <= maxtimes:
                human.friends.add(i)
                recusion(human, friends[i], times)
        return human

    for index, items in enumerate(friends):
        yield recusion(Human(index), items).get_friends_num()


def recursion_width():


def roop_depth():
    pass


def roop_width():
    pass


def main():
    print max(list(recursion_depth(friends)))


if __name__ == '__main__':
    main()
