# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/22 10:30
"""


def gcd(a, b):
    m, n = max(a, b), min(a, b)
    for i in range(n, 0, -1):
        if m % i == 0 and n % i == 0:
            return i
    return 1


a = gcd(2, 12)
print(a)
