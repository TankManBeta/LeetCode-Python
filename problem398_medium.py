# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/25 12:49
"""
from random import randrange

"""
给定一个可能含有重复元素的整数数组，要求随机输出给定的数字的索引。 您可以假设给定的数字一定存在于数组中。
注意：
数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);
// pick(3) 应该返回索引 2,3 或者 4。每个索引的返回概率应该相等。
solution.pick(3);
// pick(1) 应该返回 0。因为只有nums[0]等于1。
solution.pick(1);
"""
"""
思路：水塘抽样，遍历nums，当我们第 i 次遇到值为 target 的元素时，随机选择区间 [0,i) 内的一个整数，如果其等于 0，
则将返回值置为该元素的下标，否则返回值不变。
设 nums 中有 k 个值为 target 的元素，该算法会保证这 k 个元素的下标成为最终返回值的概率均为 1/k
"""


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        ans = cnt = 0
        for i, num in enumerate(self.nums):
            if num == target:
                cnt += 1  # 第 cnt 次遇到 target
                if randrange(cnt) == 0:
                    ans = i
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
