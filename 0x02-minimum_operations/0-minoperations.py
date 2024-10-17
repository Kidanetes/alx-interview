#!/usr/bin/python3
"""minimum operation to reach n character"""


def minOperations(n):
    """this function returns the minmum opration to
    reach n characters"""
    list1 = [1]
    n = n - 1
    i = 0
    while n > 0:
        if i > 0:
            if 2 * list1[i] <= n:
                n = n - 2 * list1[i]
                list1.append(2 * list1[i])
                i = i + 1
            elif list1[i] + list1[i - 1] <= n:
                n = n - list1[i] + list1[i - 1]
                list1.append(list1[i] + list1[i - 1])
                i = i + 1
            else:
                x = list1.copy()
                x.reverse()
                for j in x:
                    if j <= n:
                        n = n - j
                        list1.append(j)
                        i = i + 1
        else:
            if n >= 2:
                list1.append(2)
                n = n - 2
                i = i + 1
    list1.sort()
    copy_all = 0
    paste = 0
    for i in range(1, len(list1)):
        if copy_all == 0:
            copy_all = 1
            paste = paste + 1
        else:
            if list1[i] == list1[i - 1]:
                paste = paste + 1
            else:
                copy_all = copy_all + 1
                paste = paste + 1
    return copy_all + paste
