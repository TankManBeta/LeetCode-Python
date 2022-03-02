# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/1 11:03
"""
"""
给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。

输入: rowIndex = 3
输出: [1,3,3,1]

输入: rowIndex = 0
输出: [1]

输入: rowIndex = 1
输出: [1,1]
"""
"""
思路：
（1）同118，直接求出所有结果，然后返回rowIndex那一行的结果即可
（2）只用一个数组，每次都从后往前开始算，res[j] += res[j-1]，因为当前最后一个是1，下一行比当前行多一个数，所以下一行最后一个
仍然计算为1，然后一直往前计算
"""


class Solution(object):
    @staticmethod
    def get_row(row_index):
        """
        :type row_index: int
        :rtype: List[int]
        """
        # if row_index == 0:
        #     return [1]
        # if row_index == 1:
        #     return [1, 1]
        # res = [[1], [1, 1]]
        # for i in range(2, row_index + 1):
        #     row_res = [1]
        #     for j in range(1, i):
        #         row_res.append(res[i - 1][j - 1] + res[i - 1][j])
        #     row_res.append(1)
        #     res.append(row_res[:])
        # return res[row_index]

        res = [0] * (row_index + 1)
        res[0] = 1
        for i in range(1, row_index + 1):
            for j in range(i, 0, -1):
                res[j] += res[j - 1]
        return res
