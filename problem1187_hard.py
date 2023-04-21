# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/4/20 11:34
"""
from bisect import bisect_left
from math import inf
from typing import List

"""
给你两个整数数组 arr1 和 arr2，返回使 arr1 严格递增所需要的最小「操作」数（可能为 0）。
每一步「操作」中，你可以分别从 arr1 和 arr2 中各选出一个索引，分别为 i 和 j，0 <= i < arr1.length 和 0 <= j < arr2.length，
然后进行赋值运算 arr1[i] = arr2[j]。
如果无法让 arr1 严格递增，请返回 -1。 

示例 1：
输入：arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
输出：1
解释：用 2 来替换 5，之后 arr1 = [1, 2, 3, 6, 7]。

示例 2：
输入：arr1 = [1,5,3,6,7], arr2 = [4,3,1]
输出：2
解释：用 3 来替换 5，然后用 4 来替换 3，得到 arr1 = [1, 3, 4, 6, 7]。

示例 3：
输入：arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
输出：-1
解释：无法使 arr1 严格递增。
"""
"""
思路：动态规划，我们定义 f[i] 为数组前i个转换为严格递增且保留arr1[i]所需要的最少操作数。因此，我们在 arr1 设置首尾两个哨兵 −∞ 
和 ∞。最后一个数一定是不替换，因此 f[n−1] 即为答案。我们初始化 f[0]=0，其余 f[i]=∞。接下来我们对数组 arr2 进行排序并去重，方便
进行二分查找。如果 arr1[i−1]<arr1[i]，那么 f[i] 可以从 f[i−1] 转移而来，即 f[i]=f[i−1]。然后，我们考虑 arr[i−1] 替换的情况，
显然 arr[i−1] 应该替换成一个尽可能大的、且比 arr[i] 小的数字，我们在数组 arr2 中进行二分查找，找到第一个大于等于 arr[i] 的下标 
j。然后我们在 k∈[1,min(i−1,j)] 的范围内枚举替换的个数，如果满足 arr[i−k−1]<arr2[j−k]，我们就可以找到连续的k个替换arr中的连续
K个，那么 f[i] 可以从 f[i−k−1] 转移而来，即 f[i]=min(f[i],f[i−k−1]+k)。
"""


class Solution:
    @staticmethod
    def makeArrayIncreasing(arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))
        arr = [-inf] + arr1 + [inf]
        n = len(arr)
        f = [inf] * n
        f[0] = 0
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                f[i] = f[i-1]
            j = bisect_left(arr2, arr[i])
            for k in range(1, min(i - 1, j) + 1):
                if arr[i - k - 1] < arr2[j - k]:
                    f[i] = min(f[i], f[i - k - 1] + k)
        return -1 if f[n - 1] >= inf else f[n - 1]
