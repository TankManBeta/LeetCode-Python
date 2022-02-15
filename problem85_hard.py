# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/14 21:35
"""
"""
给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：6

输入：matrix = []
输出：0

输入：matrix = [["0"]]
输出：0

输入：matrix = [["1"]]
输出：1

输入：matrix = [["0","0"]]
输出：0
"""
"""
思路：同84题，调用84的题目m次即可，每次的heights就是统计前几行每一列1的个数
"""


class Solution(object):
    @staticmethod
    def maximal_rectangle(matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def largest_rectangle_area(height):
            """
            :type height: List[int]
            :rtype: int
            """
            height = [0] + height + [0]
            height_len = len(height)
            res = 0
            stack = []
            for i in range(height_len):
                while stack and height[stack[-1]] > height[i]:
                    temp = stack.pop()
                    res = max(res, (i - stack[-1] - 1) * height[temp])
                stack.append(i)
            return res

        m = len(matrix)
        n = len(matrix[0])
        ans = 0
        heights = [0 for _ in range(n)]
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == '0':
                    heights[col] = 0
                else:
                    heights[col] += 1
            ans = max(ans, largest_rectangle_area(heights))
        return ans
