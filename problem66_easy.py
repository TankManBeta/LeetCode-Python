# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/1/28 10:53
"""
"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。

输入：digits = [0]
输出：[1] 
"""
"""
思路：从最后一维开始，每一位加1直到carry为0，如果到第一位还需要进位就在第1个位置再插入一个1
"""


class Solution(object):
    @staticmethod
    def plus_one(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            if carry == 1:
                digits[i] += 1
                if digits[i] == 10:
                    digits[i] = 0
                    if i == 0:
                        digits.insert(0, 1)
                else:
                    break
            else:
                break
        return digits
