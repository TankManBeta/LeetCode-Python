# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/12 9:47
"""
"""
给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。
如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。

输入：n = 1
输出：true
解释：20 = 1

输入：n = 16
输出：true
解释：24 = 16

输入：n = 3
输出：false

输入：n = 4
输出：true

输入：n = 4
输出：true
"""
"""
思路：
（1）最开始思路是n&n-1统计有多少个1，如果大于1个就不是
（2）既然已经想到n&n-1，直接判断去除最后一个1之后是不是为0即可
（3）n&-n获取最后一个1，如果和n相等说明本身就是2的幂
（4）判断是否为最大2的幂的约数
"""


class Solution(object):
    @staticmethod
    def isPowerOfTwo(n):
        """
        :type n: int
        :rtype: bool
        """
        # if n<=0:
        #     return False
        # count = 0
        # while n:
        #     n &= n-1
        #     count += 1
        # return True if count == 1 else False

        # return n > 0 and (n & (n - 1)) == 0

        # return n > 0 and (n & -n) == n

        BIG = 2**30
        return n > 0 and BIG % n == 0
