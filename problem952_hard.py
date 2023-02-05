# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/5 21:39
"""
from collections import Counter
from typing import List

"""
给定一个由不同正整数的组成的非空数组 nums ，考虑下面的图：
    有 nums.length 个节点，按从 nums[0] 到 nums[nums.length - 1] 标记；
    只有当 nums[i] 和 nums[j] 共用一个大于 1 的公因数时，nums[i] 和 nums[j]之间才有一条边。
返回 图中最大连通组件的大小 。

示例 1：
输入：nums = [4,6,15,35]
输出：4

示例 2：
输入：nums = [20,50,9,63]
输出：2

示例 3：
输入：nums = [2,3,6,7,4,12,21,39]
输出：8
"""
"""
思路：并查集。为了得到数组 nums 中的每个数和哪些数属于同一个组件，需要得到数组 nums 中的最大值 m，对于每个不超过 m 的正整数 
num 计算 num 和哪些数属于同一个组件。对于范围 [2, √num] 内的每个正整数 i，如果 i 是 num 的因数，则 num 和 i、i/num 都属于
同一个组件。
可以使用并查集实现组件的计算。初始时，每个数分别属于不同的组件。如果两个正整数满足其中一个正整数是另一个正整数的因数，则这两个
正整数属于同一个组件，将这两个正整数的组件合并。当所有不超过 m 的正整数都完成合并操作之后。遍历数组 nums，对于每个数得到其所在
的组件并更新该组件的大小，遍历结束之后即可得到最大组件的大小。
"""


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x: int, y: int) -> None:
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            self.rank[x] += 1


class Solution:
    @staticmethod
    def largestComponentSize(nums: List[int]) -> int:
        uf = UnionFind(max(nums) + 1)
        for num in nums:
            i = 2
            while i * i <= num:
                if num % i == 0:
                    uf.merge(num, i)
                    uf.merge(num, num // i)
                i += 1
        return max(Counter(uf.find(num) for num in nums).values())
