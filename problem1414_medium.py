# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/3 11:31
"""
"""
给你数字 k ，请你返回和为 k 的斐波那契数字的最少数目，其中，每个斐波那契数字都可以被使用多次。
斐波那契数字定义为：
F1 = 1
F2 = 1
Fn = Fn-1 + Fn-2 ， 其中 n > 2 。
数据保证对于给定的 k ，一定能找到可行解。

输入：k = 7
输出：2 
解释：斐波那契数字为：1，1，2，3，5，8，13，……
对于 k = 7 ，我们可以得到 2 + 5 = 7 。

输入：k = 10
输出：2 
解释：对于 k = 10 ，我们可以得到 2 + 8 = 10 。

输入：k = 19
输出：3 
解释：对于 k = 19 ，我们可以得到 1 + 5 + 13 = 19 。
"""
"""
思路：每次选取不大于k的斐波那契数即可（主要是证明）
"""


class Solution(object):
    @staticmethod
    def find_min_fibonacci_numbers(k):
        """
        :type k: int
        :rtype: int
        """
        if k == 1:
            return k
        fibonacci = [1, 1]
        while fibonacci[-1] < k:
            fibonacci.append(fibonacci[-1]+fibonacci[-2])
        count = 0
        index = -1
        while k:
            if fibonacci[index] <= k:
                k -= fibonacci[index]
                count += 1
            index -= 1
        return count
