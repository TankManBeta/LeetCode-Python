# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/4 10:34
"""
"""
给你一个数组 rectangles ，其中 rectangles[i] = [li, wi] 表示第 i 个矩形的长度为 li 、宽度为 wi 。
如果存在k同时满足k<=li和k<=wi，就可以将第 i 个矩形切成边长为 k 的正方形。例如，矩形 [4,6] 可以切成边长最大为 4 的正方形。
设 maxLen 为可以从矩形数组 rectangles 切分得到的 最大正方形 的边长。
请你统计有多少个矩形能够切出边长为 maxLen 的正方形，并返回矩形 数目 。

输入：rectangles = [[5,8],[3,9],[5,12],[16,5]]
输出：3
解释：能从每个矩形中切出的最大正方形边长分别是 [5,3,5,5] 。
最大正方形的边长为 5 ，可以由 3 个矩形切分得到。

输入：rectangles = [[2,3],[3,7],[4,3],[3,7]]
输出：3
"""
"""
思路：简单模拟题，遍历一遍统计当前边长和最大边长，如果相等就count++；如果大就把更新最大边长，count=1；如果小就continue
"""


class Solution(object):
    @staticmethod
    def count_good_rectangles(rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        max_len = 0
        count = 0
        for rectangle in rectangles:
            temp_len = min(rectangle[0], rectangle[1])
            if temp_len > max_len:
                max_len = temp_len
                count = 1
            elif temp_len == max_len:
                count += 1
            else:
                continue
        return count
