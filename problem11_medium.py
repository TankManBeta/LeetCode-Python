# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/11/30 19:09
"""
"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器。

输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

输入：height = [1,1]
输出：1

输入：height = [4,3,2,1,4]
输出：16

输入：height = [1,2,1]
输出：2
"""
"""
思路：
（1）暴力两个for循环，超时
（2）双指针，容积为(j-i)*min{height[i], height[j]}，然后改变小的那个
"""


class Solution(object):
    @staticmethod
    def max_area(height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_volume = 0
        list_len = len(height)
        left = 0
        right = list_len - 1
        while left < right:
            list_height = height[left] if height[left] < height[right] else height[right]
            volume = (right - left) * list_height
            max_volume = volume if volume > max_volume else max_volume
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_volume
