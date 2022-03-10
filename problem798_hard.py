# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/9 11:04
"""
"""
给你一个数组 nums，我们可以将它按一个非负整数 k 进行轮调，这样可以使数组变为 [nums[k], nums[k + 1], ... nums[nums.length-1], 
nums[0], nums[1], ..., nums[k-1]] 的形式。此后，任何值小于或等于其索引的项都可以记作一分。
例如，数组为nums=[2,4,1,3,0]，我们按k = 2进行轮调后，它将变成 [1,3,0,2,4]。这将记为3分，因为 1 > 0 [不计分]、3 > 1 [不计分]、
0 <= 2 [计 1 分]、2 <= 3 [计 1 分]，4 <= 4 [计 1 分]。
在所有可能的轮调中，返回我们所能得到的最高分数对应的轮调下标 k 。如果有多个答案，返回满足条件的最小的下标 k 。

输入：nums = [2,3,1,4,0]
输出：3
解释：
下面列出了每个 k 的得分：
k = 0,  nums = [2,3,1,4,0],    score 2
k = 1,  nums = [3,1,4,0,2],    score 3
k = 2,  nums = [1,4,0,2,3],    score 3
k = 3,  nums = [4,0,2,3,1],    score 4
k = 4,  nums = [0,2,3,1,4],    score 3
所以我们应当选择 k = 3，得分最高。

输入：nums = [1,3,0,2,4]
输出：0
解释：
nums 无论怎么变化总是有 3 分。
所以我们将选择最小的 k，即 0。
"""
"""
思路：思路是对每一个数，算出他能得分的调动k的范围，然后找最大值的最小下标即可，实现没有成功。当i<x时应将的下标范围 [i+1,i−x+n]
内的所有元素加1，当i≥x时应将 下标范围 [0,i+1] 和 [i−x,n−1] 内的所有元素加 1。由于是将一段或两段连续下标范围内的元素加 1，
因此可以使用差分数组实现。
"""


class Solution(object):
    @staticmethod
    def best_rotation(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        diffs = [0] * n
        for i, num in enumerate(nums):
            low = (i + 1) % n
            high = (i - num + n + 1) % n
            diffs[low] += 1
            diffs[high] -= 1
            if low >= high:
                diffs[0] += 1

        score, max_score, idx = 0, 0, 0
        for i, diff in enumerate(diffs):
            score += diff
            if score > max_score:
                max_score, idx = score, i
        return idx
