# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/22 10:30
"""


def gcd(a, b):
    if a < b:
        a, b = b, a
    if 0 == b:
        return a
    if a % 2 == 0 and b % 2 == 0:
        return 2 * gcd(a//2, b//2)
    if a % 2 == 0:
        return gcd(a // 2, b)
    if b % 2 == 0:
        return gcd(a, b // 2)
    # 传统Stein算法
    return gcd(a-b, b)
    # 改进Stein算法（某些情况下可以降低复杂度）
    # return gcd((a + b) // 2, (a - b) // 2)

