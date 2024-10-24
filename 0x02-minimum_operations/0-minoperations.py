#!/usr/bin/python3
"""minimum operation to reach n character"""


def minOperations(n):
    """this function returns the minmum opration to
    reach n characters"""
    if n <= 1:
        return 0
    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations
