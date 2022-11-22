# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/21 11:49
"""
from typing import List

"""
给你一个大小为 m x n 的二维整数网格 grid 和一个整数 x 。每一次操作，你可以对 grid 中的任一元素 加 x 或 减 x 。
单值网格 是全部元素都相等的网格。
返回使网格化为单值网格所需的 最小 操作数。如果不能，返回 -1 。

示例 1：
输入：grid = [[2,4],[6,8]], x = 2
输出：4
解释：可以执行下述操作使所有元素都等于 4 ： 
- 2 加 x 一次。
- 6 减 x 一次。
- 8 减 x 两次。
共计 4 次操作。

示例 2：
输入：grid = [[1,5],[2,3]], x = 1
输出：5
解释：可以使所有元素都等于 3 。

示例 3：
输入：grid = [[1,2],[3,4]], x = 2
输出：-1
解释：无法使所有元素相等。
"""
"""
思路：首先将数组转化为一维数组的形式，如果有解的话，任意两个数字之间的差肯定是x的倍数。然后对数组进行排序，求中位数，然后再累加
差的绝对值除以x的值即可。（问题是为什么是中位数步数最少？）对于任意三个数而言，如果他们之间能到达的话，左右端点走的步数和其实是
定值，所有就需要看中间点到最后解的距离，很明显取自身走的路程要小。
"""


class Solution:
    @staticmethod
    def minOperations(grid: List[List[int]], x: int) -> int:
        m = len(grid)
        n = len(grid[0])
        nums = []
        for i in range(m):
            for j in range(n):
                nums.append(grid[i][j])
        for num in nums:
            if (num-nums[0]) % x != 0:
                return -1
        mid = (m*n) //2
        ans = 0
        for num in nums:
            ans += abs(num-nums[mid]) // x
        return ans
