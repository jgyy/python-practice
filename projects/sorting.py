"""
Sorting - Implement two types of sorting algorithms: Merge sort and bubble sort
"""
import random


def merge(lst0, lst1):
    """
    :param lst0:
    :param lst1:
    :return:
    """
    ret = []
    while lst0 and lst1:
        if lst0[0] <= lst1[0]:
            ret.append(lst0.pop(0))
        else:
            ret.append(lst1.pop(0))
    ret.extend(lst0)
    ret.extend(lst1)
    return ret


def merge_sort(last):
    """
    :param last: random to avoid dead loop for special sequence
    :return:
    """
    if len(last) <= 1:
        return last
    random_num = last[random.randint(0, len(last) - 1)]
    left, mid, right = [], [], []
    for i in last:
        if i < random_num:
            left.append(i)
        elif i == random_num:
            mid.append(i)
        else:
            right.append(i)
    left = merge_sort(left)
    left.extend(mid)
    right = merge_sort(right)
    ret = merge(left, right)
    return ret


if __name__ == "__main__":
    print("please input integer number array")
    LST = []
    while 1:
        try:
            N = input("> ")
            LST.extend([int(i) for i in N.split()])
        except ValueError:
            print("")
            break
    print("origin: ", LST)
    print("sorted: ", merge_sort(LST))
