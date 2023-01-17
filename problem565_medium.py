# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/16 21:07
"""
from typing import List

"""
索引从0开始长度为N的数组A，包含0到N - 1的所有整数。找到最大的集合S并返回其大小，其中 S[i] = {A[i], A[A[i]], A[A[A[i]]], ... }
且遵守以下的规则。假设选择索引为i的元素A[i]为S的第一个元素，S的下一个元素应该是A[A[i]]，之后是A[A[A[i]]]... 以此类推，不断添加
直到S出现重复的元素。

示例 1:
输入: A = [5,4,0,3,1,6,2]
输出: 4
解释: 
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.
其中一种最长的 S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
"""
"""
思路：遍历数组，从 i 向 nums[i] 连边，我们可以得到一张有向图。由于题目保证 nums 中不含有重复的元素，因此有向图中每个点的出度和
入度均为 1。在这种情况下，有向图必然由一个或多个环组成。我们可以遍历 nums，找到节点个数最大的环。代码实现时需要用一个 vis 数组
来标记访问过的节点。
"""


class Solution:
    @staticmethod
    def arrayNesting(nums: List[int]) -> int:
        ans, n = 0, len(nums)
        vis = [False] * n
        for i in range(n):
            cnt = 0
            while not vis[i]:
                vis[i] = True
                i = nums[i]
                cnt += 1
            ans = max(ans, cnt)
        return ans
