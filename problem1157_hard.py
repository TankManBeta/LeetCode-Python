# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/4/16 15:21
"""
import random
from bisect import bisect_right, bisect_left
from collections import defaultdict
from typing import List

"""
设计一个数据结构，有效地找到给定子数组的 多数元素 。
子数组的 多数元素 是在子数组中出现 threshold 次数或次数以上的元素。
实现 MajorityChecker 类:
    MajorityChecker(int[] arr) 会用给定的数组 arr 对 MajorityChecker 初始化。
    int query(int left, int right, int threshold) 返回子数组中的元素  arr[left...right] 至少出现 threshold 次数，
    如果不存在这样的元素则返回 -1。

示例 1：
输入:
["MajorityChecker", "query", "query", "query"]
[[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]
输出：
[null, 1, -1, 2]
解释：
MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
majorityChecker.query(0,5,4); // 返回 1
majorityChecker.query(0,3,3); // 返回 -1
majorityChecker.query(2,3,2); // 返回 2
"""
"""
思路：
（1）位运算，非常巧妙的算法。由题目已知条件可知，1<=arr[i]<=20000，转化为二进制最多15位，所以对于arr中的数，我们用前缀和统计
每个数二进制表示中1和0的数目。也就会得到一个15×n的数组A，15代表的是每一位，n代表的是arr数组的长度。查询的时候对每个位判断一下，
用该位的前缀和，可以在O(1)时间获得此位在区间中1/0出现的次数。比如我们要查询的left=2，right=5，所以我们就遍历A中的每一个数组，
然后用A[i][right]-A[i][left]看有多少个1。（1）如果此位中1出现的次数>=threshold，则返回值val的这一位一定是1；（2）如果此位中0
出现的次数>=threshold，则返回值val的这一位一定是0；（3）如果1和0出现的次数都<threshold，直接返回-1。如果15位均没有因为（3）退出，
对得到的val二分判断一下，如果val在区间内的次数确实>=threshold，返回val；否则返回-1。
（2）线段树 + 摩尔投票 + 二分查找。我们注意到，题目需要我们找出特定区间内可能的众数，考虑使用线段树来维护每个区间内的候选众数
以及其出现的次数。
我们定义线段树的每个节点为 Node，每个节点包含如下属性：
    l：节点的左端点，下标从 1 开始。
    r：节点的右端点，下标从 1 开始。
    x：节点的候选众数。
    cnt：节点的候选众数出现的次数。
线段树主要有以下几个操作：
    build(u, l, r)：建立线段树。
    pushup(u)：用子节点的信息更新父节点的信息。
    query(u, l, r)：查询区间和。
在主函数的初始化方法中，我们先创建一个线段树，并且用哈希表 d 记录每个元素在数组中的所有下标。
在 query(left, right, threshold) 方法中，我们直接调用线段树的 query 方法，得到候选众数 x。然后使用二分查找，找到 x 在数组中
第一个大于等于 left 的下标 l，以及第一个大于 right 的下标 r。如果 r−l≥threshold，则返回 x，否则返回 −1。
（3）随机化 + 二分查找。记录下所有数出现的位置，然后随机在区间中取数，看是否是出现次数最多的数，次数越多结果越准确。
"""


# M = 15
# A = [None] * M
# mp = defaultdict(list)
# class MajorityChecker:
#     def __init__(self, arr: List[int]):
#         mp.clear()
#         for i,x in enumerate(arr):
#             mp[x].append(i)
#         for i in range(M):
#             A[i] = [0] + list(accumulate(x >> i & 1 for x in arr))

#     def query(self, left: int, right: int, threshold: int) -> int:
#         val = 0
#         right += 1
#         for i,a in enumerate(A):
#             one = a[right] - a[left]
#             if one >= threshold:
#                 val |= 1 << i
#             elif right - left  - one < threshold:
#                 return -1
#         return [val,-1][bisect_left(mp[val],right) - bisect_left(mp[val],left) < threshold]


# class Node:
#     def __init__(self):
#         self.l = self.r = 0
#         self.x = self.cnt = 0


# class SegmentTree:
#     def __init__(self, nums):
#         self.nums = nums
#         n = len(nums)
#         self.tr = [Node() for _ in range(n << 2)]
#         self.build(1, 1, n)

#     def build(self, u, l, r):
#         self.tr[u].l, self.tr[u].r = l, r
#         if l == r:
#             self.tr[u].x = self.nums[l - 1]
#             self.tr[u].cnt = 1
#             return
#         mid = (l + r) >> 1
#         self.build(u << 1, l, mid)
#         self.build(u << 1 | 1, mid + 1, r)
#         self.pushup(u)

#     def query(self, u, l, r):
#         if self.tr[u].l >= l and self.tr[u].r <= r:
#             return self.tr[u].x, self.tr[u].cnt
#         mid = (self.tr[u].l + self.tr[u].r) >> 1
#         if r <= mid:
#             return self.query(u << 1, l, r)
#         if l > mid:
#             return self.query(u << 1 | 1, l, r)
#         x1, cnt1 = self.query(u << 1, l, r)
#         x2, cnt2 = self.query(u << 1 | 1, l, r)
#         if x1 == x2:
#             return x1, cnt1 + cnt2
#         if cnt1 >= cnt2:
#             return x1, cnt1 - cnt2
#         else:
#             return x2, cnt2 - cnt1

#     def pushup(self, u):
#         if self.tr[u << 1].x == self.tr[u << 1 | 1].x:
#             self.tr[u].x = self.tr[u << 1].x
#             self.tr[u].cnt = self.tr[u << 1].cnt + self.tr[u << 1 | 1].cnt
#         elif self.tr[u << 1].cnt >= self.tr[u << 1 | 1].cnt:
#             self.tr[u].x = self.tr[u << 1].x
#             self.tr[u].cnt = self.tr[u << 1].cnt - self.tr[u << 1 | 1].cnt
#         else:
#             self.tr[u].x = self.tr[u << 1 | 1].x
#             self.tr[u].cnt = self.tr[u << 1 | 1].cnt - self.tr[u << 1].cnt


# class MajorityChecker:

#     def __init__(self, arr: List[int]):
#         self.tree = SegmentTree(arr)
#         self.d = defaultdict(list)
#         for i, x in enumerate(arr):
#             self.d[x].append(i)

#     def query(self, left: int, right: int, threshold: int) -> int:
#         x, _ = self.tree.query(1, left + 1, right + 1)
#         l = bisect_left(self.d[x], left)
#         r = bisect_left(self.d[x], right + 1)
#         return x if r - l >= threshold else -1


class MajorityChecker:
    def __init__(self, arr: List[int]):
        self.arr, self.dct = arr, defaultdict(list)
        for i, x in enumerate(arr):
            self.dct[x].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(30):
            x = self.arr[random.randint(left, right)]
            if bisect_right(self.dct[x], right) - bisect_left(self.dct[x], left) >= threshold:
                return x
        return -1

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
