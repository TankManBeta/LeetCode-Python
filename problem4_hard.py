# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/10/28 10:47
"""
"""
给定两个大小分别为m和n的正序（从小到大）数组nums1和nums2。请你找出并返回这两个正序数组的中位数。

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数2

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000

输入：nums1 = [], nums2 = [1]
输出：1.00000

输入：nums1 = [2], nums2 = []
输出：2.00000
"""
"""
思路：
（1）先对数组进行升序合并，再根据数组长度取中间那个数或者中间两个数求平均。
（2）创建新数组，升序排列数组，当数组长度达到中位数计算需要的数量即可，后面的可以不用继续排列。
"""


class Solution(object):
    @staticmethod
    def find_median_sorted_arrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            else:
                nums1.insert(i, nums2[j])
                j += 1
        if j < len(nums2):
            nums1 = nums1 + nums2[j:]
        new_len_nums1 = len(nums1)
        if new_len_nums1 % 2 == 0:
            return (nums1[new_len_nums1/2] + nums1[new_len_nums1/2-1])/float(2)
        else:
            return nums1[new_len_nums1/2]


# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         i = 0
#         j = 0
#         len_nums1 = len(nums1)
#         len_nums2 = len(nums2)
#         len_all = len_nums1 + len_nums2
#         result_len = len_all/2 + 1
#         result_list = []
#         while len(result_list) != result_len:
#             if i == len_nums1:
#                 result_list.append(nums2[j])
#                 j += 1
#             elif j == len_nums2:
#                 result_list.append(nums1[i])
#                 i += 1
#             else:
#                 if nums1[i] < nums2[j]:
#                     result_list.append(nums1[i])
#                     i += 1
#                 else:
#                     result_list.append(nums2[j])
#                     j += 1
#         if len_all % 2 == 0 :
#             return (result_list[-1] + result_list[-2]) / float(2)
#         else:
#             return result_list[-1]