# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/20 13:09
"""
"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋
的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

输入：[3,2,3]
输出：3

输入：[2,2,1,1,1,2,2]
输出：2
"""
"""
思路：
（1）哈希表计数
（2）排序之后取中间那个
（3）摩尔投票法，遇到相同的数，就投一票，遇到不同的数，就减一票，最后还存在票的数就是众数
"""


class Solution(object):
    @staticmethod
    def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # hash_dict = {}
        # for num in nums:
        #     hash_dict[num] = hash_dict.get(num, 0)+1
        # return max(hash_dict.keys(), key=hash_dict.get)

        # nums.sort()
        # return nums[len(nums) // 2]

        count, res = 0, -1
        for num in nums:
            if count == 0:
                res = num
            if num == res:
                count += 1
            else:
                count -= 1
        return res
