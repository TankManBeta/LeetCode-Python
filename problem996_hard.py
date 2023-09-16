# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/9/13 14:18
"""
import math
from itertools import permutations

nums = [1, 8, 17]
n = len(nums)
pers = permutations(nums)
ans = set()
for per in pers:
    flag = True
    for i in range(n-1):
        prod = per[i] + per[i+1]
        root = int(math.sqrt(prod))
        if root * root != prod:
            flag = False
            break
    if flag:
        ans.add(per)
print(len(ans))