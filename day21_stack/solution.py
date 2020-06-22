import time


def solution():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = []
    max_len = len(a)
    switch = False
    while True:
        if len(a) == 0 or len(b) == 0:
            switch = not switch

        # print('-'*30)
        if switch:
            b.append(a.pop())
            for i in range(max_len -1, -1, -1):
                print('[{}] [{}]'.format(' ' if len(a) <= i else a[i], ' ' if len(b) <= i else b[i]))
        else:
            a.append(b.pop())
            for i in range(max_len -1, -1, -1):
                print('[{}] [{}]'.format(' ' if len(a) <= i else a[i], ' ' if len(b) <= i else b[i]))

        time.sleep(0.3)

