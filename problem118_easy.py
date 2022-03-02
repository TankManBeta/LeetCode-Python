# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/1 10:40
"""
"""
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。

输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

输入: numRows = 1
输出: [[1]]
"""
"""
思路：直接计算即可
"""


class Solution(object):
    @staticmethod
    def generate(num_rows):
        """
        :type num_rows: int
        :rtype: List[List[int]]
        """
        if num_rows == 1:
            return [[1]]
        if num_rows == 2:
            return[[1], [1, 1]]
        res = [[1], [1, 1]]
        for i in range(2, num_rows):
            row_res = [1]
            for j in range(1, i):
                row_res.append(res[i-1][j-1]+res[i-1][j])
            row_res.append(1)
            res.append(row_res[:])
        return res
