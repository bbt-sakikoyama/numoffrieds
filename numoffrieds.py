# -*- coding:utf-8 -*-

friends = [
        'NYNNN',
        'YNYNN',
        'NYNYN',
        'NNYNY',
        'NNNYN'
    ]


def recursion_depth():
    def execute(fIndex, friend, times=0):
        _times = times + 1
        for hIndex, human in enumerate(friend):
            # 再帰時にhuman自身をfriendとしてカウントさせない
            if human == 'Y' and fIndex != hIndex:
                # 再帰は1回だけ
                if _times < 2:
                    for tpl in execute(fIndex, friends[hIndex], _times):
                        yield tpl
                yield (fIndex, hIndex)

    for fIndex, friend in enumerate(friends):
        yield list(execute(fIndex, friend))


def recursion_width():
    def execute(friends, times=0):
        _times = times + 1
        _friendsList = []
        for fIndex, friend in enumerate(friends):
            _friends = []
            for hIndex, human in enumerate(friend):
                if human == 'Y' and fIndex != hIndex:
                    if _times < 2:
                        _friends.append(friends[hIndex])
                    yield (fIndex, hIndex)
            _friendsList.append(_friends)

        for fs in _friendsList:
            for tpl in execute(fs, _times):
                yield tpl

    return set(execute(friends))


def depth():
    pass


def width():
    pass


def main():
    print list(recursion_depth())
    print recursion_width()


if __name__ == '__main__':
    main()
