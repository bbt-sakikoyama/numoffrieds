# -*- coding:utf-8 -*-
# return 2
friends0 = [
        'NYY',
        'YNY',
        'YYN'
    ]

# return 4
friends1 = [
        'NYNNN',
        'YNYNN',
        'NYNYN',
        'NNYNY',
        'NNNYN'
    ]

# return 8
friends2 = [
        'NNNNYNNNNN',
        'NNNNYNYYNN',
        'NNNYYYNNNN',
        'NNYNNNNNNN',
        'YYYNNNNNNY',
        'NNYNNNNNYN',
        'NYNNNNNYNN',
        'NYNNNNYNNN',
        'NNNNNYNNNN',
        'NNNNYNNNNN'
    ]

# return 6
friends3 = [
        'NNNNNNNNNNNNNNY',
        'NNNNNNNNNNNNNNN',
        'NNNNNNNYNNNNNNN',
        'NNNNNNNYNNNNNNY',
        'NNNNNNNNNNNNNNY',
        'NNNNNNNNYNNNNNN',
        'NNNNNNNNNNNNNNN',
        'NNYYNNNNNNNNNNN',
        'NNNNNYNNNNNYNNN',
        'NNNNNNNNNNNNNNY',
        'NNNNNNNNNNNNNNN',
        'NNNNNNNNYNNNNNN',
        'NNNNNNNNNNNNNNN',
        'NNNNNNNNNNNNNNN',
        'YNNYYNNNNYNNNNN'
    ]

class Human(object):
    def __init__(self, index):
        self.index = index
        self.friends = set()

    def get_friends_num(self):
        return len(self.friends)


def recursion_depth(friends, maxtimes=2):
    def recusion(human, items, times=0):
        times += 1
        for i, h in enumerate(items):
            if h == 'Y' and human.index != i and times <= maxtimes:
                human.friends.add(i)
                recusion(human, friends[i], times)
        return human

    for index, items in enumerate(friends):
        yield recusion(Human(index), items).friends


def roop_width(friends, maxtimes=2):
    def roop(human, items):
        temp = []
        for i, h in enumerate(items):
            if h == 'Y' and human.index != i:
                temp.append(i)
        return temp

    tmp = []
    for index, items in enumerate(friends):
        human = Human(index)
        for i in roop(human, items):
            human.friends.add(i)
        tmp.append(human)
    times = 0
    while True:
        times += 1
        if times >= maxtimes:
            break
        for human in tmp:
            temp = []
            for i in human.friends:
                temp.extend(roop(human, friends[i]))
            for i in temp:
                human.friends.add(i)
    return [x.friends for x in tmp]


def main():
    print list(recursion_depth(friends2))
    print roop_width(friends2)


if __name__ == '__main__':
    main()
