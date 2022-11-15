# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/18 9:52
"""
"""
给你一个整数 n ，按字典序返回范围 [1, n] 内所有整数。
你必须设计一个时间复杂度为 O(n) 且使用 O(1) 额外空间的算法。

输入：n = 13
输出：[1,10,11,12,13,2,3,4,5,6,7,8,9]

输入：n = 2
输出：[1,2]
"""
"""
思路：尝试在 number 后面附加一个零，即 number×10，如果 number×10≤n，那么说明 number×10 是下一个字典序整数；
如果 number%10=9 或 number+1>n，那么说明末尾的数位已经搜索完成，退回上一位，即number=number//10，然后继续判断直到number%10!=9
且 number+1≤n 为止，那么number+1 是下一个字典序整数。
"""


class Solution(object):
    @staticmethod
    def lexicalOrder(n):
        """
        :type n: int
        :rtype: List[int]
        """
        # nums = [str(num) for num in range(1, n+1)]
        # nums = sorted(nums)
        # ans = [int(num) for num in nums]
        # return ans

        ans = [1] * n
        num = 1
        for i in range(n):
            ans[i] = num
            if num * 10 <= n:
                num *= 10
            else:
                while num % 10 == 9 or num + 1 > n:
                    num //= 10
                num += 1
        return ans
