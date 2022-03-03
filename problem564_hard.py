# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/2 10:36
"""
"""
给定一个表示整数的字符串 n ，返回与它最近的回文整数（不包括自身）。如果不止一个，返回较小的那个。
“最近的”定义为两个整数差的绝对值最小。

输入: n = "123"
输出: "121"

输入: n = "1"
输出: "0"
解释: 0 和 2是最近的回文，但我们返回最小的，也就是 0。
"""
"""
思路：首先判断本身是否是回文数，然后根据取该字符串的前一半来构造上一个下个回文数，因为回文数就是将前一半的数重新倒序加在尾部，
所以最近的回文数的前半部分就在prefix-1，prefix，prefix+1，同时需要注意前半部分+1，-1之后越界的情况例如100-1=99，99+1=100
的情况，直接把边界的回文数构造加入集合即可
"""


class Solution(object):
    @staticmethod
    def nearest_palindromic(s):
        """
        :type s: str
        :rtype: str
        """
        if int(s) <= 9:
            return str(int(s)-1)
        is_palindromic = s == s[::-1]
        n = len(s)
        # 防止前半部分加减1之后再构造时位数减少的情况1003->99
        candidates = [10 ** (n-1) - 1, 10 ** n + 1]
        prefix = int(s[:(n+1)//2])
        # 在prefix-1，prefix，prefix+1中构造
        for i in range(prefix-1, prefix+2):
            # 本身就是回文数就不考虑
            if i == prefix and is_palindromic:
                continue
            # 原字符串长度为偶数，就把str(i)翻转一下加到后面
            if n%2 == 0:
                temp_s = str(i)
                temp = int(temp_s+temp_s[::-1])
                candidates.append(temp)
            # 长度为奇数，str(i)的最后一个只需要一次
            else:
                temp_s = str(i)
                temp = int(temp_s[0:-1]+temp_s[::-1])
                candidates.append(temp)
        number = int(s)
        max_gap = 10**18
        ans = -1
        for candidate in candidates:
            if abs(candidate-number) < max_gap:
                max_gap = abs(candidate-number)
                ans = candidate
        return str(ans)
