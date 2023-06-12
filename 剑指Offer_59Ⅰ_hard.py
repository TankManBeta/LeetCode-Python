# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/11 15:15
"""
import collections
from typing import List

"""
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 
  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""
"""
思路：若 i>0 且 队首元素 deque[0] = 被删除元素 nums[i−1] ：则队首元素出队；删除 deque 内所有 <nums[j] 的元素，以保持 deque 
递减；将 nums[j] 添加至 deque 尾部；若已形成窗口（即 i≥0 ）：将窗口最大值（即队首元素 deque[0] ）添加至列表 res 。
"""


class Solution:
    @staticmethod
    def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        res, n = [], len(nums)
        for i, j in zip(range(1 - k, n + 1 - k), range(n)):
            # 删除 deque 中对应的 nums[i-1]
            if i > 0 and deque[0] == nums[i - 1]:
                deque.popleft()
            # 保持 deque 递减
            while deque and deque[-1] < nums[j]:
                deque.pop()
            deque.append(nums[j])
            # 记录窗口最大值
            if i >= 0:
                res.append(deque[0])
        return res
