# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/1/21 12:20
"""
"""
给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。
按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下："123"，"132"，"213"，"231"，"312"，"321"
给定 n 和 k，返回第 k 个排列。

输入：n = 3, k = 3
输出："213"

输入：n = 4, k = 9
输出："2314"

输入：n = 3, k = 1
输出："123"
"""
"""
思路：
（1）dfs，但是会超时
（2）挨个位置确定，对于n位数，首先确定第一位是什么，remainder=(k-1)//(n-1)!，算出第一位的数，然后获得k%(n-1)!的余数作为新的k
"""


class Solution(object):
    @staticmethod
    def get_permutation(n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        options = [str(i) for i in range(1, n+1)]
        res = ''
        while n != 0:
            divisor = factorial[n-1]
            start_num = options[(k-1) // divisor]
            res += start_num
            k = k % divisor
            n -= 1
            options.remove(start_num)
        return res
