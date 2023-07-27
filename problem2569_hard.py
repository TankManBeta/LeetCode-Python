# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/7/26 23:34
"""
from typing import List

"""
给你两个下标从 0 开始的数组 nums1 和 nums2 ，和一个二维数组 queries 表示一些操作。总共有 3 种类型的操作：
操作类型 1 为 queries[i] = [1, l, r] 。你需要将 nums1 从下标 l 到下标 r 的所有 0 反转成 1 或将 1 反转成 0 。l 和 r 下标都从 0 开始。
操作类型 2 为 queries[i] = [2, p, 0] 。对于 0 <= i < n 中的所有下标，令 nums2[i] = nums2[i] + nums1[i] * p 。
操作类型 3 为 queries[i] = [3, 0, 0] 。求 nums2 中所有元素的和。
请你返回一个数组，包含所有第三种操作类型的答案。 

示例 1：
输入：nums1 = [1,0,1], nums2 = [0,0,0], queries = [[1,1,1],[2,1,0],[3,0,0]]
输出：[3]
解释：第一个操作后 nums1 变为 [1,1,1] 。第二个操作后，nums2 变成 [1,1,1] ，所以第三个操作的答案为 3 。所以返回 [3] 。

示例 2：
输入：nums1 = [1], nums2 = [5], queries = [[2,0,0],[3,0,0]]
输出：[5]
解释：第一个操作后，nums2 保持不变为 [5] ，所以第二个操作的答案是 5 。所以返回 [5] 。
"""
"""
思路：根据题目描述：

操作 1 是把数组 nums1 的下标区间 [l,..r] 的所有数反转，即把 0 变成 1，把 1 变成 0。
操作 3 是求数组 nums2 的所有数之和。
操作 2 是把数组 nums2 的所有数之和加上 p 乘以数组 nums1 所有数之和，即 sum(nums2)=sum(nums2)+p∗sum(nums1)。
因此，我们实际上只需要维护数组 nums1 的区间和即可，我们可以通过线段树来实现。
我们定义线段树的每个节点为 Node，每个节点包含如下属性：
    l：节点的左端点，下标从 1 开始。
    r：节点的右端点，下标从 1 开始。
    s：节点的区间和。
    lazy：节点的懒标记。
线段树主要有以下几个操作：
    build(u, l, r)：建立线段树。
    pushdown(u)：下传懒标记。
    pushup(u)：用子节点的信息更新父节点的信息。
    modify(u, l, r)：修改区间和，本题中是反转区间中的每个数，那么区间和 s=r−l+1−s
    query(u, l, r)：查询区间和。
我们先算出数组 nums2 的所有数之和，记为 s。
执行操作 1 时，我们只需要调用 modify(1,l+1,r+1) 即可。
执行操作 2 时，我们更新 s=s+p×query(1,1,n) 即可。
执行操作 3 时，我们只需要将 s 加入答案数组即可。
"""


class Node:
    def __init__(self):
        self.l = self.r = 0
        self.s = self.lazy = 0


class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        n = len(nums)
        self.tr = [Node() for _ in range(n << 2)]
        self.build(1, 1, n)

    def build(self, u, l, r):
        self.tr[u].l, self.tr[u].r = l, r
        if l == r:
            self.tr[u].s = self.nums[l - 1]
            return
        mid = (l + r) >> 1
        self.build(u << 1, l, mid)
        self.build(u << 1 | 1, mid + 1, r)
        self.pushup(u)

    def modify(self, u, l, r):
        if self.tr[u].l >= l and self.tr[u].r <= r:
            self.tr[u].lazy ^= 1
            self.tr[u].s = self.tr[u].r - self.tr[u].l + 1 - self.tr[u].s
            return
        self.pushdown(u)
        mid = (self.tr[u].l + self.tr[u].r) >> 1
        if l <= mid:
            self.modify(u << 1, l, r)
        if r > mid:
            self.modify(u << 1 | 1, l, r)
        self.pushup(u)

    def query(self, u, l, r):
        if self.tr[u].l >= l and self.tr[u].r <= r:
            return self.tr[u].s
        self.pushdown(u)
        mid = (self.tr[u].l + self.tr[u].r) >> 1
        res = 0
        if l <= mid:
            res += self.query(u << 1, l, r)
        if r > mid:
            res += self.query(u << 1 | 1, l, r)
        return res

    def pushup(self, u):
        self.tr[u].s = self.tr[u << 1].s + self.tr[u << 1 | 1].s

    def pushdown(self, u):
        if self.tr[u].lazy:
            mid = (self.tr[u].l + self.tr[u].r) >> 1
            self.tr[u << 1].s = mid - self.tr[u].l + 1 - self.tr[u << 1].s
            self.tr[u << 1].lazy ^= 1
            self.tr[u << 1 | 1].s = self.tr[u].r - mid - self.tr[u << 1 | 1].s
            self.tr[u << 1 | 1].lazy ^= 1
            self.tr[u].lazy ^= 1


class Solution:
    @staticmethod
    def handleQuery(
            nums1: List[int], nums2: List[int], queries: List[List[int]]
    ) -> List[int]:
        tree = SegmentTree(nums1)
        s = sum(nums2)
        ans = []
        for op, a, b in queries:
            if op == 1:
                tree.modify(1, a + 1, b + 1)
            elif op == 2:
                s += a * tree.query(1, 1, len(nums1))
            else:
                ans.append(s)
        return ans
