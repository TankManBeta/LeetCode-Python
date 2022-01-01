# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/1/1 11:00
"""
"""
给你一个下标从0开始的一维整数数组original和两个整数m和n。你需要使用original中所有元素创建一个m行n列的二维数组。
original中下标从0到n-1（都包含）的元素构成二维数组的第一行，下标从n到2*n-1（都包含）的元素构成二维数组的第二行，依此类推。
请你根据上述过程返回一个mxn的二维数组。如果无法构成这样的二维数组，请你返回一个空的二维数组。

输入：original = [1,2,3,4], m = 2, n = 2
输出：[[1,2],[3,4]]
解释：
构造出的二维数组应该包含 2 行 2 列。
original 中第一个 n=2 的部分为 [1,2] ，构成二维数组的第一行。
original 中第二个 n=2 的部分为 [3,4] ，构成二维数组的第二行。

输入：original = [1,2,3], m = 1, n = 3
输出：[[1,2,3]]
解释：
构造出的二维数组应该包含 1 行 3 列。
将 original 中所有三个元素放入第一行中，构成要求的二维数组。

输入：original = [1,2], m = 1, n = 1
输出：[]
解释：
original 中有 2 个元素。
无法将 2 个元素放入到一个 1x1 的二维数组中，所以返回一个空的二维数组。

输入：original = [3], m = 1, n = 2
输出：[]
解释：
original 中只有 1 个元素。
无法将 1 个元素放满一个 1x2 的二维数组，所以返回一个空的二维数组。
"""
"""
思路：直接切片即可
"""


class Solution(object):
    @staticmethod
    def construct_2d_array(original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        list_len = len(original)
        if m*n != list_len:
            return []
        else:
            res = [original[i*n:(i+1)*n] for i in range(m)]
            return res
