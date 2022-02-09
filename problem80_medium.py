# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/9 10:55
"""
"""
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 最多出现两次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。 不需要考虑数组中超出新长度后面的元素。

输入：nums = [0,0,1,1,1,1,2,3,3]
输出：7, nums = [0,0,1,1,2,3,3]
解释：函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。不需要考虑数组中超出新长度后面的元素。
"""
"""
思路：
（1）顺序遍历，找到第一个不等于当前数字的数，后面的全都复制过来
（2）快慢指针
"""


class Solution(object):
    @staticmethod
    def remove_duplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count_dict = {}
        # i = 0
        # nums_len = len(nums)
        # while i < nums_len:
        #     if count_dict.get(nums[i],0)==2:
        #         j = i+1
        #         if j > nums_len-1:
        #             return i
        #         else:
        #             temp_i = i
        #             temp_count = 0
        #             temp_num = nums[i]
        #             for k in range(temp_i, nums_len):
        #                 if nums[k] == temp_num:
        #                     temp_count += 1
        #                 else:
        #                     nums[temp_i] = nums[k]
        #                     temp_i += 1
        #             nums_len -= temp_count
        #     else:
        #         count_dict[nums[i]] = count_dict.get(nums[i],0)+1
        #         i += 1
        # return nums_len

        j = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1
        return j
