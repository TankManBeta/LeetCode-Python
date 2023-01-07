# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/7 20:13
"""
from typing import List

"""
给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。
请注意，需要 修改 数组以供接下来的操作使用。
如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。

示例 1：
输入：nums = [1,1,4,2,3], x = 5
输出：2
解释：最佳解决方案是移除后两个元素，将 x 减到 0 。

示例 2：
输入：nums = [5,6,7,8,9], x = 4
输出：-1

示例 3：
输入：nums = [3,2,20,1,1,3], x = 10
输出：5
解释：最佳解决方案是移除后三个元素和前两个元素（总共 5 次操作），将 x 减到 0 。
"""
"""
思路：
（1）dfs，超时
（2）就是找一个前缀和+后缀和，看他们的和能否为x。所以我们left初值指向-1，right指向0，表示当前前缀和为0，后缀和为nums的总和，
然后如果当前的前后缀的和大于x，就把right往后移，减小sum；否则就把left往后移，增大sum
（3）类似思路，要从 nums 中找最长的子数组，其元素和等于 s−x，这里 s 为 nums 所有元素之和。每次把当前num加进和中，如果sum>x，则
将left右移，sum -= nums[left]
"""


class Solution:
    @staticmethod
    def minOperations(nums: List[int], x: int) -> int:
        # self.ans = x
        # self.flag = False
        # @lru_cache()
        # def dfs(start, end, count, remain):
        #     if start > end or remain <= 0:
        #         if remain == 0:
        #             self.ans = min(self.ans, count)
        #             self.flag = True
        #         return
        #     dfs(start+1, end, count+1, remain-nums[start])
        #     dfs(start, end-1, count+1, remain-nums[end])
        # dfs(0, len(nums)-1, 0, x)
        # return self.ans if self.flag else -1

        # n = len(nums)
        # ans = n+1
        # total = sum(nums)
        # if total < x:
        #     return -1
        # r = 0
        # l_sum, r_sum = 0, total
        # for l in range(-1, n-1):
        #     if l != -1:
        #         l_sum += nums[l]
        #     while r < n and l_sum + r_sum > x:
        #         r_sum -= nums[r]
        #         r += 1
        #     if l_sum + r_sum == x:
        #         ans = min(ans, (l + 1) + (n - r))

        # return -1 if ans > n else ans

        target = sum(nums) - x
        if target < 0:
            return -1
        ans = -1
        left = s = 0
        for right, x in enumerate(nums):
            s += x
            while s > target:  # 缩小子数组长度
                s -= nums[left]
                left += 1
            if s == target:
                ans = max(ans, right - left + 1)
        return -1 if ans < 0 else len(nums) - ans
