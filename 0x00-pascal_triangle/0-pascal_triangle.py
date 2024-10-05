#!/usr/bin/python3
""" this module will contain a function which will
give us pascal triangle"""

def pascal_triangle(n):
    """ This function will return pascal
    triangle"""
    list_intial = []
    if n <= 0:
        return list_intial
    list_intial.append([1])
    for i in range(1, n):
        if i == 1:
            list_intial.append([1,1])
        else:
            list1 = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    list1.append(1)
                else:
                    list1.append(list_intial[i- 1][j-1] + list_intial[i - 1][j])
            list_intial.append(list1)
    return list_intial
        
