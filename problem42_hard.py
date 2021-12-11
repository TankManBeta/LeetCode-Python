# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/10 10:49
"""
"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 

输入：height = [4,2,0,3,2,5]
输出：9
"""
"""
思路：
（1）一开始自己想的思路，每次看一行，为0就ans+1，最后超时
（2）看评论，每次求一列，找当前列左边最矮的和右边最矮的，如果两个里面最矮的小于等于当前列的高度，则当前列不可能有水，
否则ans += (min_height-height[i])，同样超时
（3）在（2）的基础上维护两个数组，一个用来记录当前位置左边的最高高度，一个用来记录当前位置右边的最高高度，剩下的同（2）
"""


# class Solution(object):
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         ans = 0
#         max_height = max(height)
#         for i in range(0, max_height):
#             start = -1
#             end = -1
#             for j in range(0, len(height)):
#                 if height[j] > 0:
#                     start = j
#                     break
#             for j in range(len(height)-1,-1,-1):
#                 if height[j] > 0:
#                     end = j
#                     break
#             print(start, end)
#             for index in range(start, end+1):
#                 if height[index] == 0:
#                     ans += 1
#                 else:
#                     height[index] -= 1
#         return ans


# class Solution(object):
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         ans = 0
#         len_height = len(height)
#         for i in range(1, len_height - 1):
#             left_max = 0
#             for j in range(i - 1, -1, -1):
#                 if height[j] > left_max:
#                     left_max = height[j]
#
#             right_max = 0
#             for j in range(i + 1, len_height):
#                 if height[j] > right_max:
#                     right_max = height[j]
#
#             min_height = min(left_max, right_max)
#
#             if min_height > height[i]:
#                 ans += min_height - height[i]
#
#         return ans

class Solution(object):
    @staticmethod
    def trap(height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        height_len = len(height)
        left_height = [0 for _ in range(0, height_len)]
        right_height = [0 for _ in range(0, height_len)]
        for i in range(1, height_len):
            left_height[i] = max(height[i - 1], left_height[i - 1])
        for i in range(height_len - 2, -1, -1):
            right_height[i] = max(height[i + 1], right_height[i + 1])

        for i in range(1, height_len - 1):
            min_height = min(left_height[i], right_height[i])
            if min_height > height[i]:
                ans += min_height - height[i]
        return ans
